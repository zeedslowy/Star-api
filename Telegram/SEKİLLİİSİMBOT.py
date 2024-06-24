import telebot
import requests
from bs4 import BeautifulSoup
from telebot import types

# Telegram bot token
TOKEN = "7263637843:AAHS-ozRJjbCCaB7dho-z7u_g4WNkNgARhc"

# Create a bot instance
bot = telebot.TeleBot(TOKEN)

# Function to send messages to the chat
def send_message(chat_id, message):
    bot.send_message(chat_id, message)

# Function to generate and send fonts
def generate_and_send_fonts(chat_id, font_name):
    font_api = f"https://coolnames.online/cool.php?name={font_name}"
    response = requests.get(font_api)
    soup = BeautifulSoup(response.content, 'html.parser')
    fonts = soup.find_all('textarea')

    if fonts:
        for font in fonts:
            send_message(chat_id, font.text.strip())
        
# Handler for the /start command
@bot.message_handler(commands=['start'])
def start(message):
    first = message.from_user.first_name
    use = message.from_user.username
    p1ng = "https://telegra.ph/file/4f0860fbf5e50bcc67057.jpg"
    markup = types.InlineKeyboardMarkup(row_width=1)
    button = types.InlineKeyboardButton(text="TELEGRAM", url="https://t.me/dijvarhack")
    markup.add(button)
    bot.send_photo(message.chat.id, p1ng, f"""
-   -   -   -   -  -  -  -  -  -  -   -   -   -   -  -  -  -
[=] 𝚂𝙴𝙻𝙰𝙼 :  𝙱𝙴𝙽 𝚈𝙰𝚉𝙸 𝚂𝚃𝙸𝙻𝙸 𝙾𝙻𝚄𝚂𝚃𝚄𝚁𝚄𝙲𝚄 𝙱𝙾𝚃
-   -   -   -   -  -  -  -  -  -  -   -   -   -   -  -  -  -
[=] 𝙺𝚄𝙻𝙻𝙰𝙽𝙸𝙲𝙸 :  𝙷𝙾𝚂 𝙶𝙴𝙻𝙳𝙸𝙽 @{use}
-   -   -   -   -  -  -  -  -  -  -   -   -   -   -  -  -  -
[=] 𝙺𝙾𝙼𝚄𝚃 :  /𝙵𝙾𝙽𝚃 LENOX
-   -   -   -   -  -  -  -  -  -  -   -   -   -   -  -  -  -
[=] 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 : @EVLiLENOX
-   -   -   -   -  -  -  -  -  -  -   -   -   -   -  -  -  -
  """, reply_markup=markup)

# Handler for the /font command
@bot.message_handler(commands=['font'])
def handle_font_command(message):
    chat_id = message.chat.id
    command_params = message.text.split()[1:]

    if command_params:
        font_name = ' '.join(command_params)
        generate_and_send_fonts(chat_id, font_name)
    else:
        send_message(chat_id, "❌ Yanlıs Kullanım !..\n\n🧸 Örnek: /font THG LENOX")

# Start the bot
bot.polling()
