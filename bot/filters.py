from typing import Union

from aiogram import types
from prisma.models import BotUser

from .enums import BotUserRole

INT_TEXT_FILTER = lambda m: m.text and m.text.isdigit()


async def not_banned_user_filter(event: Union[types.Message, types.CallbackQuery]):
    bot_user = await BotUser.prisma().find_unique(where={"id": event.from_user.id})

    if bot_user is None:
        return True

    return bot_user.role != BotUserRole.banned
