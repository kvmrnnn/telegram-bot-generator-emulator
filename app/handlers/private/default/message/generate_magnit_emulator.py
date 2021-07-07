from asyncio import sleep

from aiogram.types import Message
from aiogram.utils.exceptions import RetryAfter

from app.data import text
from app.data.types.emulator import EmulatorMagnit
from app.filters.private.message.card import MagnitCardFilter
from app.loader import dp
from app.utils.db_api.models.user import User


@dp.message_handler(MagnitCardFilter())
async def send_magnit_emulator(message: Message, user: User, lang_code: str, cards_data: dict):
    i = 1
    for code, raw_data in cards_data.items():
        emulator_file = EmulatorMagnit(code)
        await sleep(1)
        try:
            await message.answer_photo(emulator_file.input_file, f'{code, i}')
        except RetryAfter:
            await sleep(3)
            await message.answer_photo(emulator_file.input_file, f'{code, i}')
        except Exception:
            await message.answer(text[lang_code].message.default.error_send_emulator)
        finally:
            i+=1