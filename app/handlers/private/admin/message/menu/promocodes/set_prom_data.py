from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.data import text
from app.data.types.user import UserRole
from app.loader import dp, config
from app.states.private.create_promo_code import CreatePromoCode


@dp.message_handler(user_role=UserRole.ADMIN, text=text[config.bot.default_lang].button.admin.reply.create_promocode)
@dp.message_handler(user_role=UserRole.ADMIN, text=text[config.bot.second_lang].button.admin.reply.create_promocode)
async def create_promo_code(message: Message, lang_code, state: FSMContext):
    await message.answer(
        text=text[lang_code].message.admin.create_prom_enter_data
    )
    await CreatePromoCode.wait_for_data.set()
