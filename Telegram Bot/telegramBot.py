import telegram.ext

TOKEN = '2033158457:AAHi4kN9vrD0Vnl0-kZLLYvoA0EY5ssMY-U'

def start(update, context):
    update.message.reply_text("Welcome to BiluBot")


def help(update, context):
    update.message.reply_text("The following commands are available:"
                               "/start --> Welcome message"
                               "/help --> This message"
                               "/content --> Info about BiluBot content"
                               "/contact --> Info about contact")


def contact(update, context):
    update.message.reply_text("Mobile: 0502436148")


def content(update, context):
    update.message.reply_text("No content right now, try later.")




updater = telegram.ext.Updater(TOKEN, use_context=True)

disp = updater.dispatcher




disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("contact", contact))
disp.add_handler(telegram.ext.CommandHandler("content", content))

updater.start_polling()
updater.idle()
