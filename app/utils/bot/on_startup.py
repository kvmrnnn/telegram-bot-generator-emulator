from aiogram import Dispatcher

from app.data.types.user import UserRole
from app.utils import db_api
from app.utils.bot import sending_message
from app.utils.bot.set_commands import set_bot_commands
from app.loader import config

async def on_startup(dp: Dispatcher):

    await db_api.on_startup(1)

    await set_bot_commands(dp)

    await sending_message.text('Бот включен', [UserRole.ADMIN], config.bot.admin_id)
    

