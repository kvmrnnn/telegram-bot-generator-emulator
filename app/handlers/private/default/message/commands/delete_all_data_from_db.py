from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from app.loader import dp
from app.utils.db_api.models.user import User


@dp.message_handler(Command('delete_user_data_from_db'))
async def delete_user_data_from_db(message: Message, user: User):
    await user.delete()
    await message.answer('Данные о вас успешно удалены')
