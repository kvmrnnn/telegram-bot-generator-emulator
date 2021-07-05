from aiogram.types import Message

from app import dp
from app.loader import config


@dp.message_handler(state='*')
async def send_main_keyboard(message: Message, user, user_lang):
    await message.answer(f'Debug: Ни один хедлер не поймал это событие')
