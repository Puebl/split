import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from src.config import TELEGRAM_BOT_TOKEN
from src.db import init_db
from src.handlers import router

async def main():
    if not TELEGRAM_BOT_TOKEN:
        raise RuntimeError("TELEGRAM_BOT_TOKEN is not set. Put it in .env")

    init_db()

    bot = Bot(token=TELEGRAM_BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(router)

    print("SplitBuddy bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
