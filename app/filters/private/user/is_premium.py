from typing import Union

from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message, CallbackQuery
from loguru import logger

from app.data.types.user import UserRole
from app.utils.db_api.models.user_model import User


class IsPremiumFilter(BoundFilter):
    key = 'user_is_premium'

    def __init__(self, user_is_premium: bool = True):
        self.flag = user_is_premium

    async def check(self, obj: Union[Message, CallbackQuery]) -> bool:
        if not self.flag:
            return False
        user_id = obj.from_user.id
        user = await User.get(user_id)
        if not user:
            return False
        return user.is_premium or user.is_role(UserRole.ADMIN)