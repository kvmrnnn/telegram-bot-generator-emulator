from typing import Union, List

from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message


class NotCommand(BoundFilter):
    key = 'not_commands'

    def __init__(self, commands: Union[str, List[str]]):
        if isinstance(commands, str):
            self.commands = [commands]
        elif isinstance(commands, list):
            self.commands = list(set(commands))

    async def check(self, message: Message) -> bool:
        for command in self.commands:
            if command.lower() in message.text.lower():
                return False
        return True
