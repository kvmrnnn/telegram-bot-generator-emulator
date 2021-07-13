from aiogram.dispatcher.filters.state import StatesGroup, State


class ChooseCard(StatesGroup):
    wait_for_type = State()
