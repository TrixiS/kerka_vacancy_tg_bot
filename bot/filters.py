from typing import Union

from aiogram import types
from prisma.models import BotUser

from .enums import BotUserRole

INT_TEXT_FILTER = lambda m: m.text and m.text.isdigit()
