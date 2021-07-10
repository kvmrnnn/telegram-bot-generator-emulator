from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.data import text
from app.data.types.soft import CategorySoft, SoftCommand
from app.keyboards.default.callback_data.soft import menu_soft_cd


def keyboard(lang_code: str) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=text[lang_code].button.premium.inline.menu_soft_magnit,
                    callback_data=menu_soft_cd.new(category_soft=CategorySoft.MAGNIT, event=SoftCommand.NONE)
                )
            ],
            [
                InlineKeyboardButton(
                    text=text[lang_code].button.premium.inline.menu_soft_pyaterochka,
                    callback_data=menu_soft_cd.new(category_soft=CategorySoft.PYATEROCHKA, event=SoftCommand.NONE)
                )
            ]
        ]
    )
    return markup
