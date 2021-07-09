from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from app.data import text


def keyboard(lang_code) -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text[lang_code].button.default.reply.profile),
                KeyboardButton(text[lang_code].button.default.reply.menu_soft),
            ],
            [
                KeyboardButton(text[lang_code].button.default.reply.information)
            ]
        ]
    )
    return markup
