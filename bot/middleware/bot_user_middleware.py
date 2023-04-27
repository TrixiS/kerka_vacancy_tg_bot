from typing import Any, Dict

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from prisma.models import BotUser


class BotUserMiddleware(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: Dict[str, Any]):
        bot_user = await BotUser.prisma().find_unique(
            where={"id": message.from_user.id}
        )

        if bot_user is None:
            bot_user = await BotUser.prisma().create(data={"id": message.from_user.id})

        data["bot_user"] = bot_user
