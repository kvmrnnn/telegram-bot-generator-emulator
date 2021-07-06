from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from app.loader import config
from app.utils.db_api.models.user import User


class GettingUserFromDataBaseMiddleware(BaseMiddleware):
    async def on_process_message(self, message: Message, data: dict):
        user_id = message.from_user.id
        user = await User.get(user_id)
        lang_code = config.bot.default_lang
        if user:
            lang_code = user.lang_code
            await user.update_username(message.from_user.username)
            await user.update_full_name(message.from_user.full_name)

        data['user'] = user
        data['lang_code'] = lang_code

    async def on_process_callback_query(self, call: CallbackQuery, data: dict):
        user_id = call.from_user.id
        user = await User.get(user_id)
        lang_code = config.bot.default_lang
        if user:
            lang_code = user.lang_code
            await user.update_username(call.from_user.username)
            await user.update_full_name(call.from_user.full_name)

        data['user'] = user
        data['lang_code'] = lang_code
