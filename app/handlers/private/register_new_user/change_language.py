from aiogram.types import Message, ContentTypes

from app import dp
from app.data import text
from app.filters.private.user.is_read_rules import NotReadRules
from app.keyboards.default import reply
from app.loader import config, links
from app.states.private.registration_new_user import RegistrationNewUser
from app.utils.format_data.user import format_lang_code
from app.utils.misc import inline_generator_button_url


@dp.message_handler(NotReadRules(), content_types=ContentTypes.ANY)
@dp.message_handler(state=RegistrationNewUser.choice_language)
async def message_on(message: Message, user, user_lang):
    if message.text == format_lang_code(config.bot.default_lang):
        await user.update_data(lang=config.bot.default_lang)
    elif message.text == format_lang_code(config.bot.second_lang):
        await user.update_data(lang=config.bot.second_lang)

    await message.answer_video(
        video=links.video.read_rules,
        caption=text[user.lang].message.default.please_read_the_rules,
        reply_markup=reply.agree_rules.keyboard(user.lang)
    )
    links_data = {
        text[user.lang].button.default.inline.bot_rules: links.telegraph.bot_rules,
    }
    await message.answer(
        text=text[user.lang].message.default.links_to_rules,
        reply_markup=inline_generator_button_url.keyboard(links_data)
    )
    await RegistrationNewUser.agree_rules.set()
