from aiogram import types
from aiogram.dispatcher import FSMContext
from prisma.models import BotUser

from ... import markups
from ...bot import DISPATCHER
from ...enums import BotUserRole
from ...filters import INT_TEXT_FILTER
from ...phrases import PHRASES
from ...state import BanUserState


@DISPATCHER.message_handler(lambda m: m.text == PHRASES.admin.ban_user_button_text)
async def ban_user_handler(message: types.Message):
    await BanUserState.waiting_user_id.set()
    await message.answer(PHRASES.admin.enter_user_id_message_text)


@DISPATCHER.message_handler(INT_TEXT_FILTER, state=BanUserState.waiting_user_id)
async def user_id_handler(message: types.Message, state: FSMContext):
    await state.finish()

    await BotUser.prisma().update(
        where={"id": int(message.text)}, data={"role": BotUserRole.banned}
    )

    await message.answer(
        PHRASES.admin.ban_user_message_text, reply_markup=markups.ADMIN_MARKUP
    )
