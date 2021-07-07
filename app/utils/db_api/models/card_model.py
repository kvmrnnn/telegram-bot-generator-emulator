from sqlalchemy import Column, BigInteger, Sequence, String

from app.utils.db_api.db import BaseModel


class Card(BaseModel):
    __tablename__ = 'cards'

    id: int = Column(BigInteger, Sequence('card_id'), primary_key=True)
    code: str = Column(String(16))
    raw_data: str = Column(String)
    user_id: int = Column(BigInteger)
