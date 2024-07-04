# ! Aşamasındadır !

import os
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Telegram bot token
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Shodan API key
SHODAN_API_KEY = 'YOUR_SHODAN_API_KEY'

# Telegram bot command handlers
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Merhaba! Shodan taraması yapmak için /search komutunu kullanın.")

def search(update, context):
    query = ' '.join(context.args)
    if not query:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Lütfen bir arama sorgusu girin.")
        return

    try:
        # Shodan API'ye sorgu gönder
        url = f'https://api.shodan.io/shodan/host/search?key={SHODAN_API_KEY}&query={query}'
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Sonuçları görüntüle
        if data['total'] > 0:
            message = f"Shodan taraması sonucu:\n\n"
            for host in data['matches']:
                message += f"IP: {host['ip_str']}\n"
                message += f"Port: {host['port']}\n"
                message += f"Başlık: {host['title']}\n"
                message += f"Şehir: {host['location']['city']}\n"
                message += f"Ülke: {host['location']['country_name']}\n\n"
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Arama sonuçlarında hiçbir sonuç bulunamadı.")
    except requests.exceptions.RequestException as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hata oluştu: {e}")

def main():
    # Telegram bot oluştur
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("search", search))

    # Botu çalıştır
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
