from aiogram.types import Message, ContentTypes

from app import dp
from app.data import text
from app.filters.private.user.is_read_rules import NotReadRules
from app.keyboards.default import reply
from app.keyboards.default.inline import generator_button_url
from app.loader import config, links
from app.states.private.registration_new_user import RegistrationNewUser
from app.utils.format_data.user import format_lang_code


@dp.message_handler(NotReadRules(), state='*', content_types=ContentTypes.ANY)
@dp.message_handler(state=RegistrationNewUser.choice_language)
async def message_on(message: Message, user, lang_code):
    if message.text == format_lang_code(config.bot.default_lang):
        await user.update_data(lang_code=config.bot.default_lang)
    elif message.text == format_lang_code(config.bot.second_lang):
        await user.update_data(lang_code=config.bot.second_lang)

    await message.answer_video(
        video=links.video.read_rules,
        caption=text[user.lang_code].message.default.please_read_the_rules,
        reply_markup=reply.agree_rules.keyboard(user.lang_code)
    )

    links_data = {
        text[user.lang_code].button.default.inline.bot_rules: links.telegraph.bot_rules,
    }

    await message.answer(
        text=text[user.lang_code].message.default.links_to_rules,
        reply_markup=generator_button_url.keyboard(links_data)
    )
    await RegistrationNewUser.agree_rules.set()
