import subprocess
import telebot
import os

# Telegram botunuzun token'ını buraya girin
TOKEN = "7173279580:AAHoHdXeQh4qU_JI5eOmnZPsU_pJlPZ-HAo"

# Telegram botu oluşturma
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Merhaba! Ben Çalıştırma Botu. Bana bir Python dosyası (.py) gönderin, ben de çalıştırıp sonucunu size göndereyim.")

@bot.message_handler(content_types=['document'])
def handle_document(message):
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        # Dosyayı kaydetme
        file_path = message.document.file_name
        with open(file_path, 'wb') as new_file:
            new_file.write(downloaded_file)
        
        # Kodu çalıştırma
        process = subprocess.Popen(["python", file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        result = output.decode("utf-8")
        if error:
            result += "\nHata:\n" + error.decode("utf-8")

        bot.send_message(message.chat.id, f"Sonuç:\n{result}")

        # Temizlik işlemi
        clean_up([file_path])

    except Exception as e:
        bot.send_message(message.chat.id, f"Hata oluştu: {str(e)}")

def clean_up(file_paths):
    for file_path in file_paths:
        try:
            os.remove(file_path)
        except OSError as e:
            print(f"Error: {file_path} : {e.strerror}")

bot.polling()