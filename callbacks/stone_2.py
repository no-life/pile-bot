from typing import Tuple, Optional

from telegram import InlineKeyboardMarkup
from telegram.utils.types import ODVInput

from callbacks.base import CallbackHandler


class Stone2CallbackHandler(CallbackHandler):
    key = 'stone_2'

    def get_message(self, chat_id: int) -> Tuple[str, ODVInput[str], Optional[InlineKeyboardMarkup]]:
        return 'Ты нашел легендарный шекель от Марка, попробуй еще раз /start', None, None
