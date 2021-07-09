from aiogram.types import Message
from loguru import logger

from app.data import text
from app.loader import dp
from app.utils.db_api.models.promocode_model import Promocode
from app.utils.db_api.models.user_model import User


@logger.catch()
@dp.message_handler(is_promocode=True)
async def activate_promocode(message: Message, user: User, lang_code, promocode_obj: Promocode):
    if not promocode_obj.is_active:
        await message.answer(
            text=text[lang_code].message.default.promocode_not_active.format(
                promocode=promocode_obj.code,
                promocode_time=promocode_obj.premium_timedelta,
            )
        )
        return False
    await promocode_obj.update_data(is_active=False, user_id=user.id)
    await user.increase_premium_time(promocode_obj.premium_timedelta)
    await message.answer(
        text=text[lang_code].message.default.promocode_activated.format(
            premium_time=promocode_obj.premium_timedelta,
        )
    )
