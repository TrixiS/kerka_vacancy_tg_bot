import asyncio
import logging

import bot.handlers.user.deposit  # noqa
import bot.handlers.user.start  # noqa
from prisma import Prisma

from .bot import DISPATCHER
from .middleware.bot_user_middleware import BotUserMiddleware

logging.basicConfig(
    # filename=log_filename,
    level=logging.DEBUG,
    format=r"%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s",
)


async def main():
    prisma = Prisma(auto_register=True)
    await prisma.connect()

    # DISPATCHER.middleware.setup(BotUserMiddleware())
    await DISPATCHER.start_polling()


asyncio.run(main())
