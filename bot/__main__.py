import asyncio
import logging
from logging.handlers import RotatingFileHandler

import bot.handlers.user.deposit  # noqa
import bot.handlers.user.start  # noqa
from prisma import Prisma

from . import ROOT_PATH
from .bot import DISPATCHER
from .middleware.bot_user_middleware import BotUserMiddleware

LOG_LEVEL = logging.DEBUG

logging.getLogger("prisma").setLevel(LOG_LEVEL)

file_log_formatter = logging.Formatter(
    r"%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s"
)
file_log_handler = RotatingFileHandler(
    ROOT_PATH / "logs.log",
    mode="a",
    maxBytes=15 * 1024 * 1024,
    backupCount=2,
    encoding="utf-8",
)

file_log_handler.setFormatter(file_log_formatter)
file_log_handler.setLevel(LOG_LEVEL)

app_log = logging.getLogger("root")
app_log.setLevel(logging.INFO)

root_logger = logging.getLogger("root").addHandler(file_log_handler)
logging.getLogger("root").setLevel(LOG_LEVEL)


async def main():
    prisma = Prisma(auto_register=True)
    await prisma.connect()

    DISPATCHER.middleware.setup(BotUserMiddleware())
    await DISPATCHER.start_polling()


asyncio.run(main())
