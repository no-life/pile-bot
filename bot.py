from telegram.ext import Updater, CommandHandler, CallbackContext

from callbacks.stone_1 import Stone1CallbackHandler
from callbacks.stone_2 import Stone2CallbackHandler
from commands.start import StartCommandHandler


def hello(update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater('5205890892:AAFOPNz48m73I71aBBeSP0TFDZBtpacJKts')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(StartCommandHandler().as_handler())
updater.dispatcher.add_handler(Stone1CallbackHandler().as_handler())
updater.dispatcher.add_handler(Stone2CallbackHandler().as_handler())

updater.start_polling()
updater.idle()
