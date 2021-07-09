from aiogram.types import Message

from app.data import text
from app.loader import dp, config
from app.utils.db_api.models.promocode_model import Promocode


@dp.message_handler(text=text[config.bot.default_lang].button.admin.reply.delete_all_proms)
@dp.message_handler(text=text[config.bot.second_lang].button.admin.reply.delete_all_proms)
async def delete_all_promo_codes(message: Message):
    active_promocodes = await Promocode.query.where(is_active=True).gino.all()
