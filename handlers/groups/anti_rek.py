from loader import dp
from aiogram import types
from filters.custom_filters import IsGroupAdmin, ChatTypeFilter

from data.config import ADMINS
from states.states import Users


@dp.message_handler(IsGroupAdmin(), ChatTypeFilter())
async def delete_rek(message: types.Message):
    print(message)
    if message.entities:
        if message.entities[0].type == 'url' or 'mention':
            await message.bot.delete_message(chat_id=-1001554079401, message_id=message.message_id)
            await message.answer(f"{message.from_user.first_name} bu guruhga havola tarqatish taqiqlanadi ❌❌❌")


@dp.message_handler(IsGroupAdmin(), ChatTypeFilter(), content_types=types.ContentType.ANY)
async def media(message: types.Message):
    if 'caption_entities' in message:
        if message.caption_entities[0].type == 'url' or 'text_url' or 'text_link' or 'mention':
           await message.bot.delete_message(chat_id=-1001554079401, message_id=message.message_id)
           await message.answer(text=f"{message.from_user.first_name} Bu guruhga bog'lama biriktirilga medialar yuborish taqiqlanadi ❌❌❌")
