from aiogram import types
from pyqiwip2p.p2p_types import Bill

from .callback_data import CHECK_PAYMENT_CALLBACK_DATA, DEPOSIT_CALLBACK_DATA
from .phrases import PHRASES

DEPOSIT_MARKUP = types.InlineKeyboardMarkup().add(
    types.InlineKeyboardButton(
        text=PHRASES.deposit_button_text, callback_data=DEPOSIT_CALLBACK_DATA.new()
    )
)

ADMIN_MARKUP = (
    types.ReplyKeyboardMarkup(resize_keyboard=True)
    .row(
        types.KeyboardButton(text=PHRASES.admin.export_users_button_text),
        types.KeyboardButton(text=PHRASES.admin.export_logs_button_text),
    )
    .row(
        types.KeyboardButton(text=PHRASES.admin.set_balance_button_text),
        types.KeyboardButton(text=PHRASES.admin.ban_user_button_text),
    )
)


def create_check_payment_markup(bill: Bill):
    return (
        types.InlineKeyboardMarkup()
        .row(types.InlineKeyboardButton(text=PHRASES.pay_button_text, url=bill.pay_url))
        .row(
            types.InlineKeyboardButton(
                text=PHRASES.check_payment_button_text,
                callback_data=CHECK_PAYMENT_CALLBACK_DATA.new(bill.bill_id),
            )
        )
    )
