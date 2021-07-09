from aiogram.types import Message

from app.data import text
from app.data.types.user import UserRole
from app.keyboards.admin import reply
from app.loader import dp, config


@dp.message_handler(user_role=UserRole.ADMIN, text=text[config.bot.default_lang].button.admin.reply.menu_promocodes)
@dp.message_handler(user_role=UserRole.ADMIN, text=text[config.bot.second_lang].button.admin.reply.menu_promocodes)
async def choose_action(message: Message, lang_code):
    await message.answer(
        text=text[lang_code].message.admin.choose_action,
        reply_markup=reply.promocodes.choose_action.make_keyboard_choose_action(lang_code)
    )
