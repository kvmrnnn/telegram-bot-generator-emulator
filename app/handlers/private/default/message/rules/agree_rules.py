from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from app.data import text
from app.loader import dp
from app.states.private.registration_new_user import RegistrationUser


@dp.message_handler(text=text.button.default.reply.agree_rules, state=RegistrationUser.agree_rules)
async def agree_rules(message: Message, state: FSMContext, user):
    await message.answer('Отлично!', reply_markup=ReplyKeyboardRemove())
    await user.update_data(is_read_rules=True)
    await state.finish()