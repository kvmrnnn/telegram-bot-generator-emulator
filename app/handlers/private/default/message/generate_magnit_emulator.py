import asyncio
import time

from aiogram.types import Message, ContentTypes
from aiogram.utils.exceptions import RetryAfter
from loguru import logger

from app.data import text
from app.data.types.emulator import EmulatorMagnit
from app.filters.private.message.card import MagnitCardFilter
from app.loader import dp
from app.utils.db_api.models.user import User


@dp.message_handler(MagnitCardFilter(), content_types=ContentTypes.DOCUMENT)
async def send_magnit_emulator(message: Message, user: User, lang_code: str, cards_data: dict):
    i = 1
    for code, raw_data in cards_data.items():
        await asyncio.sleep(0.5)
        emulator_file = EmulatorMagnit(code)
        try:
            await message.answer_photo(emulator_file.input_file, f'{code, i}')
        except RetryAfter as err:
            logger.debug(f"Спим {err.timeout} секунд")
            time.sleep(err.timeout+1)
            await message.answer_photo(emulator_file.input_file, f'{code, i}')
        except Exception:
            await message.answer(text[lang_code].message.default.error_send_emulator)
        finally:
            i += 1
