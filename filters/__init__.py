from aiogram import Dispatcher

from loader import dp
from . custom_filters import IsGroupAdmin, ChatTypeFilter, IsBotAdmin, PrivateChat

if __name__ == "filters":
    dp.filters_factory.bind(IsGroupAdmin)
    dp.filters_factory.bind(ChatTypeFilter)
    dp.filters_factory.bind(PrivateChat)

