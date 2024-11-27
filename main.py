import asyncio

from handlers.home_works import hw_router
from handlers.start import start_router
from bot_config import bot, dp, database

async def on_startup(bot):
    database.create_table()


async def main():
    dp.include_router(hw_router)
    dp.include_router(start_router)

    dp.startup.register(on_startup)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())