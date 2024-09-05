from aiogram import Router, Bot
from aiogram.filters.command import CommandStart
from aiogram.types import Message
from typing import Tuple

from keyboards.start_keyboard import StartKeyboard
from loader import connection
from utils.format_cake import format_cake

router = Router()


@router.message(CommandStart())
async def get_start_command_handler(message: Message, bot: Bot):
    user_id = message.from_user.id

    async with await connection.execute(
        'SELECT name, cake FROM users WHERE id = ?;',
        (user_id,)
    ) as cursor:
        row: Tuple[str, int] = await cursor.fetchone()
    
    user_name, user_cake = row

    user_cake_formatted = await format_cake(user_cake)

    _bot = await bot.get_me()
    url = f't.me/{_bot.username}?startgroup'
    markup = await StartKeyboard.markup(url)

    await message.answer(
        f'Привет, <i>{user_name}</i>! Ты съел(-а) <b>{user_cake_formatted}</b> торта'
        '\n  — Напиши команду /cake, чтобы съесть торт 🍰',
        reply_markup=markup
    )
