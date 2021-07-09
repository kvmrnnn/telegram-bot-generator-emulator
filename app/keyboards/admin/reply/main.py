from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from loguru import logger

from app.data import text


def keyboard(lang_code) -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text[lang_code].button.admin.reply.search_info)
            ],
            [
                KeyboardButton(text[lang_code].button.default.reply.profile)
            ],
            [
                KeyboardButton(text[lang_code].button.admin.reply.menu_promocodes),
                KeyboardButton(text[lang_code].button.admin.reply.sending_messages),
            ]
        ]
    )
    return markup


