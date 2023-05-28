import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from handlers import registerUserHandlers

storage = MemoryStorage()


def register_handler(dp: Dispatcher):
    registerUserHandlers(dp)

async def main():
    load_dotenv()
    bot = Bot(os.getenv('TOKEN_API'))
    dp = Dispatcher(bot, storage=storage)
    registerUserHandlers(dp)
    try:
        await dp.skip_updates()
        await dp.start_polling()
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    asyncio.run(main())
