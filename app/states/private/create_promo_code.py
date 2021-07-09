from aiogram.dispatcher.filters.state import StatesGroup, State


class CreatePromoCode(StatesGroup):
    wait_for_data = State()
