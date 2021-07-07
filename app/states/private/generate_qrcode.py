from aiogram.dispatcher.filters.state import StatesGroup, State


class GenerateQRCode(StatesGroup):
    process_generate = State()
