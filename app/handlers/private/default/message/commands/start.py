from asyncio import sleep

from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message

from app import keyboards
from app.data import text
from app.data.types.user import UserDeepLink
from app.filters.private.user import NewUser
from app.loader import dp, links
from app.states.private.registration_new_user import RegistrationUser
from app.utils.db_api.models.user import User
from app.utils.format_data.user import format_fullname


@dp.message_handler(CommandStart(), NewUser())
async def message_on(message: Message):

    # deep link
    try:
        deep_link = int(message.get_args())
    except:
        deep_link = UserDeepLink.NONE


    user = User(
        id=message.from_user.id,
        fullname=message.from_user.full_name,
        lang=message.from_user.language_code,
        username=message.from_user.username,
        deep_link=deep_link,
    )

    # Add new user in database
    await user.create()

    await message.answer_video(
        video=links.video.read_rules,
        caption=text.message.default.start.format(
            user_fullname=format_fullname(user.fullname)
        ),
        reply_markup=keyboards.default.reply.agree_rules.keyboard
    )

    links_data = {
        'Правила для ознакомления': 'https://telegra.ph/Programma-dlya-raboty-s-kartami-MgiT-05-12',
    }
    await message.answer(
        text='Правила',
        reply_markup=keyboards.default.inline.generator_url_btn.keyboard(links_data)
    )
    await RegistrationUser.agree_rules.set()
