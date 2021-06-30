import datetime

from gino import Gino
from loguru import logger
from sqlalchemy import Column, DateTime
from sqlalchemy.orm import Query
from sqlalchemy.sql.elements import or_, and_
db = Gino()

class BaseModel(db.Model):
    __abstract__ = True
    __tablename__: str
    query: Query

    create_at: datetime.datetime = Column(DateTime, server_default=db.func.now())
    update_at: datetime.datetime = Column(DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    async def update_data(self, **kwargs):
        """
        Обновляет данные полей таблицы в базе данных
        :param kwargs: Поля в таблице и новое значение
        :return:
        """
        await self.update(**kwargs).apply()
        logger.success(f"{self.__tablename__} (id: {self.id}) set new param {kwargs}")

    def qf(self, op: str = 'and', **kwargs):
        """
        Query filter
        :param op:
        :param kwargs:
        :return:
        """
        conditions = []
        for key, value in kwargs.items():
            try:
                column: Column = getattr(self, key)
                if 'int' in str(column.type).lower():
                    conditions.append(column == int(value))
                elif 'float' in str(column.type).lower():
                    conditions.append(column == float(value))
                else:
                    conditions.append(column == value)
            except Exception as ex:
                continue

        if op == 'or':
            return or_(*conditions)
        if op == 'and':
            return or_(*conditions)
