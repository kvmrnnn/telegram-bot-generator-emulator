from aiogram.types import Message

from app.data import text
from app.loader import dp
from app.utils.db_api.models.promocode_model import Promocode
from app.utils.db_api.models.user_model import User


@dp.message_handler(is_promocode=True)
async def activate_promocode(message: Message, user: User, code_lang, promocode: Promocode):
    if not promocode.is_active:
        await message.answer(
            text=text[code_lang].message.default.promocode_not_active.format(
                promocode=promocode.code,
                promocode_time=promocode.premium_timedelta,
            )
        )
        return False
    await promocode.update_data(is_active=False, user_id=user.id)
    await user.increase_premium_time(promocode.premium_timedelta)
    await message.answer(
        text=text[code_lang].message.default.promocode_activated.format(
            promocode_time=promocode.premium_timedelta,
        )
    )
