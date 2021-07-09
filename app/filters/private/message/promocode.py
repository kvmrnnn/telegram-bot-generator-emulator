from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message
from loguru import logger

from app.utils.db_api.models.promocode_model import Promocode


class PromocodeFilter(BoundFilter):
    key = 'is_promocode'

    def __init__(self, is_promocode: bool = True):
        pass

    async def check(self, message: Message) -> bool:
        if not message.text:
            return False
        promocode_code = message.text.replace('/start', '').strip()
        promocode = await Promocode.get(promocode_code)
        if promocode:
            return {'promocode_obj': promocode}
