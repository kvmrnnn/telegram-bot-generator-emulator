from functools import reduce
from typing import Union


class Card:
    def __init__(self, code: str, date=None, cvv=None):
        if not Card.is_code_valid(code):
            raise ValueError('Invalid data')
        self.code = code
        self.date = date
        self.cvv = cvv

    @staticmethod
    def is_code_valid(code: Union[str, int]):
        LOOKUP = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)
        code = reduce(str.__add__, filter(str.isdigit, code))
        evens = sum(int(i) for i in code[-1::-2])
        odds = sum(LOOKUP[int(i)] for i in code[-2::-2])
        return ((evens + odds) % 10 == 0)
