from asyncio import run

from loader import bot, dp, connection
from handlers import start_handler, cake_handler, help_handler, top_handler
from middlewares.register_user import RegisteringUserMiddleware


@dp.shutdown()
async def on_shutdown():
    await connection.close()
    print('Telegram-Bot has been closed')


async def main():
    await connection.initialize()

    await connection.execute(
        '''CREATE TABLE IF NOT EXISTS users(
            id BIGINT PRIMARY KEY,
            name TEXT NOT NULL,
            cake NUMERIC DEFAULT 0,
            eat_lately BIGINT DEFAULT 0
        );
        '''
    )

    dp.include_routers(
        start_handler.router,
        cake_handler.router,
        help_handler.router,
        top_handler.router
    )
    dp.message.middleware(RegisteringUserMiddleware())

    print('Telegram-Bot has been launched successfully!')

    await bot.delete_webhook(True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        run(main())
    except KeyboardInterrupt:
        ...
