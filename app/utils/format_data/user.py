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