from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from app.loader import config
from app.utils.format_data.user import format_lang_code


def keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.insert(
        KeyboardButton(format_lang_code(config.bot.default_lang))
    )
    if config.bot.default_lang != config.bot.second_lang:
        markup.insert(
            KeyboardButton(format_lang_code(config.bot.second_lang))
        )
    return markup
