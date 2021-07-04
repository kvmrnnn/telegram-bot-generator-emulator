from typing import Union

from aiogram.types import Message, CallbackQuery

from app.filters.private.message.not_command import NotCommand
from app.filters.private.user import NewUser
from app.loader import dp


@dp.callback_query_handler(NewUser())
@dp.message_handler(NewUser(), NotCommand('start'))
async def user_not_db(obj: Union[Message, CallbackQuery]):
    await dp.bot.send_message(
        chat_id=obj.from_user.id,
        text='Упс, я не нашел вас в своей базе данных.\n'
             'Пропишите /start'
    )