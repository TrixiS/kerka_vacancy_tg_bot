from aiogram.dispatcher.filters.state import State, StatesGroup


class DepositState(StatesGroup):
    waiting_amount = State()
