from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.data import text
from app.data.types.user import UserRole
from app.loader import dp, config
from app.utils.bot import send_main_keyboard
from app.utils.db_api.models.promocode_model import Promocode


@dp.message_handler(user_role=UserRole.ADMIN, text=text[config.bot.default_lang].button.admin.reply.delete_all_proms)
@dp.message_handler(user_role=UserRole.ADMIN, text=text[config.bot.second_lang].button.admin.reply.delete_all_proms)
async def delete_all_promo_codes(message: Message, state: FSMContext, user, lang_code):
    await send_main_keyboard(user, state)
    active_promocodes = await Promocode.query.where(Promocode.qf(is_active=True)).gino.all()
    for promo_code in active_promocodes:
        await promo_code.update_data(is_active=False)
    await message.answer(
        text=text[lang_code].message.admin.all_proms_deleted
    )
