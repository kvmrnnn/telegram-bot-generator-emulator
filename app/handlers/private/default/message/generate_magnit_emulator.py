import asyncio
import time

from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentTypes
from aiogram.utils.exceptions import RetryAfter
from loguru import logger

from app.data import text
from app.data.types.emulator import EmulatorMagnit
from app.filters.private.message.card import MagnitCardFilter
from app.loader import dp, config
from app.states.private.generate_qrcode import GenerateQRCode
from app.utils.db_api.db import db
from app.utils.db_api.models.card_model import Card
from app.utils.db_api.models.user_model import User


@dp.message_handler(MagnitCardFilter())
@dp.message_handler(MagnitCardFilter(), content_types=ContentTypes.DOCUMENT)
async def send_magnit_emulator(message: Message, state: FSMContext, user: User, lang_code: str, cards_data: dict):
    generate_limit = user.generate_limit or config.bot.generate_limit_default
    count_generated_by_the_user_this_day = await db.scalar(db.func.count(Card.user_id))
    count_free_generate = generate_limit - count_generated_by_the_user_this_day

    if len(cards_data) > generate_limit:
        await message.answer(
            text=text[lang_code].message.default.generation_limit_exceeded.format(
                max_count=generate_limit,
                user_count=len(cards_data)
            )
        )
        return False

    if not user.is_premium and not (count_free_generate > 0):
        await message.answer(
            text=text[lang_code].message.default.generation_limit_exceeded_this_day
        )
        return False

    if not user.is_premium and len(cards_data) > count_free_generate:
        cards_data_tmp = cards_data.copy()
        cards_data.clear()
        for card, raw_data in list(cards_data_tmp.items())[:count_free_generate]:
            cards_data.setdefault(card, raw_data)

    await GenerateQRCode.process_generate.set()

    i = 1
    try:
        for code, raw_data in cards_data.items():
            await Card.insert(
                code=str(code),
                raw_data=raw_data,
                user_id=user.id
            )
            await asyncio.sleep(0.5)
            emulator_file = EmulatorMagnit(code)
            try:
                await message.answer_photo(emulator_file.input_file, f'{code} {i}')
            except RetryAfter as err:
                logger.debug(f"Спим {err.timeout} секунд")
                time.sleep(err.timeout + 1)
                await message.answer_photo(emulator_file.input_file, f'{code} {i}')
            except Exception:
                await message.answer(text[lang_code].message.default.error_send_emulator)
            finally:
                i += 1
    except Exception as ex:
        logger.debug(ex)
    finally:
        await state.finish()
