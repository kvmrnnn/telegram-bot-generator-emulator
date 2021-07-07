from datetime import datetime as dt
from typing import List, Union

from sqlalchemy import Column, BigInteger, String, Boolean, DateTime

from app.data.types.user import UserRole, UserDeepLink, UserPhone, UserDataHistory
from app.loader import config
from app.utils.db_api.db import BaseModel


class User(BaseModel):
    __tablename__ = 'users_generator'

    id: int = Column(BigInteger, primary_key=True)
    username: str = Column(String(32))
    fullname: str = Column(String(128))
    lang_code: str = Column(String(10), default=config.bot.default_lang)
    deep_link: int = Column(BigInteger, default=UserDeepLink.NONE)

    phone: str = Column(String(24), default=UserPhone.NONE)

    role: str = Column(String(20), default=UserRole.DEFAULT)

    username_history: str = Column(String, default=UserDataHistory.NONE)
    full_name_history: str = Column(String, default=UserDataHistory.NONE)

    is_read_rules: bool = Column(Boolean, default=False)
    is_blocked: bool = Column(Boolean, default=False)
    is_active: bool = Column(Boolean, default=True)
    reason_for_blocking: str = Column(String(255))

    online_at: dt = Column(DateTime, default=dt.utcnow())

    premium_up_to: dt = Column(DateTime, default=dt.utcnow())

    generate_limit: int = Column(BigInteger, default=0)

    @property
    def is_premium(self):
        return self.premium_up_to > dt.utcnow()

    @property
    def url_to_telegram(self) -> str:
        return f"tg://user?id={self.id}"

    def is_role(self, roles: Union[str, List[str]]) -> bool:
        if isinstance(roles, list):
            return self.role in roles
        return self.role == roles

    async def change_premium_time(self, datetime: dt) -> None:
        """
        Changes the premium time.
        Args:
            datetime: Time to change premium.

        Returns:
            None

        """
        if self.premium_up_to + datetime < dt.utcnow():
            await self.update_data(premium_up_to=dt.utcnow() + datetime)
        else:
            await self.update_data(premium_up_to=self.premium_up_to + datetime)

    def get_username_history(self) -> list:
        return self.username_history.rstrip().splitlines()

    def get_full_name_history(self) -> list:
        return self.full_name_history.rstrip().splitlines()

    async def update_full_name(self, full_name):
        if self.fullname == full_name:
            return False
        self.full_name_history += full_name + '\n'
        await self.update_data(full_name_history=self.full_name_history)
        await self.update_data(full_name=full_name)

    async def update_username(self, username):
        if self.username == username:
            return False

        self.username_history += str(self.username) + '\n'
        await self.update_data(username_history=self.username_history)
        await self.update_data(username=username)
