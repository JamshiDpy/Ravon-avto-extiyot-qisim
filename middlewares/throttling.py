import asyncio

from aiogram import types, Dispatcher
from aiogram.dispatcher import DEFAULT_RATE_LIMIT
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.exceptions import Throttled

from data.config import ADMINS
from filters import ChatTypeFilter

class ThrottlingMiddleware(BaseMiddleware):
    """
    Simple middleware
    """

    def __init__(self, limit=DEFAULT_RATE_LIMIT, key_prefix='antiflood_'):
        self.rate_limit = limit
        self.prefix = key_prefix
        super(ThrottlingMiddleware, self).__init__()

    async def on_process_message(self, message: types.Message, data: dict):
        handler = current_handler.get()
        dispatcher = Dispatcher.get_current()
        if handler:
            limit = getattr(handler, "throttling_rate_limit", self.rate_limit)
            key = getattr(handler, "throttling_key", f"{self.prefix}_{handler.__name__}")
        else:
            limit = self.rate_limit
            key = f"{self.prefix}_message"
        try:
            await dispatcher.throttle(key, rate=limit)
        except Throttled as t:
            await self.message_throttled(message, t)
            raise CancelHandler()

    async def message_throttled(self, message: types.Message, throttled: Throttled):
        if throttled.exceeded_count <= 2:
            await message.reply("Too many requests!")


# class MyMiddleware(BaseMiddleware):
#
#     async def on_pre_process_update(self, update: types.Update, data: dict):
#         if update.message.from_user.id not in ADMINS:
#             if "caption_entities" in update.message:
#                  if update.message.caption_entities[0].type == 'text_url' or 'url' or 'mention':
#                      await update.message.bot.delete_message(chat_id=-1001869907239, message_id=update.message.message_id)
#                      await update.message.answer(
#                          f"{update.message.from_user.first_name} bu guhga havola biriktirilgan media yuborish taqiqlanadi")



