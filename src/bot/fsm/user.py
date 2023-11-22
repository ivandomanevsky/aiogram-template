from aiogram.fsm.state import StatesGroup, State


class User(StatesGroup):
    add = State()
    delete = State()
