from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message

router = Router()


@router.message(Command('help'))
async def get_help_command_handler(message: Message):
    commands = {
        'start': 'Начать',
        'help': 'Помощь',
        'cake': 'Съесть торт',
        'top': 'Список лидеров'
    }

    text = '🔍 Помощь\n' + (''.join(f'\n  — /{i[0]} - {i[1]}' for i in commands.items()))
    await message.answer(text)