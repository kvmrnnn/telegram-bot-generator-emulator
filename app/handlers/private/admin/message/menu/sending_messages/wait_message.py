from aiogram.types import Message

from app.data import text
from app.loader import dp, config
from app.states.private.sending_messages import SendingMessages
from app.utils.db_api.models.user_model import User


@dp.message_handler(text=text[config.bot.default_lang].button.admin.reply.sending_messages)
@dp.message_handler(text=text[config.bot.second_lang].button.admin.reply.sending_messages)
async def request_a_message(message: Message, user: User, lang_code):
    await message.answer(
        text=text[lang_code].message.admin.request_message
    )
    await SendingMessages.wait_for_message.set()
