from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from app.data import text


def make_keyboard_choose_action(lang_code):
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(
                    text=text[lang_code].button.admin.reply.delete_all_proms
                ),
                KeyboardButton(
                    text=text[lang_code].button.admin.reply.delete_prom_by_code
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
