from abc import abstractmethod
from typing import Any, Tuple, Optional

from telegram import Bot, Update, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackContext
from telegram.utils.types import ODVInput


class PrivateCommandHandler:
    command: str

    _error_text = 'Чел ты...'
    _need_permissions_text = 'Незя('
    _boys = {290121941: 'Жека', 238636820: 'Артем', 5231888903: 'Костя', 5232310056: 'Ваня'}

    def as_handler(self) -> CommandHandler[CallbackContext[Any, Any, Any]]:
        return CommandHandler(command=self.command, callback=self._callback)

    def _callback(self, update: Update, context: CallbackContext[Any, Any, Any]) -> None:
        effective_chat = update.effective_chat

        try:
            self._handle(bot=context.bot, chat_id=effective_chat.id)
        except Exception as e:
            print(e)
            context.bot.send_message(chat_id=effective_chat.id, text=self._error_text)

    def _handle(self, bot: Bot, chat_id: int) -> None:
        if not self._has_permissions(chat_id):
            bot.send_message(chat_id=chat_id, text=self._need_permissions_text)
            return

        text, parse_mode, reply_markup = self._get_message(chat_id)
        bot.send_message(
            chat_id=chat_id,
            text=text,
            parse_mode=parse_mode,
            reply_markup=reply_markup,
        )

    def _has_permissions(self, chat_id: int) -> bool:
        return chat_id in self._boys

    @abstractmethod
    def _get_message(self, chat_id: int) -> Tuple[str, ODVInput[str], Optional[InlineKeyboardMarkup]]:
        raise NotImplementedError
