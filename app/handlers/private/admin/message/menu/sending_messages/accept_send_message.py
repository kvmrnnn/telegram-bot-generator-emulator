from aiogram.types import ContentTypes, Message

from app.loader import dp
from app.states.private.sending_messages import SendingMessages


@dp.message_handler(state=SendingMessages.wait_for_message, content_types=ContentTypes.ANY)
async def send_message_to_users(message: Message, lang_code):
    if message.poll:
        pass
