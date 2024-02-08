import asyncio

from core import bot


async def main():
    from handlers import dp

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
