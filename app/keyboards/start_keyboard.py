from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class StartKeyboard:
    button_text_1 = '✅ Добавить в группу'

    @classmethod
    async def markup(self, url: str) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=self.button_text_1,
                        url=url
                    )
                ]
            ]
        )
