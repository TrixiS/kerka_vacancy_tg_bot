from aiogram.dispatcher.filters.state import State, StatesGroup


class DepositState(StatesGroup):
    waiting_amount = State()


class SetBalanceState(StatesGroup):
    waiting_user_id = State()
    waiting_amount = State()


class BanUserState(StatesGroup):
    waiting_user_id = State()
