from typing import Tuple, Optional

from telegram import InlineKeyboardMarkup
from telegram.utils.types import ODVInput

from callbacks.base import CallbackHandler


class Stone1CallbackHandler(CallbackHandler):
    key = 'stone_1'

    def get_message(self, chat_id: int) -> Tuple[str, ODVInput[str], Optional[InlineKeyboardMarkup]]:
        return 'Не сдесь даун, вот те /start', None, None
