from aiogram.types import Message
from loguru import logger

from app.data import text
from app.loader import dp, config, links
from app.utils.db_api.models.user_model import User
from app.utils.format_data.user import format_username, format_premium_to_up


@dp.message_handler(text=text[config.bot.default_lang].button.default.reply.profile)
@dp.message_handler(text=text[config.bot.second_lang].button.default.reply.profile)
async def send_menu_profile(message: Message, user: User, lang_code):
    bot_data = await dp.bot.get_me()
    user_photos = (await message.from_user.get_profile_photos()).photos
    if user_photos:
        user_photo = user_photos[0][-1].file_id
    else:
        user_photo = links.photo.no_avatars

    await message.answer_photo(
        photo=user_photo,
        caption=text[lang_code].message.default.profile.format(
            user_id=user.id,
            user_username=format_username(user.username),
            bot_username=bot_data.username,
            user_balance=user.balance,
            user_premium_to_up=format_premium_to_up(user.premium_up_to, lang_code),
        )
    )
