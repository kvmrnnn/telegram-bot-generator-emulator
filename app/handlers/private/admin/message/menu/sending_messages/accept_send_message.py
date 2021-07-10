from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes, Message

from app.data import text
from app.loader import dp
from app.states.private.sending_messages import SendingMessages
from app.utils.bot import send_main_keyboard
from app.utils.bot.sending_message import copy_message, forward_message


@dp.message_handler(state=SendingMessages.wait_for_message, content_types=ContentTypes.POLL)
async def send_message_to_users(message: Message, state: FSMContext, user, lang_code):
    await forward_message(message=message)
    await message.answer(
        text=text[lang_code].message.admin.poll_was_sent_to_users
    )
    await send_main_keyboard(user, state)


@dp.message_handler(state=SendingMessages.wait_for_message, content_types=ContentTypes.ANY)
async def send_message_to_users(message: Message, state: FSMContext, user, lang_code):
    await copy_message(message=message)
    await message.answer(
        text=text[lang_code].message.admin.message_copy_was_sent_to_users
    )
    await send_main_keyboard(user, state)
