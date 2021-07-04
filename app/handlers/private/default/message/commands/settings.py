from aiogram.dispatcher.filters import CommandSettings
from aiogram.types import Message

from app.loader import dp

@dp.message_handler(CommandSettings())
async def send_menu_settings(message: Message):
    await message.answer(
        text='Меню настроек',
    )