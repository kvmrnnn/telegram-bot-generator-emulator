from aiogram.types import ContentTypes, Message

from app.data import text
from app.loader import dp, config
from app.utils.db_api.models.user_model import User


@dp.message_handler(text=text[config.bot.default_lang].button.admin.reply.menu_sending_messages)
@dp.message_handler(text=text[config.bot.second_lang].button.admin.reply.menu_sending_messages)
async def request_a_message(message: Message, user: User, lang_code):
    pass