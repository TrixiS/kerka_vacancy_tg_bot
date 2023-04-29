from aiogram import types
from aiogram.dispatcher import FSMContext
from prisma.models import BotUser

from ... import markups
from ...bot import DISPATCHER
from ...filters import INT_TEXT_FILTER
from ...phrases import PHRASES
from ...state import SetBalanceState


@DISPATCHER.message_handler(lambda m: m.text == PHRASES.admin.set_balance_button_text)
async def set_balance_handler(message: types.Message):
    await SetBalanceState.waiting_user_id.set()
    await message.answer(PHRASES.admin.enter_user_id_message_text)


@DISPATCHER.message_handler(INT_TEXT_FILTER, state=SetBalanceState.waiting_user_id)
async def user_id_handler(message: types.Message, state: FSMContext):
    await SetBalanceState.waiting_amount.set()

    async with state.proxy() as state_data:
        state_data["user_id"] = int(message.text)

    await message.answer(PHRASES.admin.enter_amount_message_text)


@DISPATCHER.message_handler(INT_TEXT_FILTER, state=SetBalanceState.waiting_amount)
async def amount_handler(message: types.Message, state: FSMContext):
    state_data = await state.get_data()
    await state.finish()

    await BotUser.prisma().update(
        where={"id": state_data["user_id"]}, data={"balance": int(message.text)}
    )

    await message.answer(
        PHRASES.admin.set_balance_message_text, reply_markup=markups.ADMIN_MARKUP
    )
