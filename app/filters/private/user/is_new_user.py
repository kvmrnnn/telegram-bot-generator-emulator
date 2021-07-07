from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message, CallbackQuery, InlineQuery

from app.utils.db_api.models.user_model import User


class NewUser(BoundFilter):

    async def check(self, obj: [Message, CallbackQuery, InlineQuery]) -> bool:
        user = await User.get(obj.from_user.id)

        return user is None
