import datetime as dt
from sqlalchemy import BigInteger, Column, Sequence, String, Boolean

from app.utils.db_api.db import BaseModel


class Promocode(BaseModel):
    id: int = Column(BigInteger, Sequence('promocode_id'), primary_key=True)
    code: str = Column(String(36), primary_key=True)
    premium_datetime: str = Column(String(51))
    user_id: int = Column(BigInteger)
    creator_user_id: int = Column(BigInteger)
    is_active: bool = Column(Boolean)

    @property
    def premium_timedelta(self) -> dt.timedelta:
        days, hours = map(int, self.premium_datetime)
        return dt.timedelta(days=days, hours=hours)
