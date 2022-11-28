from aiogram import types

from loader import dp


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    print(message.chat.id)
    await message.answer(f"Эхо."
                         f"Сообщение:\n"
                         f"{message.text}")
