from sqlalchemy import Column, BigInteger, Sequence, String

from app.data.types.card import CardType
from app.utils.db_api.db import BaseModel


class Card(BaseModel):
    __tablename__ = 'cards'

    id: int = Column(BigInteger, Sequence('card_id'), primary_key=True)
    type: str = Column(String(10))
    code: str = Column(String(16))
    raw_data: str = Column(String)
    user_id: int = Column(BigInteger)
