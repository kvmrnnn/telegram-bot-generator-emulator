import os
from datetime import datetime

from aiogram.types import InputFile
from openpyxl import Workbook


class BaseTmpFile:
    __path_to_dir_tmp = './app/data/tmp'

    def __init__(self, filename=None, extension=None):
        self.filename = self._format_filename(filename)
        self.extension = extension or 'xlsx'
        self.path_to_file = f'{self.__path_to_dir_tmp}/{self.filename}.{self.extension}'

        with open(self.path_to_file, 'w+') as file:
            pass

    @property
    def input_file(self) -> InputFile:
        return InputFile(self.path_to_file, self.filename)

    def _format_filename(self, filename):
        if not filename:
            return str(datetime.utcnow()).replace(".", ":").replace(" ", "_")
        return filename.replace(".", ":").replace(" ", "_")

    def __del__(self):
        os.remove(self.path_to_file)


class ExсelFile(BaseTmpFile):

    def __init__(self, filename=None, extension=None):
        super().__init__()
        self.data: dict
        self.book = Workbook()
        self.sheet = self.book.active

    def _set_columns_name(self, data: dict):
        pass

    def write_data(self, **data):
        self.book.save(self.path_to_file)

    def __del__(self):
        self.book.close()
        os.remove(self.path_to_file)
