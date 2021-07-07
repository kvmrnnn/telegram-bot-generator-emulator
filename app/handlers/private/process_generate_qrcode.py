from typing import Union

from aiogram.types import Message, CallbackQuery

from app.loader import dp
from app.states.private.generate_qrcode import GenerateQRCode

@dp.message_handler(state=GenerateQRCode.process_generate)
@dp.message_handler(state=GenerateQRCode.process_generate)
async def process_generate(obj: Union[Message, CallbackQuery]):
    pass

