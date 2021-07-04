from loguru import logger

from app.loader import config
from aiogram import Dispatcher
from aiogram.types import BotCommand


async def set_bot_commands(dp: Dispatcher, commands: dict = config.bot.commands):
    logger.info(f'Bot: Setting my commands {commands}')

    if commands is None:
        await dp.bot.set_my_commands([])
        return

    await dp.bot.set_my_commands(
        [
            BotCommand(command, description) for command, description in config.bot.commands.items()
        ]
    )
