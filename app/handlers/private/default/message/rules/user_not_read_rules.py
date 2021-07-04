from aiogram.types import Message

from app import keyboards
from app.filters.private.message.not_command import NotCommand
from app.filters.private.user.is_read_rules import NotReadRules
from app.loader import dp
from app.states.private.registration_new_user import RegistrationUser


@dp.message_handler(NotReadRules(), NotCommand('start'))
async def not_read_rules(message: Message, user):
    await message.answer(
        text='Ознакомьтесь с нашими правилами использования бота',
        reply_markup=keyboards.default.reply.agree_rules.keyboard
    )
    links = {
        'Правила для ознакомления': 'https://telegra.ph/Programma-dlya-raboty-s-kartami-MgiT-05-12',
    }
    await message.answer(
        text='Правила',
        reply_markup=keyboards.default.inline.generator_url_btn.keyboard(links)
    )
    await RegistrationUser.agree_rules.set()
