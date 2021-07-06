from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message

from app.loader import dp
from app.utils.bot import send_main_keyboard


@dp.message_handler(CommandStart())
async def message_on(message: Message, user, lang_code):
    await send_main_keyboard(user)
