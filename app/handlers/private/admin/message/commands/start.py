from asyncio import sleep

from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message

from app import keyboards
from app.data.types.user import UserDeepLink, UserRole
from app.filters.private.user import NewUser
from app.loader import dp
from app.utils.db_api.models.user import User


@dp.message_handler(CommandStart(), NewUser(), user_role=UserRole.ADMIN)
async def start_new_user(message: Message):

    # deep link
    try:
        deep_link = int(message.get_args())
    except:
        deep_link = UserDeepLink.NONE

    # Add new user in database
    await User.insert(
        id=message.from_user.id,
        full_name=message.from_user.full_name,
        lang=message.from_user.language_code,
        username=message.from_user.username,
        deep_link=deep_link,
        role=UserRole.ADMIN,
        is_read_rules=True,
    )

    await message.answer(
        'Добро пожаловать, админ'
    )
