from typing import List

from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup, Message

from app.utils.db_api import db
from app.utils.db_api.models.user import User


async def text(text: str,
               roles: str = None,
               chats_id: List[int] = None,
               markup: InlineKeyboardMarkup = None,
               **where_conditions
               ) -> List[int]:

    bot = Bot.get_current()
    list_not_success = []

    if chats_id is None:
        chats_id = []

    if isinstance(chats_id, int):
        chats_id = [chats_id]

    if roles is not None:
        users = await db.all(User.query.where(User.qf(**where_conditions)))
        chats_id += [user.id for user in users if user.is_role(roles)]

    for chat_id in set(chats_id):
        try:
            await bot.send_message(
                chat_id=chat_id,
                text=text,
                reply_markup=markup
            )
        except:
            list_not_success.append(chat_id)
            continue

    return list_not_success


async def copy_message(message: Message,
               roles: str = None,
               chats_id: List[int] = None,
               markup: InlineKeyboardMarkup = None,
               **where_conditions
               ) -> List[int]:
    bot = Bot.get_current()
    list_not_success = []

    if chats_id is None:
        chats_id = []

    if isinstance(chats_id, int):
        chats_id = [chats_id]

    if roles is not None:
        users = await db.all(User.query.where(User.qf(**where_conditions)))
        chats_id += [user.id for user in users if user.is_role(roles)]

    for chat_id in set(chats_id):
        try:
            await bot.copy_message(
                chat_id=chat_id,
                from_chat_id=message.from_user.id,
                message_id=message.message_id,
                reply_markup=markup
            )
        except:
            list_not_success.append(chat_id)
            continue

    return list_not_success

async def forward_message(message: Message,
               roles: str = None,
               chats_id: List[int] = None,
               **where_conditions
               ) -> List[int]:
    bot = Bot.get_current()
    list_not_success = []

    if chats_id is None:
        chats_id = []

    if isinstance(chats_id, int):
        chats_id = [chats_id]

    if roles is not None:
        users = await db.all(User.query.where(User.qf(**where_conditions)))
        chats_id += [user.id for user in users if user.is_role(roles)]

    for chat_id in set(chats_id):
        try:
            await bot.forward_message(
                chat_id=chat_id,
                from_chat_id=message.from_user.id,
                message_id=message.message_id,
            )
        except:
            list_not_success.append(chat_id)
            continue

    return list_not_success