from typing import List, Union

from sqlalchemy import Column, BigInteger, String, Boolean

from app.data.types.user import UserUsername, LangCode, UserRole, UserDeepLink, UserPhone, UserDataHistory
from app.loader import config
from app.utils.db_api.db import BaseModel


class User(BaseModel):
    __tablename__ = 'users_template'

    id: int = Column(BigInteger, primary_key=True)
    fullname: str = Column(String(128))
    phone: str = Column(String(24), default=UserPhone.NONE)
    lang: str = Column(String(10), default=config.bot.default_lang)
    username: str = Column(String(32), default=UserUsername.NONE)
    full_name_history: str = Column(String, default=UserDataHistory.NONE)
    username_history: str = Column(String, default=UserDataHistory.NONE)

    deep_link: int = Column(BigInteger, default=UserDeepLink.NONE)
    role: str = Column(String(20), default=UserRole.DEFAULT)

    is_read_rules: bool = Column(Boolean, default=False)
    is_blocked: bool = Column(Boolean, default=False)
    is_active: bool = Column(Boolean, default=True)
    reason_for_blocking: str = Column(String(255))

    @property
    def url_to_telegram(self) -> str:
        return f"tg://user?id={self.id}"

    def is_role(self, roles: Union[str, List[str]]) -> bool:
        if isinstance(roles, list):
            return self.role in roles
        return self.role == roles

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
        self.username_history += self.username + '\n'
        await self.update_data(username_history=self.username_history)
        await self.update_data(username=username)

