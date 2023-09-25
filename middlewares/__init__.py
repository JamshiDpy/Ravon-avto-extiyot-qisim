from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware # MyMiddleware


if __name__ == "middlewares":
    # dp.middleware.setup(MyMiddleware())
    dp.middleware.setup(ThrottlingMiddleware())
