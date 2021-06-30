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

    deep_link: int = Column(BigInteger, default=UserDeepLink.NONE)
    role: str = Column(String(3), default=UserRole.DEFAULT)

    status_rules_read: bool = Column(Boolean, default=False)
    status_blocked: bool = Column(Boolean, default=False)
    reason_for_blocking: str = Column(String(255))

    property
    def url_to_telegram(self) -> str:
        return f"tg://user?id={self.id}"

    def is_role(self, roles: List[str]) -> bool:
        return self.role in roles