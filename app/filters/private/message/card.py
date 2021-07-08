import os
from io import BufferedWriter
from typing import Union

from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message
from loguru import logger

from app.data.types.card import CardBank
from app.utils.format_data.card import format_code


class MagnitCardFilter(BoundFilter):
    key = 'magnit_card'

    def __init__(self, magnit_card: bool = None):
        pass

    async def check(self, message: Message) -> Union[bool, dict[str, dict]]:
        if message.document:
            file_document: BufferedWriter = await message.document.download('./app/data/tmp')
            file_document.close()
            with open(file_document.name, encoding='UTF-8') as file:
                text = file.read()
            os.remove(file_document.name)
        elif message.text:
            text = message.text
        else:
            return False

        cards_data = {}
        for data in text.splitlines():
            code = format_code(data)
            if code and CardBank.is_code_valid(code):
                cards_data.setdefault(code, data)
        if len(cards_data):
            return {'cards_data': cards_data}
        return False
