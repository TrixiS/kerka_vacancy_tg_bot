from aiogram import types

from .callback_data import DEPOSIT_CALLBACK_DATA
from .phrases import PHRASES

DEPOSIT_MARKUP = types.InlineKeyboardMarkup().add(
    types.InlineKeyboardButton(
        text=PHRASES.deposit_button_text, callback_data=DEPOSIT_CALLBACK_DATA.new()
    )
)
