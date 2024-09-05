from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message
from typing import Tuple, List, Optional

from data.config import admin_id
from loader import connection
from utils.format_cake import format_cake

router = Router()


@router.message(Command('top'))
async def get_top_command_handler(message: Message):
    async with await connection.execute(
        'SELECT name, cake FROM users WHERE cake > 0 AND id <> ? ORDER BY -cake LIMIT 10 OFFSET 0;',
        (admin_id,)
    ) as cursor:
        rows: List[Optional[Tuple[str, int]]] = await cursor.fetchall()
    
    if rows:
        leaderboard_content = ''
        for i in enumerate(rows, 1):
            user = i[1]
            user_name = user[0]
            user_cake = user[1]

            user_cake = await format_cake(user_cake)

            leaderboard_content += f'\n{i[0]}. {user_name} - <b>{user_cake}</b>'
    else:
        leaderboard_content = '\n  — Здесь пока никого нет! 😢'
    
    await message.answer(
        f'🏆 Список лидеров'
        f'\n{leaderboard_content}'
    )
