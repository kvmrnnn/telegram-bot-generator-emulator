from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode

from app.utils.misc.config_loader import ConfigLoader

config = ConfigLoader('./.config.ini').get_config()

bot = Bot(
    token=config.bot.token,
    parse_mode=ParseMode.HTML,
)

dp = Dispatcher(
    bot=bot,
    storage=MemoryStorage()
)
