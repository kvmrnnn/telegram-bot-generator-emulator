from datetime import datetime

from app.data.types.lang import LangCode


def format_username(username: str) -> str:
    """
    Formatting username to string.
    Args:
        username: username

    Returns:
        Formatted username.
    """

    if str(username) == 'None':
        username = 'No username'
    else:
        username = '@' + username

    return username

def format_premium_to_up(t: datetime, lang_code: str) -> str:
    """

    Args:
        t:
        lang_code:

    Returns:

    """
    t_now = datetime.utcnow()
    if t < t_now and lang_code == LangCode.RU:
        return 'Не активен'
    elif t > t_now and lang_code == LangCode.RU:
        return f'Активен до {str(t)[:-7]}. (Нулевой часовой пояс)'

    if t < t_now and lang_code == LangCode.ENG:
        return 'Not active'
    elif t > t_now and lang_code == LangCode.ENG:
        return f'Active until {str(t)[:-8]}. (Zero time zone)'


def format_fullname(fullname: str) -> str:
    """
    Formatting user fullname.
    Replace html symbol to html code.
    Args:
        fullname: String.

    Returns:
        Formatted user fullname.

    """
    new_fullname = ''
    for char in fullname:
        if char == '<':
            new_fullname += '&lt;'
        elif char == '>':
            new_fullname += '&gt;'
        else:
            new_fullname += char

    return new_fullname


def format_lang_code(lang_code: str) -> str:
    """
    Formatting language code to string.
    Args:
        lang_code: language code.

    Returns:
        String formatted language code.

    """
    if lang_code == LangCode.RU:
        return '🇷🇺 Русский'
    elif lang_code == LangCode.ENG:
        return '🇺🇸 English'

    return 'He yдaлocb oпpeдeлutb Я3ыk'
