from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.data import text
from app.data.types.menu_cd import MenuProfileCd
from app.keyboards.default.callback_data.profile.main_profile import profile_cd


def make_keyboard_profile(lang_code):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=text[lang_code].button.default.inline.increase_balance,
                    callback_data=profile_cd.new(command=MenuProfileCd.increase_balance)
                )
            ]
        ]
    )
    return keyboard
