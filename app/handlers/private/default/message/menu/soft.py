from aiogram.types import Message

from app import keyboards
from app.data import text
from app.loader import dp, config
from app.utils.db_api.models.user_model import User


@dp.message_handler(
    user_is_premium=True,
    text=text[config.bot.default_lang].button.default.reply.menu_soft)
@dp.message_handler(
    user_is_premium=True,
    text=text[config.bot.second_lang].button.default.reply.menu_soft)
async def send_soft(message: Message, user: User, lang_code):
    await message.answer(
        text=text[lang_code].message.default.menu_soft_choice_category,
        reply_markup=keyboards.default.inline.menu_soft.choice_category.keyboard(lang_code)
    )


@dp.message_handler(
    text=text[config.bot.default_lang].button.default.reply.menu_soft)
@dp.message_handler(
    text=text[config.bot.second_lang].button.default.reply.menu_soft)
async def send_menu_soft(message: Message, user: User, lang_code):
    await message.answer(
        text=text[lang_code].message.default.buying_a_subscription,
        reply_markup=keyboards.default.inline.subscriptions_prices.keyboard(lang_code)
    )
