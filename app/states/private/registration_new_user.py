from aiogram.dispatcher.filters.state import StatesGroup, State


class RegistrationUser(StatesGroup):
    agree_rules = State()
    subscribe_main_chat = State()
