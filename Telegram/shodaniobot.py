# ! Deneme Aşamasındadır !

import os
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Telegram bot token
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Shodan web araması URL'si
SHODAN_SEARCH_URL = 'https://www.shodan.io/search?query={query}'

# Telegram bot command handlers
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Merhaba! Shodan taraması yapmak için /search komutunu kullanın.")

def search(update, context):
    query = ' '.join(context.args)
    if not query:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Lütfen bir arama sorgusu girin.")
        return

    try:
        # Shodan web arama sayfasına sorgu gönder
        url = SHODAN_SEARCH_URL.format(query=query)
        response = requests.get(url)
        response.raise_for_status()

        # Sonuçları görüntüle
        if 'No results found' not in response.text:
            message = f"Shodan taraması sonucu:\n\n{url}"
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Arama sonuçlarında hiçbir sonuç bulunamadı.")
    except requests.exceptions.RequestException as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hata oluştu: {e}")

def main():
    # Telegram bot oluştur
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Komutları kaydet
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("search", search))

    # Botu çalıştır
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
