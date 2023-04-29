from aiogram import types

from ... import filters, markups
from ...bot import DISPATCHER
from ...phrases import PHRASES


@DISPATCHER.message_handler(filters.not_banned_user_filter, commands=["start"])
async def start_command_handler(message: types.Message):
    await message.answer(
        PHRASES.start_message_text_fmt.format(full_name=message.from_user.full_name),
        reply_markup=markups.DEPOSIT_MARKUP,
    )
