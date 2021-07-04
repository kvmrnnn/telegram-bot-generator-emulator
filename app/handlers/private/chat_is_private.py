from typing import Union

from aiogram.types import ChatType, Message, CallbackQuery

from app.filters.is_not_chat_type import NotChatType
from app.loader import dp


@dp.callback_query_handler(NotChatType(ChatType.PRIVATE))
@dp.message_handler(NotChatType(ChatType.PRIVATE))
async def chat_not_private(obj: Union[Message, CallbackQuery]):
    pass
