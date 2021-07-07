from aiogram import Dispatcher

from app.data.types.user import UserRole
from app.loader import config
from app.utils import db_api
from app.utils.bot import sending_message
from app.utils.bot.set_commands import set_bot_commands


async def on_startup(dp: Dispatcher):
    await db_api.on_startup(drop_all=False)

    await set_bot_commands(dp)

    await sending_message.text_message('Бот включен', roles=[UserRole.ADMIN], chats_id=config.bot.admin_id)
