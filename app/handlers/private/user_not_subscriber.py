from typing import Union

from aiogram.types import Message, CallbackQuery

from app import keyboards
from app.filters.private.message.not_command import NotCommand
from app.filters.private.user.not_subscriber import NotSubscribedChat
from app.loader import dp


@dp.callback_query_handler(NotSubscribedChat())
@dp.message_handler(NotCommand('start'), NotSubscribedChat())
async def not_subscriber(obj: Union[Message, CallbackQuery], data_filter):
    await obj.bot.send_message(
        chat_id=obj.from_user.id,
        text='Чтобы нас не потерять, подпишитесь на наш канал',
        reply_markup=keyboards.default.inline.generator_url_btn.keyboard(data_filter)
    )