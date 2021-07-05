from aiogram.dispatcher.filters.state import StatesGroup, State


class RegistrationNewUser(StatesGroup):
    choice_language = State()
    agree_rules = State()
    subscribe_main_chat = State()
