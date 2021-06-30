from typing import List

from sqlalchemy import Column, BigInteger, String, Boolean

from app.data.types.user import UserUsername, UserLang, UserRole, UserDeepLink
from app.utils.db_api.db import BaseModel


class User(BaseModel):
    id: int = Column(BigInteger, primary_key=True)
    full_name: str = Column(String(128))
    phone: str = Column(String(24))
    lang: str = Column(String(10), default=UserLang.RUS)
    username: str = Column(String(32), default=UserUsername.NONE)
    full_name_history: str = Column(String)
    username_history: str = Column(String, default=UserUsername.NONE)

    deep_link: int = Column(BigInteger, default=UserDeepLink.NONE)
    role: str = Column(String(3), default=UserRole.DEFAULT)

    status_rules_read: bool = Column(Boolean, default=False)
    status_blocked: bool = Column(Boolean, default=False)
    reason_for_blocking: str = Column(String(255))

    @property
    def url_to_telegram(self) -> str:
        return f"tg://user?id={self.id}"

    def is_role(self, roles: List[str]) -> bool:
        return self.role in roles

    async def update_username(self, username):
        if self.username == username:
            return False
        self.username_history += self.username + ' '
        await self.update_data(username_history=self.username_history)
        await self.update_data(username=username)

    def get_username_history(self) -> list:
        return self.username_history.rstrip().split()

    async def update_full_name(self, full_name):
        if self.full_name == full_name:
            return False
        self.full_name_history += full_name + ' '
        await self.update_data(full_name_history=self.full_name_history)
        await self.update_data(full_name=full_name)

    def get_full_name_history(self) -> list:
        return self.full_name_history.rstrip().split()
