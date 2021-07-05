import os


class LangLoader:

    def __init__(self, path_to_lang: str):
        self.__path = path_to_lang
        self.__dirs = os.listdir(self.__path)
        self.__data = {}

        for dir in self.__dirs:

            if dir in ['__pycache__', '__init__.py']:
                continue

            path_to_module = self.__path.replace('/', '.')[2:] + f'.{dir}'

            self.__data[dir] = __import__(path_to_module, globals(), locals(), [dir], 0)

    def __getitem__(self, item):
        return self.__data[item]
