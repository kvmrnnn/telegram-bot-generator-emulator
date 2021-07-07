from PIL import Image

from app.data.types.qrcode import QRCodeMagnit, QRCode5ka
from app.data.types.tmp_files import PhotoFile


class EmulatorBase(PhotoFile):
    def __init__(self, path_to_emulator):
        super().__init__()
        self.path_to_emulator = path_to_emulator
        self.generate()

    def generate(self):
        raise ValueError('This is an abstract method')


class EmulatorMagnit(EmulatorBase):
    emulator_path = './app/data/cache/emulator_magnit.jpeg'

    def __init__(self, code):
        self.file_qrcode = QRCodeMagnit(code)
        super().__init__(self.emulator_path)

    def generate(self):
        qrcode_img = Image.open(self.file_qrcode.path_to_file)
        emulator_app = Image.open(self.emulator_path)

        x1 = emulator_app.size[0] // 2 - qrcode_img.size[0] // 2
        x2 = emulator_app.size[0] // 2 + qrcode_img.size[0] // 2
        y1 = 590 - qrcode_img.size[1] // 2
        y2 = 590 + qrcode_img.size[1] // 2

        emulator_app.paste(qrcode_img, (x1, y1, x2, y2))
        emulator_app.save(self.path_to_file)


class Emulator5ka(EmulatorBase):
    emulator_path = './app/data/cache/emulator_5ka.jpeg'

    def __init__(self, code):
        self.file_qrcode = QRCode5ka(code)
        super().__init__(self.emulator_path)



