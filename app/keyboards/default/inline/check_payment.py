from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.data import text
from app.data.types.menu_cd import MenuProfileCd
from app.keyboards.default.callback_data.profile.main_profile import payment_cd


def make_keyboard_check_payment(lang_code, comment: str):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=text[lang_code].button.default.inline.check_payment,
                    callback_data=payment_cd.new(comment=comment, command=MenuProfileCd.check_payment)
                )
            ]
        ]
    )
    return keyboard
