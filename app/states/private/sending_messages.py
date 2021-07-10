from aiogram.dispatcher.filters.state import StatesGroup, State


class SendingMessages(StatesGroup):
    wait_for_message = State()
