import random
from typing import Tuple, Optional

from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.utils.types import ODVInput

from commands.private_command import PrivateCommandHandler


class StartCommandHandler(PrivateCommandHandler):
    command = 'start'

    def _get_message(self, chat_id: int) -> Tuple[str, ODVInput[str], Optional[InlineKeyboardMarkup]]:
        random_int = random.randrange(2)
        buttons = [
            InlineKeyboardButton(text='Камень', callback_data=f'stone_1'),
            InlineKeyboardButton(text='Камень', callback_data=f'stone_2'),
        ]
        if random_int:
            buttons.reverse()
        reply_markup = InlineKeyboardMarkup(inline_keyboard=[buttons])
        return f'Привет {self._boys[chat_id]}, угадай под каким камнем драмы', None, reply_markup
