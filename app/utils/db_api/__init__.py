from loguru import logger

from app.loader import config
from app.utils.db_api.db import db


async def on_startup(drop_all: bool = False):
    # Подключение к базе данных.

    logger.info('Db: Connect to db')
    await db.set_bind(bind=config.database.url)

    if drop_all:
        logger.warning('Db: Drop all')
        await db.gino.drop_all()

    # Создание таблиц.
    logger.info('Db: Create all')
    await db.gino.create_all()
