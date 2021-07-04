import os


class LoaderText:

    def __init__(self, path_to_text: str):
        self.__path = path_to_text
        self.__dirs = os.listdir(self.__path)
        self.__text = {}

        for dir in self.__dirs:

            if dir in ['__pycache__', '__init__.py']:
                continue

            file = open(f'{self.__path}/{dir}')

            self.__text[dir.split('.')[0]] = file.read()

            file.close()

    def __getattr__(self, item) -> str:
        return self.__text[item]
