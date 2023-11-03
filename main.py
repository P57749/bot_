from telegram import Bot
from telegram.ext import Application, ApplicationBuilder, MessageHandler, filters

TOKEN = '6920357470:AAEoABUsiNMI6bBg7eWk6WOenLtTuOuzi64'
bot = Bot(token=TOKEN)

async def message_handler(update, context):
    message = update.message
    chat_id = message.chat_id
    text = message.text

    # Guarda el mensaje en un archivo .txt
    with open('messages.txt', 'a') as f:
        f.write(f"Message from channel: {text}\n")

application = ApplicationBuilder().token(TOKEN).build()
application.add_handler(MessageHandler(filters.ALL, message_handler))

if __name__ == '__main__':
    application.run_polling(1.0)