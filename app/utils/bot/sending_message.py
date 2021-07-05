from typing import List, Union

from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup, Message

from app.utils.db_api import db
from app.utils.db_api.models.user import User


async def text_message(text: str,
                       roles: Union[str, List[str]] = None,
                       chats_id: Union[int, List[int]] = None,
                       markup: InlineKeyboardMarkup = None,
                       **where_conditions
                       ) -> List[int]:

    bot = Bot.get_current()
    list_not_success = []

    if chats_id is None:
        chats_id = []
    elif isinstance(chats_id, int):
        chats_id = [chats_id]
    elif isinstance(chats_id, str):
        chats_id = [int(chats_id)]


    if roles is not None:
        users = []
        for role in roles:
            users + await db.all(User.query.where(User.qf(role=role, **where_conditions)))

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
    elif isinstance(chats_id, int):
        chats_id = [chats_id]
    elif isinstance(chats_id, str):
        chats_id = [int(chats_id)]

    if roles is not None:
        users = []
        for role in roles:
            users + await db.all(User.query.where(User.qf(role=role, **where_conditions)))

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
    elif isinstance(chats_id, int):
        chats_id = [chats_id]
    elif isinstance(chats_id, str):
        chats_id = [int(chats_id)]


    if roles is not None:
        users = []
        for role in roles:
            users + await db.all(User.query.where(User.qf(role=role, **where_conditions)))

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
