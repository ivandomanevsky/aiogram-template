from aiogram import types
from aiogram.filters import BaseFilter
from src.configuration import conf


class IsAdmin(BaseFilter):
    def __init__(self) -> None:
        self.admin_id = conf.bot.admin_id

    async def __call__(self, message: types.Message) -> bool:
        return str(message.from_user.id) == self.admin_id
