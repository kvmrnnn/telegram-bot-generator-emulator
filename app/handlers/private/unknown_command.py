from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app import dp
from app.utils.bot import send_main_keyboard


@dp.message_handler(state='*')
async def unknown_command(message: Message, state: FSMContext, user, lang_code):
    await send_main_keyboard(user, state)
