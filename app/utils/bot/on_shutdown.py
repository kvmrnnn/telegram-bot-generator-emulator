from aiogram import Dispatcher

from app.utils.db_api.db import db


async def on_shutdown(dp: Dispatcher):
    # Отключение от базы данных.
    await db.pop_bind().close()
