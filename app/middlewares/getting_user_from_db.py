from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from app.utils.db_api.models.user import User


class GettingUserFromDataBase(BaseMiddleware):
    async def on_pre_process_message(self, message: Message, data: dict):
        user_id = message.from_user.id
        user = await User.get(id=user_id)
        if user is not None:
            await user.update_username(message.from_user.username)
            await user.update_full_name(message.from_user.full_name)
        data['user'] = user

    async def on_pre_process_callback_query(self, call: CallbackQuery, data: dict):
        user_id = call.from_user.id
        user = await User.get(id=user_id)
        if user is not None:
            await user.update_username(call.from_user.username)
            await user.update_full_name(call.from_user.full_name)
        data['user'] = user
