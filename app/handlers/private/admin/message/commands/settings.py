from aiogram.dispatcher.filters import CommandSettings
from aiogram.types import Message

from app.data.types.user import UserRole
from app.filters.private.user.user_role import UserRoleFilter
from app.loader import dp

@dp.message_handler(UserRoleFilter([UserRole.ADMIN]), CommandSettings())
async def send_menu_settings(message: Message):
    await message.answer(
        text='Меню настроек',
    )