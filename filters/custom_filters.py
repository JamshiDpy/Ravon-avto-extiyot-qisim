from abc import ABC

from aiogram.dispatcher.filters import BoundFilter

from aiogram import types

from data.config import ADMINS


class IsGroupAdmin(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        member = await message.chat.get_member(message.from_user.id)
        return not member.is_chat_admin()


class IsBotAdmin(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.from_user.id in ADMINS


class ChatTypeFilter(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.chat.type in (types.ChatType.GROUP, types.ChatType.SUPERGROUP)


class PrivateChat(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.chat.type == types.ChatType.PRIVATE
