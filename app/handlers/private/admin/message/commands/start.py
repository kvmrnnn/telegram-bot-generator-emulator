from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message

from app.data.types.user import UserRole
from app.loader import dp
from app.utils.bot import send_main_keyboard


@dp.message_handler(CommandStart(), user_role=UserRole.ADMIN)
async def start_new_user(message: Message, user):
    await send_main_keyboard(user)
