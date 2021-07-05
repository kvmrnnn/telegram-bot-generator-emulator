from typing import Union

from aiogram.types import Message, CallbackQuery

from app.data import text
from app.filters.private.message.not_command import NotCommand
from app.filters.private.user.not_subscriber import NotSubscribedChat
from app.loader import dp
from app.utils.misc import inline_generator_button_url


@dp.callback_query_handler(NotSubscribedChat())
@dp.message_handler(NotCommand('start'), NotSubscribedChat(), state='*')
async def not_subscriber(obj: Union[Message, CallbackQuery], user_lang, data_filter):
    await obj.bot.send_message(
        chat_id=obj.from_user.id,
        text=text[user_lang].message.default.subscribe_to_the_chat,
        reply_markup=inline_generator_button_url.keyboard(data_filter)
    )
