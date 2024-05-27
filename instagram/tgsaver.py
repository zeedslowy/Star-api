import requests
from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler

# Telegram botunuzun token'ı
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

# Instagram video indirme fonksiyonu
def download_instagram_video(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    video_url = soup.find('meta', property='og:video')['content']
    return video_url

# /start komutu
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Merhaba! Instagram video indirmek için /download_instagram_video komutunu kullanabilirsiniz.")

# /download_instagram_video komutu
def download_instagram_video_command(update, context):
    # Kullanıcı tarafından gönderilen Instagram video URL'si
    url = context.args[0]
    video_url = download_instagram_video(url)
    context.bot.send_video(chat_id=update.effective_chat.id, video=video_url)

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Komut işleyicilerini kaydetme
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    download_instagram_video_handler = CommandHandler('download_instagram_video', download_instagram_video_command)
    dispatcher.add_handler(download_instagram_video_handler)

    # Botu çalıştırma
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
