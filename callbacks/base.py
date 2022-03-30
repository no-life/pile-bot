from abc import abstractmethod
from typing import Any, Tuple, Optional, Union

from telegram import InlineKeyboardMarkup, Update, Bot, TelegramError
from telegram.ext import CallbackQueryHandler, CallbackContext
from telegram.utils.types import ODVInput


class CallbackHandler:
    key: str

    _need_permissions_text = 'Необходимо авторизоваться /start'

    @abstractmethod
    def get_message(self, chat_id: int) -> Tuple[str, ODVInput[str], Optional[InlineKeyboardMarkup]]:
        raise NotImplementedError

    def as_handler(self) -> CallbackQueryHandler[CallbackContext[Any, Any, Any]]:
        return CallbackQueryHandler(pattern=self._pattern, callback=self._callback)

    @classmethod
    def _pattern(cls, key: object) -> Optional[bool]:
        return cls.key == key

    def _callback(self, update: Update, context: CallbackContext[Any, Any, Any]) -> Optional[str]:
        effective_chat = update.effective_chat
        effective_message = update.effective_message
        callback_query = update.callback_query

        # noinspection PyBroadException
        try:
            return self._handle(
                bot=context.bot,
                chat_id=effective_chat.id,                                                          # type: ignore
                message_id=effective_message.message_id,                                            # type: ignore
            )
        except Exception:
            pass
        finally:
            context.bot.answer_callback_query(callback_query_id=callback_query.id)
        return None

    def _handle(self, bot: Bot, chat_id: int, message_id: int) -> Optional[Union[int, str]]:
        if not self._has_permissions(chat_id):
            return self._answer(bot=bot, chat_id=chat_id, message_id=message_id, text=self._need_permissions_text)

        text, parse_mode, reply_markup = self.get_message(chat_id)
        self._answer(
            bot=bot,
            chat_id=chat_id,
            message_id=message_id,
            text=text,
            parse_mode=parse_mode,
            reply_markup=reply_markup,
        )
        return None

    def _has_permissions(self, chat_id: int) -> bool:
        return self._user_exists(chat_id)

    @classmethod
    def _user_exists(cls, chat_id: int) -> bool:
        return True

    @classmethod
    def _answer(  # noqa: WPS211
        cls,
        bot: Bot,
        chat_id: int,
        message_id: int,
        text: str,
        parse_mode: ODVInput[str] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
    ):
        try:
            bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=text,
                parse_mode=parse_mode,
                reply_markup=reply_markup,
            )
        except TelegramError:
            bot.send_message(chat_id=chat_id, text=text, parse_mode=parse_mode, reply_markup=reply_markup)