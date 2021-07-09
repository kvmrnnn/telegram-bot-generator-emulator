from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.data import text
from app.loader import dp, config
from app.utils.bot import send_main_keyboard


@dp.message_handler(text=text[config.bot.default_lang].button.default.reply.cancel, state='*')
@dp.message_handler(text=text[config.bot.second_lang].button.default.reply.cancel, state='*')
async def cancel(message: Message, user, state: FSMContext):
    await send_main_keyboard(user, state)
