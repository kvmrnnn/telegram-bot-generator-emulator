from aiogram.types import Message

from app.data import text
from app.data.types.user import UserRole
from app.loader import dp, config
from app.states.private.delete_promo_code import DeletePromoCode


@dp.message_handler(user_role=UserRole.ADMIN, text=text[config.bot.default_lang].button.admin.reply.delete_prom_by_code)
@dp.message_handler(user_role=UserRole.ADMIN, text=text[config.bot.second_lang].button.admin.reply.delete_prom_by_code)
async def set_prom_code(message: Message, lang_code):
    await message.answer(
        text=text[lang_code].message.admin.wait_for_prom_code
    )
    await DeletePromoCode.wait_for_code.set()
