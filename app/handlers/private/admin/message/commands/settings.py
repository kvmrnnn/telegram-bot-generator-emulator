from aiogram.dispatcher.filters import CommandSettings
from aiogram.types import Message

from app.data.types.user import UserRole
from app.loader import dp

@dp.message_handler(CommandSettings(), user_role=UserRole.ADMIN)
async def send_menu_settings(message: Message):
    pass