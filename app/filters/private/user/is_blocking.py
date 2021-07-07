from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message, CallbackQuery, InlineQuery

from app.utils.db_api.models.user_model import User


class UserBlocked(BoundFilter):

    async def check(self, obj: [Message, CallbackQuery, InlineQuery]) -> bool:
        user = User.get(obj.from_user.id)
        if user is None:
            return False
        return not user.is_blocked
