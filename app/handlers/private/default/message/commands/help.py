from aiogram.dispatcher.filters import CommandHelp
from aiogram.types import Message

from app.data import text
from app.loader import dp


@dp.message_handler(CommandHelp())
async def message_on(message: Message, user_lang):
    await message.answer(
        text=text[user_lang].message.default.command_help
    )
