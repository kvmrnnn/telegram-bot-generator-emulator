from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message, CallbackQuery, InlineQuery
from loguru import logger

from app.loader import config
from app.utils.db_api.models.user import User


class UserRoleFilter(BoundFilter):

    key = 'user_role'

    def __init__(self, user_role: list[str]):
        if isinstance(user_role, list):
            self.roles = list(set(user_role))
        elif isinstance(user_role, str):
            self.roles = [user_role]

    async def check(self, obj: [Message, CallbackQuery, InlineQuery]) -> bool:
        user_id = obj.from_user.id
        user = await User.get(user_id)
        if user is None:
            return user_id == config.bot.admin_id

        return user.is_role(self.roles)
