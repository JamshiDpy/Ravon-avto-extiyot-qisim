from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from filters import IsBotAdmin, PrivateChat
from data.config import ADMINS
from states.states import Users

from loader import dp


@dp.message_handler(PrivateChat(), CommandStart())
async def start(message: types.Message):
    await message.answer(text=f"{message.from_user.first_name} Ravon avto extiyot qisimlari botiga hush kelibsiz !!!")
