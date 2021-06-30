
from aiogram.dispatcher.filters import CommandStart, AdminFilter
from aiogram.types import Message, User

from app.loader import dp


@dp.message_handler(CommandStart())
async def message_on(message: Message):
    pass
