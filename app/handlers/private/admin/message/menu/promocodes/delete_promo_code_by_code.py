import os
from io import BufferedWriter

from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentTypes
from loguru import logger

from app.data import text
from app.loader import dp
from app.states.private.delete_promo_code import DeletePromoCode
from app.utils.bot import send_main_keyboard
from app.utils.db_api.models.promocode_model import Promocode
from app.utils.format_data.promocodes import format_promo_code


@dp.message_handler(state=DeletePromoCode.wait_for_code, content_types=ContentTypes.ANY)
async def delete_promocode_by_code(message: Message, state: FSMContext, user, lang_code):
    logger.debug(f" is doc {bool(message.document)}")
    if message.text:
        promocodes_data = message.text.splitlines()

    elif message.document:
        file_doc: BufferedWriter = await message.document.download('./app/data/tmp')
        file_doc.close()
        with open(file_doc.name, encoding='UTF-8') as file:
            promocodes_data = file.read().splitlines()
        os.remove(file_doc.name)
    else:
        await message.answer(
            text='Wrong data'
        )
    logger.debug(promocodes_data)
    await send_main_keyboard(user, state)

    for data in promocodes_data:
        promocode = format_promo_code(data)
        if promocode and await Promocode.get(promocode):
            promo_code = await Promocode.get(promocode)
            await promo_code.update_data(is_active=False)

    await message.answer(
        text=text[lang_code].message.admin.proms_are_removed
    )
