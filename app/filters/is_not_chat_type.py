from typing import Union, List

from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message, CallbackQuery


class NotChatType(BoundFilter):

    def __init__(self, chat_types: List[str]):

        if isinstance(chat_types, list):
            self.chat_types = list(set(chat_types))
        elif isinstance(chat_types, str):
            self.chat_types = [chat_types]

    async def check(self, obj: Union[Message, CallbackQuery]) -> bool:
        if isinstance(obj, CallbackQuery):
            obj = obj.message
        return not (obj.chat.type in self.chat_types)
