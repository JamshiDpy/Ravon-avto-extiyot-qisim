from aiogram import types

from loader import dp
from filters import ChatTypeFilter

# Echo bot
@dp.message_handler(ChatTypeFilter(), state=None)
async def bot_echo(message: types.Message):
    await message.answer(message.text)
