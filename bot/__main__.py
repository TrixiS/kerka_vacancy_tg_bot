import asyncio

from aiogram import types

from .bot import DISPATCHER


async def main():
    await DISPATCHER.start_polling()


asyncio.run(main())
