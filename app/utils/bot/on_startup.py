from aiogram import Dispatcher

from app.loader import config
from app.utils.db_api.db import db


async def on_startup(dp: Dispatcher):
    # Подключение к базе данных.
    await db.set_bind(config.database.url)

    # При коммите комментировать! Иначе все данные в таблицах сотрутся.
    await db.gino.drop_all()
    # Создание таблиц.
    await db.gino.create_all()
