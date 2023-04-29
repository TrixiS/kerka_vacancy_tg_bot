from typing import Any, Dict

from aiogram import types
from aiogram.dispatcher import FSMContext
from prisma.models import BotUser
from pyqiwip2p import AioQiwiP2P

from ... import filters, markups
from ...bot import BOT, DISPATCHER
from ...callback_data import CHECK_PAYMENT_CALLBACK_DATA, DEPOSIT_CALLBACK_DATA
from ...env import env
from ...phrases import PHRASES
from ...state import DepositState

BILL_LIFETIME_MINUTES = 5

QIWI_API_CLIENT = AioQiwiP2P(auth_key=env.qiwi_p2p_key)


@DISPATCHER.callback_query_handler(
    DEPOSIT_CALLBACK_DATA.filter(), filters.not_banned_user_filter
)
async def deposit_handler(query: types.CallbackQuery):
    await query.answer()
    await DepositState.waiting_amount.set()
    await BOT.send_message(
        query.from_user.id, PHRASES.enter_deposit_amount_message_text
    )


@DISPATCHER.message_handler(
    lambda m: m.text and m.text.isdigit(),
    filters.not_banned_user_filter,
    state=DepositState.waiting_amount,
)
async def deposit_amount_handler(message: types.Message, state: FSMContext):
    amount = int(message.text)

    try:
        bill = await QIWI_API_CLIENT.bill(amount=amount, lifetime=BILL_LIFETIME_MINUTES)
    except Exception:
        return await message.answer(PHRASES.invalid_deposit_amount_message_text)

    await state.finish()

    await message.answer(
        PHRASES.bill_message_text,
        reply_markup=markups.create_check_payment_markup(bill),
    )


@DISPATCHER.callback_query_handler(
    CHECK_PAYMENT_CALLBACK_DATA.filter(), filters.not_banned_user_filter
)
async def check_payment_handler(
    query: types.CallbackQuery, callback_data: Dict[str, Any]
):
    bill = await QIWI_API_CLIENT.check(callback_data["bill_id"])

    if bill.status != "PAID":
        return await query.answer(PHRASES.unpaid_bill_answer_text, show_alert=True)

    await BotUser.prisma().update(
        where={"id": query.from_user.id},
        data={"balance": {"increment": int(float(bill.amount))}},
    )

    await query.message.edit_text(text=PHRASES.deposit_message_text)
