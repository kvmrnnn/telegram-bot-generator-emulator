from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.data.types.lang import LangCode
from app.keyboards.default.callback_data.settings_profile import choice_lang_cd
from app.utils.db_api.models.user import User
from app.utils.format_data.user import format_lang_code


def keyboard(user: User) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=1)
    if user.lang == LangCode.RU:
        markup.insert(
            InlineKeyboardButton(
                text=format_lang_code(LangCode.ENG),
                callback_data=choice_lang_cd.new(user_id=user.id, lang_code=LangCode.ENG)
            )
        )
    elif user.lang == LangCode.ENG:
        markup.insert(
            InlineKeyboardButton(
                text=format_lang_code(LangCode.RU),
                callback_data=choice_lang_cd.new(user_id=user.id, lang_code=LangCode.RU)
            )
        )
    return markup
