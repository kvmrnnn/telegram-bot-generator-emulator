from aiogram.types import Message

from app.data import text
from app.loader import dp, config


@dp.message_handler(text=text[config.bot.default_lang].button.admin.reply.create_promocode)
@dp.message_handler(text=text[config.bot.second_lang].button.admin.reply.create_promocode)
async def create_promo_code(message: Message, lang_code):
    await message.answer(
        text=text[lang_code].message.admin.create_prom_enter_data
    )
