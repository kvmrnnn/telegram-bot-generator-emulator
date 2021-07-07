from abc import abstractmethod

import qrcode
from loguru import logger
from qrcode import constants

from app.data.types.tmp_files import PhotoFile


class QRCodeBase(PhotoFile):

    def __init__(self, data):
        self.data = self.format_data(data)
        super().__init__()
        self.generate_qrcode()


    def generate_qrcode(self):
        raise ValueError('This is an abstract method')

    def format_data(self, data) -> str:
        raise ValueError('This is an abstract method')


class QRCodeMagnit(QRCodeBase):
    def __init__(self, data):
        data = self.format_data(data)
        super().__init__(data)

    def generate_qrcode(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=constants.ERROR_CORRECT_M,
            box_size=20,
            border=2
        )
        qr.add_data(self.data)
        image = qr.make_image()
        image.save(self.path_to_file)

    def format_data(self, data) -> str:
        data = str(data).replace(' ', '')
        if len(data) != 16:
            raise ValueError('Invalid data')
        return data


class QRCode5ka(QRCodeBase):
    def __init__(self, data):
        super(QRCodeBase, self).__init__(data)

    def generate_qrcode(self):
        img = self.path_to_file

    def format_data(self, data) -> str:
        data = str(data).replace(' ', '')
        if len(data) != 16:
            raise ValueError('Invalid data')
        return data

