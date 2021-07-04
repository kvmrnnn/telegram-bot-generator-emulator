from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from app.data import text

keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text=text.button.default.reply.agree_rules)
        ]
    ]
)