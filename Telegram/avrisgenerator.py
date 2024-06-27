import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

# Telegram bot token'i
TOKEN = 'BOTUNUZ_TOKEN'

# Avris Generator API endpoint'i
AVRIS_API_URL = 'https://generator.avris.it/api'

# Bot için mevcut komutlar
AVAILABLE_COMMANDS = ['/ean13', '/pesel', '/tc']

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Merhaba! Avris Generator API'sini kullanarak kod üreten ve doğrulayan bir botum. İşte mevcut komutlar:")
    context.bot.send_message(chat_id=update.effective_chat.id, text='\n'.join(AVAILABLE_COMMANDS))

def generate(update, context):
    command = update.message.text.split()[0]
    if command == '/ean13':
        generator = 'ean13'
    elif command == '/pesel':
        generator = 'pesel'
    elif command == '/tc':
        generator = 'it_codice_fiscale'
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Bilinmeyen komut. Lütfen tekrar deneyin.")
        return

    response = requests.get(f"{AVRIS_API_URL}/{generator}").json()
    context.bot.send_message(chat_id=update.effective_chat.id, text=response['result'])

def validate(update, context):
    command = update.message.text.split()[0]
    if command == '/ean13':
        generator = 'ean13'
    elif command == '/pesel':
        generator = 'pesel'
    elif command == '/tc':
        generator = 'it_codice_fiscale'
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Bilinmeyen komut. Lütfen tekrar deneyin.")
        return

    value = ' '.join(update.message.text.split()[1:])
    response = requests.get(f"{AVRIS_API_URL}/{generator}/{value}").json()
    if response['valid']:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"'{value}' değeri geçerli.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"'{value}' değeri geçerli değil.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Komut işleyicileri ekleniyor
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ean13", generate))
    dp.add_handler(CommandHandler("pesel", generate))
    dp.add_handler(CommandHandler("tc", generate))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, validate))

    # Bot başlatılıyor
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
