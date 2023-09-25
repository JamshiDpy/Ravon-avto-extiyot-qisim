from aiogram.dispatcher.filters.state import StatesGroup, State


class Admins(StatesGroup):
    pass


class Users(StatesGroup):
    first_step = State()
