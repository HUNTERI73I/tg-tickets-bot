import logging

from aiogram import Dispatcher

from data.config import ADMINS, LOG_CHAT

#         except Exception as err:
#             logging.exception(err)

# async def on_startup_notify(dp: Dispatcher):
#     for admin in ADMINS:
#         try:
#             await dp.bot.send_message(admin, "Бот Запущен")

#         except Exception as err:
#             logging.exception(err)

async def on_startup_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message(LOG_CHAT, 'Бот запущен')
    except Exception as err:
        logging.exception(err)


async def on_shutdown_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message(LOG_CHAT, 'Бот выключен')
    except Exception as err:
        logging.exception(err)
