from aiogram.utils import executor

from app import dp
from app.utils.bot import on_startup, on_shutdown


def main():
    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=on_startup)

if __name__ == '__main__':
    main()
