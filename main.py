import asyncio  # Работа с асинхронностью


from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import config  # Config
from data import common
from handlers import numbers, stone, magic_ball


def register_routers(dp:Dispatcher):
    dp.include_routers(common.start)
    dp.include_routers(numbers.num)
    dp.include_routers(stone.sps)
    dp.include_routers(magic_ball.mag)



async def main():
    bot = Bot(token=config.token)
    dp = Dispatcher(storage=MemoryStorage())  # Менеджер бота

    register_routers(dp)

    try:
        print('Bot Started')
        await dp.start_polling(bot)

    finally:
        await bot.session.close()


if __name__ == '__main__':  # Если мы запускаем конкретно этот файл.
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')