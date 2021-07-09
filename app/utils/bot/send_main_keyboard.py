from aiogram import Bot
from aiogram.dispatcher import FSMContext

from app import keyboards
from app.data import text
from app.data.types.user import UserRole
from app.loader import config
from app.utils.db_api.models.user_model import User


async def send_main_keyboard(user: User, state: FSMContext = None):
    """
    Send main keyboard depending on his role.
    Args:
        user: Object User from table users.
        state: User state to finished.

    Returns:
        None

    """
    if state:
        await state.finish()

    bot = Bot.get_current()

    if user.is_role(UserRole.ADMIN) or user.id == config.bot.admin_id:
        keyboard = keyboards.admin.reply.main.keyboard(user.lang_code)
        await user.update_data(role=UserRole.ADMIN)
    else:
        keyboard = keyboards.default.reply.main.keyboard(user.lang_code)

    await bot.send_message(
        chat_id=user.id,
        text=text[user.lang_code].message.default.send_main_keyboard,
        reply_markup=keyboard
    )
