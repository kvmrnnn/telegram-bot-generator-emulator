from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.handler import SkipHandler
from aiogram.types import Message

from app import dp
from app.data import text
from app.loader import config
from app.states.private.registration_new_user import RegistrationNewUser


@dp.message_handler(state=RegistrationNewUser.agree_rules,
                    text=text[config.bot.default_lang].button.default.reply.agree_rules)
@dp.message_handler(state=RegistrationNewUser.agree_rules,
                    text=text[config.bot.second_lang].button.default.reply.agree_rules)
async def agree_rules(message: Message, state: FSMContext, user, lang_code):
    await state.finish()
    await message.answer(
        text=text[lang_code].message.default.good
    )
    await user.update_data(is_read_rules=True)
    raise SkipHandler()
