from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand('game', "Запустить рег на игру"),
            types.BotCommand('leave', 'Выйти из игры'),
            types.BotCommand('stop', 'Остановить игру или регистрацию'),
            types.BotCommand('reg', 'Зарегистрироваться или войти в игру'),
            types.BotCommand('options', 'Админ панель чата'),
            types.BotCommand('go', 'Начать игру')
            # types.BotCommand('autostart', 'Автостарт игр'),
        ]
    )
