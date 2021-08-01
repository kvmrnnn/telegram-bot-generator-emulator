from aiogram.types import Message
from loguru import logger

from app.data import text
from app.data.types.card import CardType
from app.data.types.emulator import EmulatorMagnit, Emulator5ka
from app.filters.private.message.start_link import StartLink
from app.loader import dp


@dp.message_handler(StartLink('ge'))
async def send_emulator(message: Message, message_args: dict, lang_code):
    emulator_type = message_args.get('et')
    emulator_code = message_args.get('ec')
    try:
        if emulator_type == CardType.MAGNIT:
            emulator = EmulatorMagnit(emulator_code)
        elif emulator_type == CardType.PYATEROCHKA:
            emulator = Emulator5ka(emulator_code)
        else:
            return await message.answer(
                text=text[lang_code].message.default.error_generate_emulator
            )
    except Exception:
        return await message.answer(
            text=text[lang_code].message.default.error_generate_emulator
        )
    await message.answer_photo(
        photo=emulator.input_file,
        caption=emulator_code
    )
