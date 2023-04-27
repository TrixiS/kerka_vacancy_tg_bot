import asyncio

from prisma import Prisma

from .bot import DISPATCHER
from .middleware.bot_user_middleware import BotUserMiddleware


async def main():
    prisma = Prisma(auto_register=True)
    await prisma.connect()

    DISPATCHER.middleware.setup(BotUserMiddleware())
    await DISPATCHER.start_polling()


asyncio.run(main())
