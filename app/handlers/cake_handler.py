from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message
from typing import Tuple

from data.config import MIN_CAKE_MULTIPLIER, MAX_CAKE_MULTIPLIER, CAKE_AMOUNT, CAKE_DELAY
from loader import connection
from utils.randint import randint
from utils.format_cake import format_cake
from utils.format_time import format_time
from utils.timestamp import get_current_timestamp

router = Router()


@router.message(Command('cake'))
async def get_cake_command_handler(message: Message):
    user_id = message.from_user.id

    async with await connection.execute(
        'SELECT name, cake, eat_lately FROM users WHERE id = ?;',
        (user_id,)
    ) as cursor:
        row: Tuple[int, int] = await cursor.fetchone()
    
    user_name, user_cake, user_eat_lately = row
    current_time = await get_current_timestamp()

    if user_eat_lately + CAKE_DELAY > current_time:
        time_left = int(user_eat_lately + CAKE_DELAY - current_time)
        time_left_formatted = await format_time(time_left)
        await message.answer(
            f'<i>{user_name}</i>, тебе ещё рано есть торт! 🍰'
            f'\n  — Приходи снова через {time_left_formatted}'
        )
        return

    add_cake = await randint(MIN_CAKE_MULTIPLIER, MAX_CAKE_MULTIPLIER)
    add_cake *= CAKE_AMOUNT

    user_eat_lately = current_time

    await connection.execute(
        'UPDATE users SET cake = cake + ?, eat_lately = ? WHERE id = ?;',
        (add_cake, user_eat_lately, user_id)
    )

    user_cake += add_cake

    add_cake_formatted = await format_cake(add_cake)
    user_cake_formatted = await format_cake(user_cake)

    await message.answer(
        f'<i>{user_name}</i>, ты съел(-а) <b>{add_cake_formatted}</b> торта 🍰'
        f'\n  — Съедено всего - <b>{user_cake_formatted}</b>'
    )
