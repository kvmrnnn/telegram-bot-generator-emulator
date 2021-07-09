from aiogram.types import Message

from app.data import text
from app.loader import dp, config
from app.utils.db_api import db
from app.utils.db_api.models.card_model import Card
from app.utils.db_api.models.user_model import User


@dp.message_handler(text=text[config.bot.default_lang].button.default.reply.information)
@dp.message_handler(text=text[config.bot.second_lang].button.default.reply.information)
async def send_information(message: Message, user: User, lang_code):
    await message.answer(
        text=text[lang_code].message.default.information.format(
            count_emulators=await db.scalar(
                db.select([db.func.count(Card.id)])
            )
        ),
    )