from app.data.types.lang import LangCode
from app.data.types.user import UserUsername


def format_username(username: str) -> str:
    if username == UserUsername.NONE:
        return 'Not Username'
    return '@' + username


def format_fullname(full_name: str) -> str:
    new_full_name = ''
    for char in full_name:
        if char == '<':
            new_full_name += '&lt;'
        elif char == '>':
            new_full_name += '&gt;'
        else:
            new_full_name += char

    return new_full_name


def format_lang_code(lang_code: str) -> str:
    if lang_code == LangCode.RU:
        return '🇷🇺 Русский'
    elif lang_code == LangCode.ENG:
        return '🇺🇸 English'

    return 'He yдaлocb oпpeдeлutb Я3ыk'

