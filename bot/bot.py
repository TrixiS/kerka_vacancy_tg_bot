from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from .env import env

BOT = Bot(token=env.bot_token)
DISPATCHER = Dispatcher(BOT, storage=MemoryStorage())
