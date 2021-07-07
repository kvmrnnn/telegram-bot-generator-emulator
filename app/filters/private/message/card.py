from typing import Union

from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message
from loguru import logger

from app.data.types.card import Card
from app.utils.format_data.card import format_code


class MagnitCardFilter(BoundFilter):
    key = 'magnit_card'
    def __init__(self, magnit_card: bool = None):
        pass
    async def check(self, message: Message) -> Union[bool, dict[str, dict]]:
        if message.document:
            async with await message.document.download('./app/data/tmp', make_dirs=False) as file:
                text = file.read()
        elif message.text:
            text = message.text
        else:
            return False
        logger.debug(text)

        cards_data = {}
        for data in text.splitlines():
            code = format_code(data)
            if code and Card.is_code_valid(code):
                cards_data.setdefault(code, data)
        if len(cards_data):
            return {'cards_data': cards_data}
        return False
