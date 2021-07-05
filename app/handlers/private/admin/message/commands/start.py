from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message

from app.data.types.user import UserRole
from app.loader import dp


@dp.message_handler(CommandStart(), user_role=UserRole.ADMIN)
async def start_new_user(message: Message):
    pass
