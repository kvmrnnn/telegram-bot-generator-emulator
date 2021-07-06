from aiogram.utils import executor

from app import dp
from app.data.types.tmp_files import ExсelFile
from app.utils.bot import on_startup, on_shutdown


def main():
    excel_file = ExсelFile()
    excel_file.write_data(user_id=12, balance=0, is_banned=True)
    # executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)


if __name__ == '__main__':
    main()
