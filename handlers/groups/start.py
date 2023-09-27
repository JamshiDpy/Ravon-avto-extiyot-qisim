from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from filters.custom_filters import IsBotAdmin, ChatTypeFilter
from data.config import ADMINS

from loader import dp


@dp.message_handler(ChatTypeFilter(), CommandStart())
async def start(message: types.Message):
    await message.answer(text=f"{message.from_user.first_name} Ravon avto extiyot qisimlari guruhiga hush kelibsiz !!!")


@dp.message_handler(ChatTypeFilter(), content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def new_chat_member(message: types.Message):
    if message.new_chat_members[0].is_bot:
        await message.bot.ban_chat_member(chat_id=-1001554079401, user_id=message.new_chat_members[0].id)
        print(message.new_chat_members[0].first_name, 'nomli bot guruhdan chiqarb yuborldi !!!')
