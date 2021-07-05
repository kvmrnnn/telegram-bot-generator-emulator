from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message

from app.loader import dp


@dp.message_handler(CommandStart())
async def message_on(message: Message, user_lang):
    pass
