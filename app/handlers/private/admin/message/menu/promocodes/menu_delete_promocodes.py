from aiogram.types import Message

from app.data import text
from app.keyboards.admin import reply
from app.loader import dp, config


@dp.message_handler(text=text[config.bot.default_lang].button.admin.reply.delete_promocode)
@dp.message_handler(text=text[config.bot.second_lang].button.admin.reply.delete_promocode)
async def send_prom_delete_menu(message: Message, lang_code):
    await message.answer(
        text=text[lang_code].message.admin.choose_action,
        reply_markup=reply.promocodes.prom_delete_menu.make_keyboard_choose_action(lang_code)
    )
