from aiogram import Dispatcher
from aiogram.dispatcher.handler import current_handler, CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, User
from aiogram.utils.exceptions import Throttled

from app.data import text
from app.loader import config


class AntiFloodMiddleware(BaseMiddleware):
    async def on_process_message(self, message: Message, data: dict):
        handler = current_handler.get()
        dispatcher = Dispatcher.get_current()
        if handler and getattr(handler, 'no_limit', False):
            return False
        try:
            await dispatcher.throttle('key', rate=1.5)
        except Throttled as throttled:
            if await self.is_throttled(message, throttled):
                raise CancelHandler()

    async def is_throttled(self, message: Message, throttled: Throttled):
        if throttled.exceeded_count < 5:
            return False
        elif throttled.exceeded_count < 8:
            await message.answer(text=text[self.lang_code].message.default.antiflood_warning)
            return False
        elif throttled.exceeded_count == 8:
            await message.reply(text=text[self.lang_code].message.default.antiflood_mute)
            return True
        else:
            return True

    @property
    def lang_code(self):
        user = User.get_current()
        if user.language_code == config.bot.default_lang or user.language_code == config.bot.second_lang:
            return user.language_code
        return config.bot.default_lang
