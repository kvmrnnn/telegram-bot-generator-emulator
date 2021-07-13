from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from app.data import text


def make_keyboard(lang_code):
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(
                    text=text[lang_code].button.default.reply.magnit
                ),
                KeyboardButton(
                    text=text[lang_code].button.default.reply.pyaterochka
                )
            ],
            [
                KeyboardButton(
                    text=text[lang_code].button.default.reply.cancel
                )
            ]
        ]
    )
    return keyboard
