from aiogram import types

from ... import markups
from ...bot import DISPATCHER
from ...phrases import PHRASES


@DISPATCHER.message_handler(commands=["admin"])
async def admin_command_handler(message: types.Message):
    await message.answer(
        PHRASES.admin.admin_message_text, reply_markup=markups.ADMIN_MARKUP
    )
