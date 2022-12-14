from aiogram.utils.executor import start_polling, start_webhook

from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify, on_shutdown_notify
from utils.set_bot_commands import set_default_commands
from data.config import WEBHOOK, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT, WEBHOOK_URL


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    await dp.bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)
    # Уведомляет про запускs
    await on_startup_notify(dispatcher)
    

async def on_shutdown(dispatcher):
    await on_shutdown_notify(dispatcher)
    await dp.bot.delete_webhook()


if __name__ == '__main__':
    if WEBHOOK:
        start_webhook(
            dispatcher=dp,
            webhook_path=WEBHOOK_PATH,
            skip_updates=True,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            host=WEBAPP_HOST,
            port=WEBAPP_PORT,
        )
    else:
        start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
