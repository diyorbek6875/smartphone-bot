from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from . import handlers


def main(token):
    # updater
    updater = Updater(token)

    # dispatcher
    dispatcher = updater.dispatcher

    # command handlers
    dispatcher.add_handler(CommandHandler('start', handlers.start))

    # message handlers
    dispatcher.add_handler(MessageHandler(Filters.text('🛍 Shop'), handlers.shop))
    dispatcher.add_handler(MessageHandler(Filters.text('🛒 Cart'), handlers.cart))
    dispatcher.add_handler(MessageHandler(Filters.text('📞 Contact'), handlers.contact))
    dispatcher.add_handler(MessageHandler(Filters.text('📝 About'), handlers.about))

    # start polling
    updater.start_polling()
    updater.idle()

