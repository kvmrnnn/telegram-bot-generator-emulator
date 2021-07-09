from aiogram.dispatcher.filters.state import StatesGroup, State


class DeletePromoCode(StatesGroup):
    wait_for_code = State()
