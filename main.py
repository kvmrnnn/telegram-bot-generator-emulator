from aiogram.utils import executor

from app import dp
from app.data.types.emulator import Emulator5ka, EmulatorMagnit
from app.data.types.qrcode import QRCode5ka
from app.utils.bot import on_startup, on_shutdown


def main():
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
    # xxx = Emulator5ka('1234567890123456')


if __name__ == '__main__':
    main()
