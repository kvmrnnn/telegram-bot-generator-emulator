import datetime as dt
from sqlalchemy import BigInteger, Column, Sequence, String, Boolean

from app.utils.db_api.db import BaseModel


class Promocode(BaseModel):
    __tablename__ = 'promocodes_generator'
    id: int = Column(BigInteger, Sequence('promocode_id'))
    code: str = Column(String(36), primary_key=True)
    premium_datetime: str = Column(String(51))
    user_id: int = Column(BigInteger)
    creator_user_id: int = Column(BigInteger)
    is_active: bool = Column(Boolean, default=True)

    @property
    def premium_timedelta(self) -> dt.timedelta:
        days, hours = map(int, self.premium_datetime.split())
        return dt.timedelta(days=days, hours=hours)
