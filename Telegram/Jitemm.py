import telebot
import json
import requests
from telebot import types
import time
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from io import BytesIO
from datetime import datetime
from pytz import timezone
from datetime import timedelta
import sqlite3
from bs4 import BeautifulSoup
from flask import Flask, request
import telegram
from datetime import datetime, timedelta
import threading
import pytz
import re
import os



TOKEN = 'tokengir'

bot = telebot.TeleBot("tokengir")

print("Bot Calisiyor")


def is_user_in_channel(chat_id, channel_username):
    try:
        member = bot.get_chat_member(channel_username, chat_id)
        return member.status != "left"
    except telebot.apihelper.ApiException:
        return False



def fetch_data_from_api(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"⚠️ işlem sırasında Hata oluştu: {e}")
        return None





def get_username(user_id):
    cursor.execute('SELECT username FROM users WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    return result[0] if result else None

def get_last_registered_user():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users ORDER BY id DESC LIMIT 1')
        return cursor.fetchone()

        
conn = sqlite3.connect('veritabani.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        username TEXT,
        password TEXT
    )
''')
conn.commit()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS logged_in_users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER
    )
''')
conn.commit()


conn.close()



def get_connection():
    return sqlite3.connect('veritabani.db')

def is_username_taken(username):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        return cursor.fetchone() is not None


def is_user_registered(user_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
        return cursor.fetchone() is not None

def is_username_taken(username):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        return cursor.fetchone() is not None

def add_user(user_id, username, password):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (user_id, username, password) VALUES (?, ?, ?)', (user_id, username, password))
        conn.commit()

def check_credentials(username, password):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        return cursor.fetchone() is not None

def add_login_user(user_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO logged_in_users (user_id) VALUES (?)', (user_id,))
        conn.commit()

def is_user_logged_in(user_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM logged_in_users WHERE user_id = ?', (user_id,))
        return cursor.fetchone() is not None

def remove_login_user(user_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM logged_in_users WHERE user_id = ?', (user_id,))
        conn.commit()


def add_userr(user_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (user_id) VALUES (?)', (user_id,))
        conn.commit()




import base64
from io import BytesIO



def fetch_data_from_api(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as errh:
        return f'Hata! HTTP Error: {errh}'
    except requests.exceptions.ConnectionError as errc:
        return f'Hata! Bağlantı Hatası: {errc}'
    except requests.exceptions.Timeout as errt:
        return f'Hata! Zaman Aşımı Hatası: {errt}'
    except requests.exceptions.RequestException as err:
        return f'Hata! Genel Hata: {err}'
    except Exception as e:
        return f'Hata! {str(e)}'


conn = sqlite3.connect("ban.db")
cursor = conn.cursor()

# Create the bans table
cursor.execute("CREATE TABLE IF NOT EXISTS bans (user_id INTEGER, reason TEXT, end_date TEXT)")

# Commit changes and close the connection
conn.commit()
conn.close()


def check_active_bans():
    with sqlite3.connect("ban.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT user_id, end_date FROM bans WHERE end_date > ?", (datetime.now(),))
        active_bans = cursor.fetchall()

    for user_id, end_date in active_bans:
        # Implement logic to handle active bans, e.g., store in-memory or take some action
        print(f"User {user_id} is still banned until {end_date}")

# Call the function when the bot starts
check_active_bans()


def is_premium(user_id):
    logged_in_ids = read_ids_from_file('premium.txt')
    return str(user_id) in logged_in_ids

def read_ids_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]










@bot.message_handler(commands=['start'])
def handle_start(message):
    if message.chat.type != "private":
        return
    user_id = message.from_user.id
    random_messages = ['Jitemin Şuanki Coderi 16 yaşındadır.', 'Jitemin Alt Yapı Yapım Süresi 5 Hafta sürmüştür.', 'Jitemin Alt Yapı Yapım Süresi 5 Hafta sürmüştür.', 'Jitem Her Geçen Gün daha çok Gelişiyor ve Gelişmeye devam ediyor!', 'Jitemin Toplam Admin Sayısı 2. dir']
    selected_message = random.choice(random_messages)
    
    if not is_user_registered(user_id):
        add_userr(user_id)
        
    username = message.from_user.username
    first_name = message.from_user.first_name
    query_count = get_query_count()
    tz_Turkey = pytz.timezone('Europe/Istanbul')
    saat = datetime.now(tz_Turkey).strftime('%H:%M:%S')
    last_registered_user = get_last_registered_user()

    if last_registered_user:
        last_registered_username = last_registered_user[2]
        now = datetime.now(tz_Turkey)
        current_hour = now.hour
        if 6 <= current_hour < 12:
            greeting = "İyi Sabahlar"
        elif 12 <= current_hour < 18:
            greeting = "İyi Öğleler"
        elif 18 <= current_hour < 24 or 0 <= current_hour < 6:
            greeting = "İyi Akşamlar"
        else:
            greeting = "İyi Geceler"

    
    channel_username1 = '@CerenyTeam'
    channel_username2 = '@Bot4Chan'
    
    if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(0.1)
            bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
            return

    user_id = message.from_user.id
    ban_info = get_ban_info(user_id)
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(0.1)
    if ban_info:
        _, sebep, bitis_tarihi = ban_info
        bot.reply_to(message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için süresiz olarak şutlandın.*\n┃*📨 Sebep*: `{sebep}`\nBitiş Tarihi: {bitis_tarihi}\n\n┃*/itiraz Komutunu Kullanarak İtiraz Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode='Markdown')
        return
        
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        if not is_user_logged_in(user_id):
            bot.send_message(user_id, "*🚫 Üzgünüm, önce giriş yapmanız gerekiyor!*", parse_mode="Markdown")
            return
            
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(0.1)
    if is_user_registered(user_id):
        if is_user_logged_in(user_id):
            bot.send_message(user_id, f"*{greeting}, {first_name}👋!* (`{user_id}`)\n\n📚 *Komutlar Menüsüne Hoş geldin!*\n\n*📥 Toplam Sorgu Sayısı: {query_count}*\n*🧍 Son Kullanıcı:* `{last_registered_username}`\n*🎭 Üyelik Türü:* `Freemium`\n*⏳ Bitiş Tarihi: ∞*\n\n*❓ Biliyor Muydunuz?*: *{selected_message}*\n\n📣 *Duyuru:* `🥷 İfşala Geç Paşam`\n\n*Sistem • Komutları*\n*/cikisyap • Hesaptan Çıkış Yapar!*\n*/komutlar • Komutlar Listesini Verir*\n*/itiraz • Ban Yediğiniz Zaman İtiraz Edebilirsiniz*\n*/destek • Destek Talebi Oluşturur*\n\n*👪 Nüfus Ve Vatandaşlık İşleri • BÖLÜMÜ*\n*/sorgu • Ad Soyad'dan Kişinin Bilgilerini Verir* (`Free`)\n*/adres  •T.C'den Kişinin Adresini Verir* (`Kapalı`)\n*/kizlik • T.C'den Kişinin Kızlık Soyadını Verir* (`Free`)\n*/ailepro • T.C'den Kişinin Aile Bilgilerini Verir* (`Pro`) (`Free`)\n*/aile • T.C'den Kişinin Aile Bilgilerini Verir* (`Free`)\n*/sulale • T.C'den Kişinin Sülale Bilgilerini Verir* (`Free`)\n*/medeni • T.C'den Kişinin Medeni Halini Verir* (`Free`)\n*/tcpro • T.C'den Kişinin Detaylı Bilgilerini Verir* (`Kapalı`)\n*/tckn • T.C'den Kişinin Bilgilerini Verir* (`Free`)\n*/tcplaka • T.C'den Kişiye Yazılan Ceza Verir* (`Free`)\n*/plaka • Plaka'dan Ceza Bilgileri Verir* (`Free`)\n*/haciz • T.C'den Kişinin Haciz Bilgilerini Verir* (`Free`)\n*/iban • IBAN'dan İbana Ait Bilgileri Verir* (`Free`)\n*/ihbar • Adres'e ihbar Basar* (`Free`)\n\n*📱 Telefon Mobil İletişim Sistemi • BÖLÜMÜ*\n*/gsmtc • GSM'den T.C Verir* (`Free`)\n*/tcgsm • T.C'den GSM Verir* (`Free`)\n*/sms • GSM'ye Sms Saldırısı Yapar* (`Free`)\n*/operator • GSM'den Operatör Verir* (`Free`)\n\n*🏫 Millî Eğitim Bakanlığı • BÖLÜMÜ*\n*/vesika • T.C'den Kişinin E-okul Vesika Verir* (`Free`)\n\n*🎉 Eğlence • BÖLÜMÜ*\n*/index • URL'dan Sitenin indexini Verir* (`Free`)\n*/yaz Girilen Mesajı Deftere yazar* (`Free`)\n*/am • T.C'den Kişinin Am Vesika Verir* (`+18 içerir`) (`Free`)\n*/penis • T.C'den Penis CM Verir* (`Free`)\n\n*JİTEM © Tüm Hakları Saklıdır. Gizlilik, Kullanım ve Telif Hakları bildiriminde belirtilen kurallar çerçevesinde hizmet sunulmaktadır.*\n\n*Komutlar Hakkında Bilgi almak için*\n`/yardim KomutAdı` *girin.*\n\n`Free`: *Freemium Temsil eder.*\n`Pre`: *Premium temsil eder.*", parse_mode="Markdown")
        else:
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Giriş Yap", callback_data='login'))
            markup.add(types.InlineKeyboardButton("Kayıt Ol", callback_data='register'))
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(0.1)
            caption_text = f"*👋 Merhaba, {first_name} Ben Gelişmiş Bir Sorgu Botuyum Kayıt Olarak Veya Giriş Yaparak Botu Kullanmaya Başlayabilirsin.*"
            bot.send_photo(user_id, open("jitem.png", "rb"), caption=caption_text, reply_markup=markup, parse_mode="Markdown")




@bot.callback_query_handler(func=lambda call: True)
def handle_callbacks(call):
    if call.message.chat.type != "private":
        return

    user_id = call.from_user.id
    channel_username1 = '@CerenyTeam'
    channel_username2 = '@Bot4Chan'

    if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
        send_group_join_prompt(user_id)
        return

    ban_info = get_ban_info(user_id)
    if ban_info:
        handle_ban_info(call, ban_info)
        return

    if is_user_registered(user_id):
        if not is_user_logged_in(user_id):
            handle_login_or_register(call, user_id)
    elif call.data == 'register':
        handle_registration_prompt(call, user_id)
    else:
        send_registration_required_prompt(call, user_id)

def send_group_join_prompt(user_id):
    bot.send_chat_action(user_id, 'typing')
    time.sleep(0.1)
    bot.send_message(user_id, "*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")

def handle_ban_info(call, ban_info):
    _, sebep, bitis_tarihi = ban_info
    bot.reply_to(call.message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için Hesabın Engellendi*\n┃*📨 Sebep*: `{sebep}`\n┃*🕓 Bitiş Tarihi:* `{bitis_tarihi}`\n\n┃*/itiraz Komutunu Kullanarak İtiraz Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")

def handle_login_or_register(call, user_id):
    if call.data == 'login':
        send_login_prompt(call, user_id)
    else:
        handle_registration_prompt(call, user_id)

def send_login_prompt(call, user_id):
    bot.send_chat_action(call.message.chat.id, 'typing')
    time.sleep(0.1)
    bot.send_message(user_id, "*🧍 Kullanıcı Adı Girin:*", parse_mode="Markdown")
    bot.register_next_step_handler_by_chat_id(user_id, process_login_username_step)

def handle_registration_prompt(call, user_id):
    bot.send_chat_action(call.message.chat.id, 'typing')
    time.sleep(0.1)
    bot.send_message(user_id, "*🧍 Kullanıcı Adı Belirleyin:*", parse_mode="Markdown")
    bot.register_next_step_handler_by_chat_id(user_id, process_username_step)

def send_registration_required_prompt(call, user_id):
    bot.send_chat_action(call.message.chat.id, 'typing')
    time.sleep(0.1)
    bot.send_message(user_id, "*📥 Önce Kayıt olmanız gerekiyor.*", parse_mode="Markdown")




def process_username_step(message):
    if message.chat.type != "private":
        return
    user_id = message.from_user.id
    username = message.text
    channel_username1 = '@CerenyTeam'
    channel_username2 = '@Bot4Chan'
    
    if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
            	bot.send_chat_action(message.chat.id, 'typing')
            	time.sleep(0.1)
            	bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
            	return
            
    ban_info = get_ban_info(user_id)
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(0.1)
    if ban_info:
        _, sebep, bitis_tarihi = ban_info
        bot.reply_to(message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için Hesabın Engellendi*\n┃*📨 Sebep*: `{sebep}`\n┃*🕓 Bitiş Tarihi:* `{bitis_tarihi}`\n\n┃*/itiraz Komutunu Kullanarak İtiraz Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")
        return
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
    if not re.match("^[a-zA-Z0-9_]*$", username):
        bot.send_message(user_id, "*Lütfen Geçerli Bir Kullanıcı Adı Girin Özel Parametre içermeyecek şekilde girin!*", parse_mode="Markdown")
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
    elif is_username_taken(username):
        bot.send_message(user_id, "*🚫 Kullanıcı Adı önceden alınmış. Lütfen farklı bir kullanıcı Adı girin!*", parse_mode="Markdown")
    else:
            	bot.send_chat_action(message.chat.id, 'typing')
            	time.sleep(0.1)
            	bot.send_message(user_id, "*🔑 Şifre Belirleyin:*", parse_mode="Markdown")
            	bot.register_next_step_handler_by_chat_id(user_id, process_password_step, username)




def process_password_step(message, username):
    user_id = message.from_user.id
    password = message.text
    channel_username1 = '@CerenyTeam'
    channel_username2 = '@Bot4Chan'
    
    if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
        return

    ban_info = get_ban_info(user_id)
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(0.1)
    if ban_info:
        _, sebep, bitis_tarihi = ban_info
        bot.reply_to(message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için Hesabın Engellendi*\n┃*📨 Sebep*: `{sebep}`\n┃*🕓 Bitiş Tarihi:* `{bitis_tarihi}`\n\n┃*/itiraz Komutunu Kullanarak İtiraz Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")
        return

    add_user(user_id, username, password)
    bot.send_message(user_id, "*🔓 Kayıt Başarılı! /start yazarak Giriş Yap Buttonuna Basarak Giriş Yapabilirsiniz!*", parse_mode="Markdown")



def process_login_username_step(message):
    user_id = message.from_user.id
    username = message.text
    channel_username1 = '@CerenyTeam'
    channel_username2 = '@Bot4Chan'
    
    if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
            	bot.send_chat_action(message.chat.id, 'typing')
            	time.sleep(0.1)
            	bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
            	return
            	
    ban_info = get_ban_info(user_id)
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(0.1)
    if ban_info:
        _, sebep, bitis_tarihi = ban_info
        bot.reply_to(message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için Hesabın Engellendi*\n┃*📨 Sebep*: `{sebep}`\n┃*🕓 Bitiş Tarihi:* `{bitis_tarihi}`\n\n┃*/itiraz Komutunu Kullanarak İtiraz Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")
        return
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
    if is_username_taken(username):
        bot.send_message(user_id, "*🔑 Şifre Girin:*", parse_mode="Markdown")
        bot.register_next_step_handler_by_chat_id(user_id, process_login_password_step, username)
    else:
            	bot.send_chat_action(message.chat.id, 'typing')
            	time.sleep(0.1)
            	bot.send_message(user_id, "*🧍 Kullanıcı Adı Yanlış!*", parse_mode="Markdown")



def process_login_password_step(message, username):
    user_id = message.from_user.id
    password = message.text
    random_messages = ['Jitemin Şuanki Coderi 16 yaşındadır.', 'Jitemin Alt Yapı Yapım Süresi 5 Hafta sürmüştür.', 'Jitemin Alt Yapı Yapım Süresi 5 Hafta sürmüştür.', 'Jitem Her Geçen Gün daha çok Gelişiyor ve Gelişmeye devam ediyor!', 'Jitemin Toplam Admin Sayısı 2. dir']
    selected_message = random.choice(random_messages)
    first_name = message.from_user.first_name
    query_count = get_query_count()
    tz_Turkey = pytz.timezone('Europe/Istanbul')
    saat = datetime.now(tz_Turkey).strftime('%H:%M:%S')
    last_registered_user = get_last_registered_user()

    if last_registered_user:
        last_registered_username = last_registered_user[2]
        now = datetime.now(tz_Turkey)
        current_hour = now.hour
        if 6 <= current_hour < 12:
            greeting = "İyi Sabahlar"
        elif 12 <= current_hour < 18:
            greeting = "İyi Öğleler"
        elif 18 <= current_hour < 24 or 0 <= current_hour < 6:
            greeting = "İyi Akşamlar"
        else:
            greeting = "İyi Geceler"

        channel_username1 = '@CerenyTeam'
        channel_username2 = '@Bot4Chan'

        if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(0.1)
            bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
            return

    ban_info = get_ban_info(user_id)
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(0.1)
    if ban_info:
        _, sebep, bitis_tarihi = ban_info
        bot.reply_to(message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için Hesabın Engellendi*\n┃*📨 Sebep*: `{sebep}`\n┃*🕓 Bitiş Tarihi:* `{bitis_tarihi}`\n\n┃*/itiraz Komutunu Kullanarak İtiraz Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")
        return

    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(0.1)
    if check_credentials(username, password):
        bot.send_message(user_id, f"*{greeting}, {first_name}👋!* (`{user_id}`)\n\n📚 *Komutlar Menüsüne Hoş geldin!*\n\n*📥 Toplam Sorgu Sayısı: {query_count}*\n*🧍 Son Kullanıcı:* `{last_registered_username}`\n*🎭 Üyelik Türü:* `Freemium`\n*⏳ Bitiş Tarihi: ∞*\n\n*❓ Biliyor Muydunuz?*: *{selected_message}*\n\n📣 *Duyuru:* `🥷 İfşala Geç Paşam`\n\n*Sistem • Komutları*\n*/cikisyap • Hesaptan Çıkış Yapar!*\n*/komutlar • Komutlar Listesini Verir*\n*/itiraz • Ban Yediğiniz Zaman İtiraz Edebilirsiniz*\n*/destek • Destek Talebi Oluşturur*\n\n*👪 Nüfus Ve Vatandaşlık İşleri • BÖLÜMÜ*\n*/sorgu • Ad Soyad'dan Kişinin Bilgilerini Verir* (`Free`)\n*/adres  •T.C'den Kişinin Adresini Verir* (`Free`)\n*/kizlik • T.C'den Kişinin Kızlık Soyadını Verir* (`Free`)\n*/ailepro • T.C'den Kişinin Aile Bilgilerini Verir* (`Pro`) (`Free`)\n*/aile • T.C'den Kişinin Aile Bilgilerini Verir* (`Free`)\n*/sulale • T.C'den Kişinin Sülale Bilgilerini Verir* (`Free`)\n*/medeni • T.C'den Kişinin Medeni Halini Verir* (`Free`)\n*/tcpro • T.C'den Kişinin Detaylı Bilgilerini Verir* (`Free`)\n*/tckn • T.C'den Kişinin Bilgilerini Verir* (`Free`)\n*/tcplaka • T.C'den Kişiye Yazılan Ceza Verir* (`Free`)\n*/plaka • Plaka'dan Ceza Bilgileri Verir* (`Free`)\n*/haciz • T.C'den Kişinin Haciz Bilgilerini Verir* (`Free`)\n*/iban • IBAN'dan İbana Ait Bilgileri Verir* (`Free`)\n*/ihbar • Adres'e ihbar Basar* (`Free`)\n\n*📱 Telefon Mobil İletişim Sistemi • BÖLÜMÜ*\n*/gsmtc • GSM'den T.C Verir* (`Free`)\n*/tcgsm • T.C'den GSM Verir* (`Free`)\n*/sms • GSM'ye Sms Saldırısı Yapar* (`Free`)\n*/operator • GSM'den Operatör Verir* (`Free`)\n\n*🏫 Millî Eğitim Bakanlığı • BÖLÜMÜ*\n*/vesika • T.C'den Kişinin E-okul Vesika Verir* (`Free`)\n\n*🎉 Eğlence • BÖLÜMÜ*\n*/index • URL'dan Sitenin indexini Verir* (`Free`)\n*/yaz Girilen Mesajı Deftere yazar* (`Free`)\n*/am • T.C'den Kişinin Am Vesika Verir* (`+18 içerir`) (`Free`)\n*/penis • T.C'den Penis CM Verir* (`Free`)\n\n*JİTEM © Tüm Hakları Saklıdır. Gizlilik, Kullanım ve Telif Hakları bildiriminde belirtilen kurallar çerçevesinde hizmet sunulmaktadır.*\n\n*Komutlar Hakkında Bilgi almak için*\n`/yardim KomutAdı` *girin.*\n\n`Free`: *Freemium Temsil Eder.*\n`Pre`: *Premium Temsil Eder.*", parse_mode="Markdown")
        add_login_user(user_id)
    else:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.send_message(user_id, "*🔐 Şifre Yanlış!*", parse_mode="Markdown")




@bot.message_handler(commands=['komutlar'])
def send_welcome(message):

    user_id = message.from_user.id
    random_messages = ['Jitemin Şuanki Coderi 16 yaşındadır.', 'Jitemin Alt Yapı Yapım Süresi 5 Hafta sürmüştür.', 'Jitemin Alt Yapı Yapım Süresi 5 Hafta sürmüştür.', 'Jitem Her Geçen Gün daha çok Gelişiyor ve Gelişmeye devam ediyor!', 'Jitemin Toplam Admin Sayısı 2. dir']
    selected_message = random.choice(random_messages)
    first_name = message.from_user.first_name
    query_count = get_query_count()
    tz_Turkey = pytz.timezone('Europe/Istanbul')
    saat = datetime.now(tz_Turkey).strftime('%H:%M:%S')
    last_registered_user = get_last_registered_user()

    if last_registered_user:
        last_registered_username = last_registered_user[2]
        now = datetime.now(tz_Turkey)
        current_hour = now.hour
        if 6 <= current_hour < 12:
            greeting = "İyi Sabahlar"
        elif 12 <= current_hour < 18:
            greeting = "İyi Öğleler"
        elif 18 <= current_hour < 24 or 0 <= current_hour < 6:
            greeting = "İyi Akşamlar"
        else:
            greeting = "İyi Geceler"

        channel_username1 = '@CerenyTeam'
        channel_username2 = '@Bot4Chan'

        if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(0.1)
            bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
            return

    ban_info = get_ban_info(user_id)
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(0.1)
    if ban_info:
        _, sebep, bitis_tarihi = ban_info
        bot.reply_to(message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için Hesabın Engellendi*\n┃*📨 Sebep*: `{sebep}`\n┃*🕓 Bitiş Tarihi:* `{bitis_tarihi}`\n\n┃*/itiraz Komutunu Kullanarak İtiraz Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")
        return
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        if not is_user_logged_in(user_id):
            bot.send_message(user_id, "*🚫 Üzgünüm, önce giriş yapmanız gerekiyor!*", parse_mode="Markdown")
            return
            
    if is_user_registered(user_id):
        if is_user_logged_in(user_id):
        	bot.reply_to(message, f"*{greeting}, {first_name}👋!* (`{user_id}`)\n\n📚 *Komutlar Menüsüne Hoş geldin!*\n\n*📥 Toplam Sorgu Sayısı: {query_count}*\n*🧍 Son Kullanıcı:* `{last_registered_username}`\n*🎭 Üyelik Türü:* `Freemium`\n*⏳ Bitiş Tarihi: ∞*\n\n*❓ Biliyor Muydunuz?*: *{selected_message}*\n\n📣 *Duyuru:* `🥷 İfşala Geç Paşam`\n\n*Sistem • Komutları*\n*/cikisyap • Hesaptan Çıkış Yapar!*\n*/komutlar • Komutlar Listesini Verir*\n*/itiraz • Ban Yediğiniz Zaman İtiraz Edebilirsiniz*\n*/destek • Destek Talebi Oluşturur*\n\n*👪 Nüfus Ve Vatandaşlık İşleri • BÖLÜMÜ*\n*/sorgu • Ad Soyad'dan Kişinin Bilgilerini Verir* (`Free`)\n*/adres  •T.C'den Kişinin Adresini Verir* (`Free`)\n*/kizlik • T.C'den Kişinin Kızlık Soyadını Verir* (`Free`)\n*/ailepro • T.C'den Kişinin Aile Bilgilerini Verir* (`Pro`) (`Free`)\n*/aile • T.C'den Kişinin Aile Bilgilerini Verir* (`Free`)\n*/sulale • T.C'den Kişinin Sülale Bilgilerini Verir* (`Free`)\n*/medeni • T.C'den Kişinin Medeni Halini Verir* (`Free`)\n*/tcpro • T.C'den Kişinin Detaylı Bilgilerini Verir* (`Free`)\n*/tckn • T.C'den Kişinin Bilgilerini Verir* (`Free`)\n*/tcplaka • T.C'den Kişiye Yazılan Ceza Verir* (`Free`)\n*/plaka • Plaka'dan Ceza Bilgileri Verir* (`Free`)\n*/haciz • T.C'den Kişinin Haciz Bilgilerini Verir* (`Free`)\n*/iban • IBAN'dan İbana Ait Bilgileri Verir* (`Free`)\n*/ihbar • Adres'e ihbar Basar* (`Free`)\n\n*📱 Telefon Mobil İletişim Sistemi • BÖLÜMÜ*\n*/gsmtc • GSM'den T.C Verir* (`Free`)\n*/tcgsm • T.C'den GSM Verir* (`Free`)\n*/sms • GSM'ye Sms Saldırısı Yapar* (`Free`)\n*/operator • GSM'den Operatör Verir* (`Free`)\n\n*🏫 Millî Eğitim Bakanlığı • BÖLÜMÜ*\n*/vesika • T.C'den Kişinin E-okul Vesika Verir* (`Free`)\n\n*🎉 Eğlence • BÖLÜMÜ*\n*/index • URL'dan Sitenin indexini Verir* (`Free`)\n*/yaz Girilen Mesajı Deftere yazar* (`Free`)\n*/am • T.C'den Kişinin Am Vesika Verir* (`+18 içerir`) (`Free`)\n*/penis • T.C'den Penis CM Verir* (`Free`)\n\n*JİTEM © Tüm Hakları Saklıdır. Gizlilik, Kullanım ve Telif Hakları bildiriminde belirtilen kurallar çerçevesinde hizmet sunulmaktadır.*\n\n*Komutlar Hakkında Bilgi almak için*\n`/yardim KomutAdı` *girin.*\n\n`Free`: *Freemium Temsil Eder.*\n`Pre`: *Premium Temsil Eder.*", parse_mode="Markdown")





message_permission_count = 1

@bot.message_handler(commands=['itiraz'])
def send_message(message):
    if message.chat.type != "private":
        return
    user_id = message.from_user.id
    global message_permission_count
    channel_username1 = '@CerenyTeam'
    channel_username2 = '@Bot4Chan'
    
    if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
            	bot.send_chat_action(message.chat.id, 'typing')
            	time.sleep(0.1)
            	bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
            	return
            	bot.send_chat_action(message.chat.id, 'typing')
            	time.sleep(0.1)
    if not is_user_logged_in(user_id):
            bot.send_message(user_id, "*🚫 Üzgünüm, önce giriş yapmanız gerekiyor!*", parse_mode="Markdown")
            return

    try:
        msg = message.text.split(' ', 1)[1]
    except IndexError:
            	bot.send_chat_action(message.chat.id, 'typing')
            	time.sleep(0.1)
            	bot.reply_to(message, "*Lütfen bir mesaj girin\nÖrnek: /itiraz Mesaj*", parse_mode="Markdown")
            	return


    if message_permission_count > 0:
            	bot.send_chat_action(message.chat.id, 'typing')
            	time.sleep(0.1)
            	bot.send_message(-1002122807954, f"*İtiraz Mesajı:* `{msg}`\n\n*Kullanıcı Adı: {message.from_user.first_name}*\n*Kullanıcı ID:* `{message.from_user.id}`\n\n*Cevaplamak için* `/cevapla ID Mesaj Girin!`", parse_mode="Markdown")
            	bot.send_chat_action(message.chat.id, 'typing')
            	time.sleep(0.1)
            	bot.reply_to(message, "*İtirazınız, gönderildi!.\nYetkililer Tarafından incelenip Geri dönüş yapılacaktır!*", parse_mode="Markdown")
            	
            	message_permission_count -= 1
    else:
            	bot.send_chat_action(message.chat.id, 'typing')
            	time.sleep(0.1)
            	bot.reply_to(message, "*Zaten İtiraz Etmişsiniz!\nİlgin için teşşekürler. İtirazınız Hayla Bekleme Listesinde.*", parse_mode="Markdown")





def get_ban_info(user_id):
    with sqlite3.connect("ban.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bans WHERE user_id = ? AND end_date > ?", (user_id, datetime.now()))
        return cursor.fetchone()



@bot.message_handler(commands=['cikisyap'])
def handle_logout(message):
    if message.chat.type != "private":
        return

    user_id = message.from_user.id
    channel_username1 = '@CerenyTeam'
    channel_username2 = '@Bot4Chan'
    
    if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
            	bot.send_chat_action(message.chat.id, 'typing')
            	time.sleep(0.1)
            	bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
            	return
                
    user_id = message.from_user.id
    ban_info = get_ban_info(user_id)
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(0.1)
    if ban_info:
        _, sebep, bitis_tarihi = ban_info
        bot.reply_to(message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için Hesabın ┃Engellendi*\n┃*📨 Sebep*: `{sebep}`\n┃*🕓 Bitiş Tarihi:* `{bitis_tarihi}`\n┃\n┃*/itiraz Komutunu Kullanarak İtiraz ┃Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")
        return
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
    if is_user_logged_in(user_id):
        remove_login_user(user_id)
        bot.send_message(user_id, "*Çıkış Yapıldı!*", parse_mode="Markdown")
    else:
            	bot.send_chat_action(message.chat.id, 'typing')
            	time.sleep(0.1)
            	bot.send_message(user_id, "*Zaten, çıkış yapmışsınız!*", parse_mode="Markdown")

    
    remove_user_id(user_id)

def remove_user_id(user_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM logged_in_users WHERE user_id = ?', (user_id,))
        conn.commit()




def is_user_registered(user_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
        return cursor.fetchone() is not None

def is_username_taken(username):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        return cursor.fetchone() is not None

def add_user(user_id, username, password):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (user_id, username, password) VALUES (?, ?, ?)', (user_id, username, password))
        conn.commit()

def check_credentials(username, password):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        return cursor.fetchone() is not None

def add_login_user(user_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO logged_in_users (user_id) VALUES (?)', (user_id,))
        conn.commit()

def is_user_logged_in(user_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM logged_in_users WHERE user_id = ?', (user_id,))
        return cursor.fetchone() is not None

def remove_login_user(user_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM logged_in_users WHERE user_id = ?', (user_id,))
        conn.commit()



@bot.message_handler(commands=['tcndhddnkn'])
def tckn(message):
    if message.chat.type != "private":
        return

    user_id = message.from_user.id
    channel_username1 = '@CerenyTeam'
    channel_username2 = '@Bot4Chan'
    
    if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
        return
                
    user_id = message.from_user.id
    ban_info = get_ban_info(user_id)
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(0.1)
    if ban_info:
        _, sebep, bitis_tarihi = ban_info
        bot.reply_to(message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için Hesabın ┃Engellendi*\n┃*📨 Sebep*: `{sebep}`\n┃*🕓 Bitiş Tarihi:* `{bitis_tarihi}`\n┃\n┃*/itiraz Komutunu Kullanarak İtiraz ┃Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")
        return

    if not is_user_logged_in(user_id):
        bot.send_message(user_id, "*🚫 Üzgünüm, önce /start komutu ile giriş yapmanız gerekiyor!*", parse_mode="Markdown")
        return
    
    tc = message.text.split()[1] if len(message.text.split()) > 1 else None
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(0.1)
    if not tc:
        bot.reply_to(message, '*⚠️ Lütfen Geçerli Bir T.C Kimlik Numarası girin!\n\nÖrnek:* `/tckn 11111111110`', parse_mode='Markdown')
        return

    try:
        
        api_url = f"http://20.121.61.198/orj/tc/api.php?tc={tc}"
        response = requests.get(api_url)
        response.raise_for_status()

       
        data = response.json()
        if not data or data[0]['ADI'] is None:
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(0.1)
            bot.reply_to(message, '⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*', parse_mode='Markdown')
            return
        result_text = (
            f"╭─━━━━━━━━━━━━─╮\n┃*T.C*.: `{data[0]['TC']}`\n"
            f"┃*Adı*: `{data[0]['ADI'] or 'Bulunamadı'}`\n"
            f"┃*Soyadı:* `{data[0]['SOYADI'] or 'Bulunamadı'}`\n"
            f"┃*Doğum Tarihi:* `{data[0]['DOGUMTARIHI'] or 'Bulunamadı'}`\n"
            f"┃*Nüfus İli:* `{data[0]['NUFUSIL'] or 'Bulunamadı'}`\n"
            f"┃*Nüfus İlçesi:* `{data[0]['NUFUSILCE'] or 'Bulunamadı'}`\n"
            f"┃*Anne Adı:* `{data[0]['ANNEADI'] or 'Bulunamadı'}`\n"
            f"┃*Anne T.C.*: `{data[0]['ANNETC'] or 'Bulunamadı'}`\n"
            f"┃*Baba Adı:* `{data[0]['BABAADI'] or 'Bulunamadı'}`\n"
            f"┃*Baba T.C*.: `{data[0]['BABATC'] or 'Bulunamadı'}`\n"
            f"┃*Uyruk:* `{data[0]['UYRUK'] or 'Bulunamadı'}`\n╰─━━━━━━━━━━━━─╯"
        )
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, result_text, parse_mode='Markdown')
        increment_query_count()
    except requests.exceptions.HTTPError as errh:
        bot.reply_to(message, f'Hata! HTTP Error: {errh}')

    except requests.exceptions.ConnectionError as errc:
        bot.reply_to(message, f'Hata! Bağlantı Hatası: {errc}')

    except requests.exceptions.Timeout as errt:
        bot.reply_to(message, f'Hata! Zaman Aşımı Hatası: {errt}')

    except requests.exceptions.RequestException as err:
            	bot.send_chat_action(message.chat.id, 'typing')
            	time.sleep(0.1)
            	bot.reply_to(message, f'Hata! Genel Hata: {err}')

    except Exception as e:
            	bot.send_chat_action(message.chat.id, 'typing')
            	time.sleep(0.1)
            	bot.reply_to(message, f'⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*', parse_mode='Markdown')



@bot.message_handler(commands=['tckn'])
def tckn(message):
    if message.chat.type != "private":
        return

    user_id = message.from_user.id
    channel_username1 = '@CerenyTeam'
    channel_username2 = '@Bot4Chan'
    
    if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
            	bot.send_chat_action(message.chat.id, 'typing')
            	time.sleep(0.1)
            	bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
            	return
                
    user_id = message.from_user.id
    ban_info = get_ban_info(user_id)
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(0.1)
    if ban_info:
        _, sebep, bitis_tarihi = ban_info
        bot.reply_to(message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için Hesabın ┃Engellendi*\n┃*📨 Sebep*: `{sebep}`\n┃*🕓 Bitiş Tarihi:* `{bitis_tarihi}`\n┃\n┃*/itiraz Komutunu Kullanarak İtiraz ┃Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")
        return
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
    if not is_user_logged_in(user_id):
            bot.send_message(user_id, "*🚫 Üzgünüm, önce /start komutu ile giriş yapmanız gerekiyor!*", parse_mode="Markdown")
            return
    # Kullanıcının girdiği T.C. numarasını al
    tc = message.text.split()[1] if len(message.text.split()) > 1 else None
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(0.1)
    if not tc:
        bot.reply_to(message, '*⚠️ Lütfen Geçerli Bir T.C Kimlik Numarası girin!\n\nÖrnek:* `/tckn 11111111110`', parse_mode='Markdown')
        return

    try:
        
        api_url = f"http://20.121.61.198/orj/tc/api.php?tc={tc}"
        response = requests.get(api_url)
        response.raise_for_status()

        
        data = response.json()
        if not data:
            	bot.send_chat_action(message.chat.id, 'typing')
            	time.sleep(0.1)
            	bot.reply_to(message, '⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*', parse_mode='Markdown')
            	return
        result_text = (
            f"╭─━━━━━━━━━━━━─╮\n┃*T.C*.: `{data[0]['TC']}`\n"
            f"┃*Adı*: `{data[0]['ADI']}`\n"
            f"┃*Soyadı:* `{data[0]['SOYADI']}`\n"
            f"┃*Doğum Tarihi:* `{data[0]['DOGUMTARIHI']}`\n"
            f"┃*Nüfus İli:* `{data[0]['NUFUSIL']}`\n"
            f"┃*Nüfus İlçesi:* `{data[0]['NUFUSILCE']}`\n"
            f"┃*Anne Adı:* `{data[0]['ANNEADI']}`\n"
            f"┃*Anne T.C.*: `{data[0]['ANNETC']}`\n"
            f"┃*Baba Adı:* `{data[0]['BABAADI']}`\n"
            f"┃*Baba T.C*.: `{data[0]['BABATC']}`\n"
            f"┃*Uyruk:* `{data[0]['UYRUK']}`\n╰─━━━━━━━━━━━━─╯"
        )
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, result_text, parse_mode='Markdown')
        increment_query_count()
    except requests.exceptions.HTTPError as errh:
        bot.reply_to(message, f'Hata! HTTP Error: {errh}')

    except requests.exceptions.ConnectionError as errc:
        bot.reply_to(message, f'Hata! Bağlantı Hatası: {errc}')

    except requests.exceptions.Timeout as errt:
        bot.reply_to(message, f'Hata! Zaman Aşımı Hatası: {errt}')

    except requests.exceptions.RequestException as err:
            	bot.send_chat_action(message.chat.id, 'typing')
            	time.sleep(0.1)
            	bot.reply_to(message, f'Hata! Genel Hata: {err}')

    except Exception as e:
            	bot.send_chat_action(message.chat.id, 'typing')
            	time.sleep(0.1)
            	bot.reply_to(message, f'⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*', parse_mode='Markdown')



@bot.message_handler(commands=['vesikbbba'])
def vesika(message):
    if message.chat.type != "private":
        return

    user_id = message.from_user.id
    channel_username1 = '@CerenyTeam'
    channel_username2 = '@Bot4Chan'
    
    if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(1)
        bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
        return
                
    user_id = message.from_user.id
    ban_info = get_ban_info(user_id)
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(1)
    if ban_info:
        _, sebep, bitis_tarihi = ban_info
        bot.reply_to(message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için Hesabın ┃Engellendi*\n┃*📨 Sebep*: `{sebep}`\n┃*🕓 Bitiş Tarihi:* `{bitis_tarihi}`\n┃\n┃*/itiraz Komutunu Kullanarak İtiraz ┃Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")
        return

    if not is_user_logged_in(user_id):
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.send_message(user_id, "*🚫 Üzgünüm, önce /start komutu ile giriş yapmanız gerekiyor!*", parse_mode="Markdown")
        return
        
    try:
        command, tc = message.text.split()
        if len(tc) != 11:
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(0.1)
            bot.reply_to(message, "*⚠️ Lütfen 11 Haneli T.C. Kimlik Numarası girin.*", parse_mode='Markdown')
            return
        
        api_url = f"http://20.121.61.198/orj/vesikalrx/api.php?tc={tc}"
        response_data = fetch_data_from_api(api_url)

        if tc == "22222222220":
            with open("vesika.png", "rb") as photo:
                bot.send_chat_action(message.chat.id, 'typing')
                time.sleep(0.1)
                bot.send_photo(message.chat.id, photo, caption="╭─━━━━━━━━━━━━━─╮\n┃*T.C Kimlik No:* `22222222220`\n┃*Adı:* `Lorax`\n┃*Soyadı*: `LoraxAmk`\n┃*Okul No:* `11111`\n╰─━━━━━━━━━━━━━─╯", parse_mode='Markdown')
                increment_query_count()
                return
        if tc == "11111111110":
            with open("vesika.png", "rb") as photo:
                bot.send_chat_action(message.chat.id, 'typing')
                time.sleep(0.1)
                bot.send_photo(message.chat.id, photo, caption="╭─━━━━━━━━━━━━━─╮\n┃*T.C Kimlik No:* `11111111110`\n┃*Adı:* `ABDULSELAM`\n┃*Soyadı*: `DENİZ`\n┃*Okul No:* `2017857`\n╰─━━━━━━━━━━━━━─╯", parse_mode='Markdown')
                increment_query_count()
                return
        if response_data:
            tc = response_data.get("tc", "Bilgi Yok")
            ad = response_data.get("ad", "Bilgi Yok")
            soyad = response_data.get("soyad", "Bilgi Yok")
            okulno = response_data.get("okulno", "Bilgi Yok")
            vesika_base64 = response_data.get("image", "")
            
            if vesika_base64:
                image_data = base64.b64decode(vesika_base64)
                image = BytesIO(image_data)
                bot.send_chat_action(message.chat.id, 'typing')
                time.sleep(0.1)
                bot.send_photo(message.chat.id, photo=image, caption=f"╭─━━━━━━━━━━━━━─╮\n┃*T.C Kimlik No:* `{tc}`\n┃*Adı:* `{ad}`\n┃*Soyadı*: `{soyad}`\n┃*Okul No:* `{okulno}`\n╰─━━━━━━━━━━━━━─╯", parse_mode='Markdown')
                increment_query_count()
            else:
                bot.send_chat_action(message.chat.id, 'typing')
                time.sleep(0.1)
                bot.reply_to(message, "⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*", parse_mode='Markdown')
        else:
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(0.1)
            bot.reply_to(message, "⚠️ *Veri alınamadı. Daha sonra tekrar deneyin*.", parse_mode='Markdown')
        
    except ValueError:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, "*⚠️ Lütfen Geçerli Bir T.C Kimlik Numarası girin!\n\nÖrnek:* `/vesika 11111111110`", parse_mode='Markdown')





@bot.message_handler(commands=['kizlik'])
def kizlik(message):
    if message.chat.type != "private":
        return

    user_id = message.from_user.id
    channel_username1 = '@CerenyTeam'
    channel_username2 = '@Bot4Chan'
    
    if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
        bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
        return

    user_id = message.from_user.id
    ban_info = get_ban_info(user_id)

    if ban_info:
        _, sebep, bitis_tarihi = ban_info
        bot.reply_to(message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için Hesabın ┃Engellendi*\n┃*📨 Sebep*: `{sebep}`\n┃*🕓 Bitiş Tarihi:* `{bitis_tarihi}`\n┃\n┃*/itiraz Komutunu Kullanarak İtiraz ┃Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")
        return

    if not is_user_logged_in(user_id):
        bot.send_message(user_id, "*🚫 Üzgünüm, önce /start komutu ile giriş yapmanız gerekiyor!*", parse_mode="Markdown")
        return

   
    tc = message.text.split()[1] if len(message.text.split()) > 1 else None

    if not tc:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, '*⚠️ Lütfen Geçerli Bir T.C Kimlik Numarası girin!\n\nÖrnek:* `/kizlik 11111111110`', parse_mode='Markdown')
        return

    try:
        
        api_url = f"http://20.121.61.198/orj/kizlik/api.php?tc={tc}"
        response = requests.get(api_url)
        response.raise_for_status()

      
        data = response.json()
        if not data:
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(0.1)
            bot.reply_to(message, '⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*', parse_mode='Markdown')
            return

        result_text = f"╭─━━━━━━━━━━━━─╮\n┃*T.C*.: `{data['tc']}`\n┃*Kızlık Soyadı:* `{data['kizliksoyadi']}`\n╰─━━━━━━━━━━━━─╯"
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, result_text, parse_mode='Markdown')
        increment_query_count()

    except requests.exceptions.HTTPError as errh:
        bot.reply_to(message, f'Hata! HTTP Error: {errh}')

    except requests.exceptions.ConnectionError as errc:
        bot.reply_to(message, f'Hata! Bağlantı Hatası: {errc}')

    except requests.exceptions.Timeout as errt:
        bot.reply_to(message, f'Hata! Zaman Aşımı Hatası: {errt}')

    except requests.exceptions.RequestException as err:
        bot.reply_to(message, f'Hata! Genel Hata: {err}')

    except Exception as e:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, f'⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*', parse_mode='Markdown')





import os


@bot.message_handler(commands=['am'])
def send_random_photo_with_caption(message):
    if message.chat.type != "private":
        return

    user_id = message.from_user.id
    channel_username1 = '@CerenyTeam'
    channel_username2 = '@Bot4Chan'
    
    if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
        bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
        return

    user_id = message.from_user.id
    ban_info = get_ban_info(user_id)

    if ban_info:
        _, sebep, bitis_tarihi = ban_info
        bot.reply_to(message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için Hesabın ┃Engellendi*\n┃*📨 Sebep*: `{sebep}`\n┃*🕓 Bitiş Tarihi:* `{bitis_tarihi}`\n┃\n┃*/itiraz Komutunu Kullanarak İtiraz ┃Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")
        return

    if not is_user_logged_in(user_id):
        bot.send_message(user_id, "*🚫 Üzgünüm, önce /start komutu ile giriş yapmanız gerekiyor!*", parse_mode="Markdown")
        return

    if len(message.text.split()) != 2 or not message.text.split()[1].isdigit() or len(message.text.split()[1]) != 11:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.send_message(message.chat.id, "*⚠️ Lütfen Geçerli Bir T.C Kimlik Numarası girin!\n\nÖrnek:* `/am 11111111110`", parse_mode='Markdown')
        return

    photo_files = ['beyazam.png', 'karaam.png', 'pembeam.png']
    selected_photo = random.choice(photo_files)
    photo_path = os.path.join('', selected_photo)

    
    caption = ""
    if selected_photo == 'beyazam.png':
        caption = "*Bunu Kaçırma sakın Beyaz En sevdiğim!.*"
    elif selected_photo == 'karaam.png':
        caption = "*Bunu Siktir Et amk amına Bak zenciler sikmiş sanki amı buruşmuş şuna bak Kara Amı var!.*"
    elif selected_photo == 'pembeam.png':
        caption = "*Bunu Hiç Kaçırma Pembe Am Çok Severim!.*"

    with open(photo_path, 'rb') as photo:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.send_photo(message.chat.id, photo, caption, parse_mode='Markdown')






import os


@bot.message_handler(commands=['index'])
def index(message):
    if message.chat.type != "private":
        return

    user_id = message.from_user.id
    channel_username1 = '@CerenyTeam'
    channel_username2 = '@Bot4Chan'
    
    if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
        bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
        return

    user_id = message.from_user.id
    ban_info = get_ban_info(user_id)

    if ban_info:
        _, sebep, bitis_tarihi = ban_info
        bot.reply_to(message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için Hesabın ┃Engellendi*\n┃*📨 Sebep*: `{sebep}`\n┃*🕓 Bitiş Tarihi:* `{bitis_tarihi}`\n┃\n┃*/itiraz Komutunu Kullanarak İtiraz ┃Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")
        return

    if not is_user_logged_in(user_id):
        bot.send_message(user_id, "*🚫 Üzgünüm, önce /start komutu ile giriş yapmanız gerekiyor!*", parse_mode="Markdown")
        return

    try:
        site_url = message.text.split(maxsplit=1)[1]
    except IndexError:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, "*⚠️ Lütfen Geçerli Bir Site URL girin!*\n\n*Örnek:* `/index https://e-okul.meb.gov.tr`", parse_mode="Markdown")
        return

    if not site_url.startswith("http://") and not site_url.startswith("https://"):
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, "*⚠️ Üzgünüm Hatalı URL girdiniz Lütfen geçerli bir URL girin*\n\n*Örnek*: `/index https://e-okul.meb.gov.tr`", parse_mode="Markdown")
        return

    response = requests.get(site_url)

    if response.status_code == 200:
        file_name = "Jitem.html"
        file_content = response.text
        increment_query_count()
        with open(file_name, 'w') as file:
            file.write(file_content)

        with open(file_name, 'rb') as file:
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(0.1)
            bot.send_document(message.chat.id, file)

        os.remove(file_name)
    else:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, "*⚠️ Üzgünüm bu siteye Ait Bir index Çekilemiyor!*", parse_mode='Markdown')



support_channel_id = -1002122807954

@bot.message_handler(commands=['destek'])
def handle_destek(message):
    if message.chat.type != "private":
        return
    user_id = message.from_user.id
    channel_username1 = '@CerenyTeam'
    channel_username2 = '@Bot4Chan'
    
    if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
                bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
                return
                
    user_id = message.from_user.id
    ban_info = get_ban_info(user_id)

    if ban_info:
        _, sebep, bitis_tarihi = ban_info
        bot.reply_to(message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için Hesabın ┃Engellendi*\n┃*📨 Sebep*: `{sebep}`\n┃*🕓 Bitiş Tarihi:* `{bitis_tarihi}`\n┃\n┃*/itiraz Komutunu Kullanarak İtiraz ┃Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")
        return

    if not is_user_logged_in(user_id):
            bot.send_message(user_id, "*🚫 Üzgünüm, önce /start komutu ile giriş yapmanız gerekiyor!*", parse_mode="Markdown")
            return
    user_id = message.from_user.id
    kullanici = f"{message.from_user.first_name} {message.from_user.last_name}" if message.from_user.last_name else message.from_user.first_name
    mesaj = message.text.split(maxsplit=1)
    
    if len(mesaj) > 1:
        mesaj = mesaj[1]
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.send_message(support_channel_id, f"*Destek Talebi Var!\n\nMesaj:* `{mesaj}`\n\n*Kullanıcı: {kullanici}*\n*Kullanıcı ID:* `{user_id}`", parse_mode="Markdown")
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, "*Destek talebiniz alındı. En kısa sürede size dönüş yapılacaktır*.", parse_mode="Markdown")
    else:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, "⚠️ *Lütfen geçerli bir destek mesajı girin.*\n\n*Örnek:* `/destek Merhaba, yardıma ihtiyacım var gibi`.", parse_mode="Markdown")




@bot.message_handler(commands=['penis'])
def penis_size(message):
    if message.chat.type != "private":
        return
    user_id = message.from_user.id
    channel_username1 = '@CerenyTeam'
    channel_username2 = '@Bot4Chan'
    
    if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
                bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
                return
                
    user_id = message.from_user.id
    ban_info = get_ban_info(user_id)

    if ban_info:
        _, sebep, bitis_tarihi = ban_info
        bot.reply_to(message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için Hesabın ┃Engellendi*\n┃*📨 Sebep*: `{sebep}`\n┃*🕓 Bitiş Tarihi:* `{bitis_tarihi}`\n┃\n┃*/itiraz Komutunu Kullanarak İtiraz ┃Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")
        return

    if not is_user_logged_in(user_id):
            bot.send_message(user_id, "*🚫 Üzgünüm, önce /start komutu ile giriş yapmanız gerekiyor!*", parse_mode="Markdown")
            return

    try:
        query = message.text.strip().split(' ')
        if len(query) != 2 or len(query[1]) != 11:
        	bot.send_chat_action(message.chat.id, 'typing')
        	time.sleep(0.1)
        	bot.reply_to(message, "*⚠️ Lütfen Geçerli Bir T.C Kimlik Numarası girin!\n\nÖrnek:* `/penis 11111111110`", parse_mode='Markdown')
        	return
        penis_length = random.choice([6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32])
        penis_unit = 'CM'
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, f"╭─━━━━━━━━━━━━━─╮\n┃*T.C* `{query[1]}`\n┃*Penis Boyutu:* `{penis_length}{penis_unit}`\n╰─━━━━━━━━━━━━━─╯", parse_mode='Markdown')
        increment_query_count()
    except IndexError:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, "*⚠️ Lütfen Geçerli Bir T.C Kimlik Numarası girin!\n\nÖrnek:* `/penis 11111111110`", parse_mode='Markdown')
    except Exception as e:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, f"⚠️ *Bir hata oluştu: Lütfen daha sonra Tekrar deneyin*", parse_mode='Markdown')
        
        
        
        

@bot.message_handler(commands=['burc'])
def burc(message):
    if message.chat.type != "private":
        return

    user_id = message.from_user.id
    channel_username1 = '@CerenyTeam'
    channel_username2 = '@Bot4Chan'
    
    if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
        bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
        return

    user_id = message.from_user.id
    ban_info = get_ban_info(user_id)

    if ban_info:
        _, sebep, bitis_tarihi = ban_info
        bot.reply_to(message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için Hesabın ┃Engellendi*\n┃*📨 Sebep*: `{sebep}`\n┃*🕓 Bitiş Tarihi:* `{bitis_tarihi}`\n┃\n┃*/itiraz Komutunu Kullanarak İtiraz ┃Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")
        return

    if not is_user_logged_in(user_id):
        bot.send_message(user_id, "*🚫 Üzgünüm, önce /start komutu ile giriş yapmanız gerekiyor!*", parse_mode="Markdown")
        return

    
    user_first_name = message.from_user.first_name

    
    tc = message.text.split()[1] if len(message.text.split()) > 1 else None

    if not tc:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(2)
        bot.reply_to(message, '*⚠️ Lütfen Geçerli Bir T.C Kimlik Numarası girin!\n\nÖrnek:* `/burc 11111111110`', parse_mode='Markdown')
        return

    try:
        api_url = f"http://20.121.61.198/orj/burc/api.php?tc={tc}"
        response = requests.get(api_url)
        response.raise_for_status()

        
        data = response.json()
        if not data:
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(0.1)
            bot.reply_to(message, '⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*', parse_mode='Markdown')
            return

        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        result_text = f"╭─━━━━━━━━━━━━─╮\n┃*T.C.*: `{data['tc']}`\n┃*Burç:* `{data['burc']}`\n╰─━━━━━━━━━━━━─╯"
        bot.reply_to(message, result_text, parse_mode='Markdown')
        increment_query_count()
    except requests.exceptions.HTTPError as errh:
        bot.reply_to(message, f'Hata! HTTP Error: {errh}')

    except requests.exceptions.ConnectionError as errc:
        bot.reply_to(message, f'Hata! Bağlantı Hatası: {errc}')

    except requests.exceptions.Timeout as errt:
        bot.reply_to(message, f'Hata! Zaman Aşımı Hatası: {errt}')

    except requests.exceptions.RequestException as err:
        bot.reply_to(message, f'Hata! Genel Hata: {err}')

    except Exception as e:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, f'⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*', parse_mode='Markdown')






@bot.message_handler(commands=['medeni'])
def medeni(message):
    if message.chat.type != "private":
        return

    user_id = message.from_user.id
    channel_username1 = '@CerenyTeam'
    channel_username2 = '@Bot4Chan'
    
    if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
        bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
        return

    user_id = message.from_user.id
    ban_info = get_ban_info(user_id)

    if ban_info:
        _, sebep, bitis_tarihi = ban_info
        bot.reply_to(message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için Hesabın ┃Engellendi*\n┃*📨 Sebep*: `{sebep}`\n┃*🕓 Bitiş Tarihi:* `{bitis_tarihi}`\n┃\n┃*/itiraz Komutunu Kullanarak İtiraz ┃Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")
        return

    if not is_user_logged_in(user_id):
        bot.send_message(user_id, "*🚫 Üzgünüm, önce /start komutu ile giriş yapmanız gerekiyor!*", parse_mode="Markdown")
        return


    user_first_name = message.from_user.first_name

    
    tc = message.text.split()[1] if len(message.text.split()) > 1 else None

    if not tc:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, '*⚠️ Lütfen Geçerli Bir T.C Kimlik Numarası girin!\n\nÖrnek:* `/medeni 11111111110`', parse_mode='Markdown')
        return

    try:

        api_url = f"http://20.121.61.198/orj/medenihal/api.php?tc={tc}"
        response = requests.get(api_url)
        response.raise_for_status()

       
        data = response.json()
        if not data:
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(0.1)
            bot.reply_to(message, '⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*.', parse_mode='Markdown')
            return

        result_text = (
            f"╭─━━━━━━━━━━━━─╮\n┃*T.C.*: `{data['tc']}`\n"
            f"*┃Ad Soyad:* `{data['AdSoyad']}`\n"
            f"*┃Medeni Hal*: `{data['medenihal']}`\n"
            f"*┃GSM*: `{data['gsm']}`\n╰─━━━━━━━━━━━━─╯"
        )
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, result_text, parse_mode='Markdown')
        increment_query_count()
    except requests.exceptions.HTTPError as errh:
        bot.reply_to(message, f'Hata! HTTP Error: {errh}')

    except requests.exceptions.ConnectionError as errc:
        bot.reply_to(message, f'Hata! Bağlantı Hatası: {errc}')

    except requests.exceptions.Timeout as errt:
        bot.reply_to(message, f'Hata! Zaman Aşımı Hatası: {errt}')

    except requests.exceptions.RequestException as err:
        bot.reply_to(message, f'Hata! Genel Hata: {err}')

    except Exception as e:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, f'⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*', parse_mode='Markdown')






@bot.message_handler(commands=['ihbar'])
def ihbar(message):
    if message.chat.type != "private":
        return

    user_id = message.from_user.id
    channel_username1 = '@CerenyTeam'
    channel_username2 = '@Bot4Chan'
    
    if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
        bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
        return

    user_id = message.from_user.id
    ban_info = get_ban_info(user_id)

    if ban_info:
        _, sebep, bitis_tarihi = ban_info
        bot.reply_to(message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için Hesabın ┃Engellendi*\n┃*📨 Sebep*: `{sebep}`\n┃*🕓 Bitiş Tarihi:* `{bitis_tarihi}`\n┃\n┃*/itiraz Komutunu Kullanarak İtiraz ┃Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")
        return

    if not is_user_logged_in(user_id):
        bot.send_message(user_id, "*🚫 Üzgünüm, önce /start komutu ile giriş yapmanız gerekiyor!*", parse_mode="Markdown")
        return

   
    user_first_name = message.from_user.first_name

    adres = message.text.split()[1] if len(message.text.split()) > 1 else None

    if not adres:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, '*⚠️ Lütfen Geçerli Bir Adres girin!\n\nÖrnek:* `/ihbar 100.YIL MAH. 1295 SK. 10/`', parse_mode='Markdown')
        return

    try:

        api_url = f"http://20.121.61.198/orj/fakeihbar/api.php?adres={adres}"
        response = requests.get(api_url)
        response.raise_for_status()

       
        data = response.json()
        if not data['message'].lower() == 'true':
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(0.1)
            bot.reply_to(message, '⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*', parse_mode='Markdown')
            return

        result_text = f"╭─━━━━━━━━━━━━─╮\n┃*Gönderilen İhbar*: `{data['data'][0]['gönderilen']}`\n╰─━━━━━━━━━━━━─╯"
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, result_text, parse_mode='Markdown')
        increment_query_count()
    except requests.exceptions.HTTPError as errh:
        bot.reply_to(message, f'Hata! HTTP Error: {errh}')

    except requests.exceptions.ConnectionError as errc:
        bot.reply_to(message, f'Hata! Bağlantı Hatası: {errc}')

    except requests.exceptions.Timeout as errt:
        bot.reply_to(message, f'Hata! Zaman Aşımı Hatası: {errt}')

    except requests.exceptions.RequestException as err:
        bot.reply_to(message, f'Hata! Genel Hata: {err}')

    except Exception as e:
        bot.reply_to(message, f'*Hata Lütfen Yönetici ile iletişime geçin!*', parse_mode='Markdown')




@bot.message_handler(commands=['iban'])
def iban(message):
    if message.chat.type != "private":
        return

    user_id = message.from_user.id
    channel_username1 = '@CerenyTeam'
    channel_username2 = '@Bot4Chan'
    
    if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
        bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
        return

    user_id = message.from_user.id
    ban_info = get_ban_info(user_id)

    if ban_info:
        _, sebep, bitis_tarihi = ban_info
        bot.reply_to(message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için Hesabın ┃Engellendi*\n┃*📨 Sebep*: `{sebep}`\n┃*🕓 Bitiş Tarihi:* `{bitis_tarihi}`\n┃\n┃*/itiraz Komutunu Kullanarak İtiraz ┃Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")
        return

    if not is_user_logged_in(user_id):
        bot.send_message(user_id, "*🚫 Üzgünüm, önce /start komutu ile giriş yapmanız gerekiyor!*", parse_mode="Markdown")
        return

    # Get the user's first name for the message
    user_first_name = message.from_user.first_name

    # Kullanıcının girdiği IBAN numarasını al
    iban_num = message.text.split()[1] if len(message.text.split()) > 1 else None

    if not iban_num:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, '*⚠️ Lütfen geçerli bir IBAN Numarası girin!.\nÖrnek:* `/iban TR560001002247786851675002`', parse_mode='Markdown')
        return

    try:

        api_url = f"http://20.121.61.198/orj/iban/api.php?iban={iban_num}"
        response = requests.get(api_url)
        response.raise_for_status()


        data = response.json()
        if not data:
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(0.1)
            bot.reply_to(message, '⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*', parse_mode='Markdown')
            return

        result_text = (
            f"╭─━━━━━━━━━━━━─╮\n┃*BANKA Bilgileri*\n"
            f"┃*Banka Adı:* `{data['BANKA']['BankaAdı']}`\n"
            f"┃*Banka Kodu*: `{data['BANKA']['BankaKodu']}`\n"
            f"┃*Swift:* `{data['BANKA']['Swift']}`\n"
            f"┃*Hesap No:* `{data['BANKA']['Hesap No']}`\n\n"
            f"┃*ŞUBE Bilgileri*\n"
            f"┃*Şube Adı:* `{data['ŞUBE']['SubeAd']}`\n"
            f"┃*Şube Kodu:* `{data['ŞUBE']['SubeKodu']}`\n"
            f"┃*Nufüs İl:* `{data['ŞUBE']['İl']}`\n"
            f"┃*Nufüs İlçe:* `{data['ŞUBE']['İlçe']}`\n"
            f"┃*Telefon:* `{data['ŞUBE']['Tel']}`\n"
            f"┃*Fax:* `{data['ŞUBE']['Fax']}`\n"
            f"┃*Adres*: `{data['ŞUBE']['Adres']}`\n╰─━━━━━━━━━━━━─╯"
        )

        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, result_text, parse_mode='Markdown')
        increment_query_count()
    except requests.exceptions.HTTPError as errh:
        bot.reply_to(message, f'Hata! HTTP Error: {errh}')

    except requests.exceptions.ConnectionError as errc:
        bot.reply_to(message, f'Hata! Bağlantı Hatası: {errc}')

    except requests.exceptions.Timeout as errt:
        bot.reply_to(message, f'Hata! Zaman Aşımı Hatası: {errt}')

    except requests.exceptions.RequestException as err:
        bot.reply_to(message, f'Hata! Genel Hata: {err}')

    except Exception as e:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, f'⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*', parse_mode='Markdown')






@bot.message_handler(commands=['operator'])
def operator(message):
    if message.chat.type != "private":
        return

    user_id = message.from_user.id
    channel_username1 = '@CerenyTeam'
    channel_username2 = '@Bot4Chan'
    
    if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
        bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
        return

    user_id = message.from_user.id
    ban_info = get_ban_info(user_id)

    if ban_info:
        _, sebep, bitis_tarihi = ban_info
        bot.reply_to(message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için Hesabın ┃Engellendi*\n┃*📨 Sebep*: `{sebep}`\n┃*🕓 Bitiş Tarihi:* `{bitis_tarihi}`\n┃\n┃*/itiraz Komutunu Kullanarak İtiraz ┃Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")
        return

    if not is_user_logged_in(user_id):
        bot.send_message(user_id, "*🚫 Üzgünüm, önce /start komutu ile giriş yapmanız gerekiyor!*", parse_mode="Markdown")
        return

    user_first_name = message.from_user.first_name

    gsm = message.text.split()[1] if len(message.text.split()) > 1 else None

    if not gsm:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, '*⚠️ Lütfen geçerli bir GSM Numarası girin!.\nÖrnek:* `/operator 5553723339`', parse_mode="Markdown")
        return

    try:

        api_url = f"http://20.121.61.198/orj/operator/api.php?gsm={gsm}"
        response = requests.get(api_url)
        response.raise_for_status()

        
        data = response.json()
        if not data:
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(0.1)
            bot.reply_to(message, '⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*', parse_mode="Markdown")
            return

        result_text = f"╭─━━━━━━━━━━━━─╮\n┃*GSM:* `{data['gsm']}`\n┃*Operatör:* `{data['operator']}`\n╰─━━━━━━━━━━━━─╯"
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, result_text, parse_mode="Markdown")
        increment_query_count()
    except requests.exceptions.HTTPError as errh:
        bot.reply_to(message, f'Hata! HTTP Error: {errh}')

    except requests.exceptions.ConnectionError as errc:
        bot.reply_to(message, f'Hata! Bağlantı Hatası: {errc}')

    except requests.exceptions.Timeout as errt:
        bot.reply_to(message, f'Hata! Zaman Aşımı Hatası: {errt}')

    except requests.exceptions.RequestException as err:
        bot.reply_to(message, f'Hata! Genel Hata: {err}')

    except Exception as e:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(2)
        bot.reply_to(message, f'⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*', parse_mode="Markdown")






@bot.message_handler(commands=['gsmtc'])
def gsmtc(message):
    if message.chat.type != "private":
        return

    user_id = message.from_user.id
    channel_username1 = '@CerenyTeam'
    channel_username2 = '@Bot4Chan'
    
    if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
        bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
        return

    user_id = message.from_user.id
    ban_info = get_ban_info(user_id)

    if ban_info:
        _, sebep, bitis_tarihi = ban_info
        bot.reply_to(message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için Hesabın ┃Engellendi*\n┃*📨 Sebep*: `{sebep}`\n┃*🕓 Bitiş Tarihi:* `{bitis_tarihi}`\n┃\n┃*/itiraz Komutunu Kullanarak İtiraz ┃Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")
        return

    if not is_user_logged_in(user_id):
        bot.send_message(user_id, "*🚫 Üzgünüm, önce /start komutu ile giriş yapmanız gerekiyor!*", parse_mode="Markdown")
        return

    user_first_name = message.from_user.first_name

    gsm = message.text.split()[1] if len(message.text.split()) > 1 else None

    if not gsm:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, '*⚠️ Lütfen geçerli bir GSM Numarası girin!.\nÖrnek:* `/gsmtc 5553723339`', parse_mode="Markdown")
        return

    try:
        api_url = f"http://20.121.61.198/orj/gsm/gsmtc.php?gsm={gsm}"
        response = requests.get(api_url)
        response.raise_for_status()

        data = response.json()
        if not data:
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(0.1)
            bot.reply_to(message, '⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*', parse_mode="Markdown")
            return

        result_text = f"╭─━━━━━━━━━━━━─╮\n┃*Telefon Numarası*: `{data[0]['GSM']}`\n┃*T.C Kimlik Numarası:* `{data[0]['TC']}`\n╰─━━━━━━━━━━━━─╯"
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, result_text, parse_mode="Markdown")
        increment_query_count()
    except requests.exceptions.HTTPError as errh:
        bot.reply_to(message, f'Hata! HTTP Error: {errh}')

    except requests.exceptions.ConnectionError as errc:
        bot.reply_to(message, f'Hata! Bağlantı Hatası: {errc}')

    except requests.exceptions.Timeout as errt:
        bot.reply_to(message, f'Hata! Zaman Aşımı Hatası: {errt}')

    except requests.exceptions.RequestException as err:
        bot.reply_to(message, f'Hata! Genel Hata: {err}')

    except Exception as e:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, f'⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*', parse_mode="Markdown")







@bot.message_handler(commands=['tcgsm'])
def tcgsm(message):
    if message.chat.type != "private":
        return

    user_id = message.from_user.id
    channel_username1 = '@CerenyTeam'
    channel_username2 = '@Bot4Chan'
    
    if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
        bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
        return

    user_id = message.from_user.id
    ban_info = get_ban_info(user_id)

    if ban_info:
        _, sebep, bitis_tarihi = ban_info
        bot.reply_to(message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için Hesabın ┃Engellendi*\n┃*📨 Sebep*: `{sebep}`\n┃*🕓 Bitiş Tarihi:* `{bitis_tarihi}`\n┃\n┃*/itiraz Komutunu Kullanarak İtiraz ┃Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")
        return

    if not is_user_logged_in(user_id):
        bot.send_message(user_id, "*🚫 Üzgünüm, önce /start komutu ile giriş yapmanız gerekiyor!*", parse_mode="Markdown")
        return

    # Get the user's first name for the message
    user_first_name = message.from_user.first_name

    # Kullanıcının girdiği T.C. numarasını al
    tc = message.text.split()[1] if len(message.text.split()) > 1 else None

    if not tc:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, '*⚠️ Lütfen geçerli bir T.C. Kimlik Numarası girin!.\nÖrnek:* `/tcgsm 11111111110`', parse_mode="Markdown")
        return

    try:
        api_url = f"http://20.121.61.198/orj/gsm/tcgsm.php?tc={tc}"
        response = requests.get(api_url)
        response.raise_for_status()

       
        data = response.json()
        if not data or not data[0]:
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(0.1)
            bot.reply_to(message, '⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*', parse_mode="Markdown")
            return

        result_text = f"╭─━━━━━━━━━━━━─╮\n┃*T.C Kimlik Numarası:* `{data[0]['TC']}`\n┃*Telefon Numarası:* `{data[0]['GSM']}`\n╰─━━━━━━━━━━━━─╯"
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, result_text, parse_mode="Markdown")
        increment_query_count()
    except requests.exceptions.HTTPError as errh:
        bot.reply_to(message, f'Hata! HTTP Error: {errh}')

    except requests.exceptions.ConnectionError as errc:
        bot.reply_to(message, f'Hata! Bağlantı Hatası: {errc}')

    except requests.exceptions.Timeout as errt:
        bot.reply_to(message, f'Hata! Zaman Aşımı Hatası: {errt}')

    except requests.exceptions.RequestException as err:
        bot.reply_to(message, f'Hata! Genel Hata: {err}')

    except Exception as e:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, f'⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*', parse_mode="Markdown")





@bot.message_handler(commands=['plaka'])
def plaka(message):
    if message.chat.type != "private":
        return

    user_id = message.from_user.id
    channel_username1 = '@CerenyTeam'
    channel_username2 = '@Bot4Chan'
    
    if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
                bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
                return
                
    user_id = message.from_user.id
    ban_info = get_ban_info(user_id)

    if ban_info:
        _, sebep, bitis_tarihi = ban_info
        bot.reply_to(message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için Hesabın ┃Engellendi*\n┃*📨 Sebep*: `{sebep}`\n┃*🕓 Bitiş Tarihi:* `{bitis_tarihi}`\n┃\n┃*/itiraz Komutunu Kullanarak İtiraz ┃Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")
        return

    if not is_user_logged_in(user_id):
            bot.send_message(user_id, "*🚫 Üzgünüm, önce /start komutu ile giriş yapmanız gerekiyor!*", parse_mode="Markdown")
            return
    # Kullanıcının girdiği plakayı al
    plaka = message.text.split()[1] if len(message.text.split()) > 1 else None

    if not plaka:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(2)
        bot.reply_to(message, '*⚠️ Lütfen geçerli bir Plaka girin!.\nÖrnek:* `/plaka 07EAT94`', parse_mode="Markdown")
        return

    try:
        api_url = f"http://20.121.61.198/orj/plakaceza/api.php?plaka={plaka}"
        response = requests.get(api_url)
        response.raise_for_status()

       
        data = response.json()
        if not data:
        	bot.send_chat_action(message.chat.id, 'typing')
        	time.sleep(0.1)
        	bot.reply_to(message, '⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*', parse_mode="Markdown")
        	return

        result_text = f"╭─━━━━━━━━━━━━─╮\n┃*Plaka*: `{data['plaka']}`\n┃*Borç Türü:* `{data['borcTuru']}`\n┃*İsim Soyisim:* `{data['Isimsoyisim']}`\n┃*T.C.*: `{data['Tc']}`\n┃*Yazılan Ceza:* `{data['YazilanCeza']}`\n┃*Toplam Ceza:* `{data['ToplamCeza']}`\n╰─━━━━━━━━━━━━─╯"
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(2)
        bot.reply_to(message, result_text, parse_mode="Markdown")
        increment_query_count()
    except requests.exceptions.HTTPError as errh:
        bot.reply_to(message, f'Hata! HTTP Error: {errh}')

    except requests.exceptions.ConnectionError as errc:
        bot.reply_to(message, f'Hata! Bağlantı Hatası: {errc}')

    except requests.exceptions.Timeout as errt:
        bot.reply_to(message, f'Hata! Zaman Aşımı Hatası: {errt}')

    except requests.exceptions.RequestException as err:
        bot.reply_to(message, f'Hata! Genel Hata: {err}')

    except Exception as e:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, f'⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*', parse_mode="Markdown")





@bot.message_handler(commands=['tcplaka'])
def plaka(message):
    if message.chat.type != "private":
        return

    user_id = message.from_user.id
    channel_username1 = '@CerenyTeam'
    channel_username2 = '@Bot4Chan'
    
    if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
                bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
                return
                
    user_id = message.from_user.id
    ban_info = get_ban_info(user_id)

    if ban_info:
        _, sebep, bitis_tarihi = ban_info
        bot.reply_to(message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için Hesabın ┃Engellendi*\n┃*📨 Sebep*: `{sebep}`\n┃*🕓 Bitiş Tarihi:* `{bitis_tarihi}`\n┃\n┃*/itiraz Komutunu Kullanarak İtiraz ┃Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")
        return

    if not is_user_logged_in(user_id):
            bot.send_message(user_id, "*🚫 Üzgünüm, önce /start komutu ile giriş yapmanız gerekiyor!*", parse_mode="Markdown")
            return
    tc = message.text.split()[1] if len(message.text.split()) > 1 else None

    if not tc:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(2)
        bot.reply_to(message, '*⚠️ Lütfen geçerli bir T.C. Kimlik Numarası girin!.\nÖrnek:* `/tcplaka 11111111110`', parse_mode="Markdown")
        return

    try:
        
        api_url = f"http://20.121.61.198/orj/tcplaka/api.php?tc={tc}"
        response = requests.get(api_url)
        response.raise_for_status()


        data = response.content.decode('utf-8-sig')
        json_data = json.loads(data)

        if not json_data:
        	bot.send_chat_action(message.chat.id, 'typing')
        	time.sleep(0.1)
        	bot.reply_to(message, '⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*', parse_mode="Markdown")
        	return

        
        result_text = f"╭─━━━━━━━━━━━━─╮\n┃*T.C Kimlik Numarası*: `{json_data['tc']}`\n┃*Borç Türü:* `{json_data['borcTuru']}`\n┃*Plaka:* `{json_data['plaka']}`\n┃*İsim Soyisim:* `{json_data['isimSoyisim']}`\n┃*Yazılan Ceza:* `{json_data['yazilanCeza']}`\n╰─━━━━━━━━━━━━─╯"
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(2)
        bot.reply_to(message, result_text, parse_mode="Markdown")
        increment_query_count()

    except requests.exceptions.HTTPError as errh:
        bot.reply_to(message, f'Hata! HTTP Error: {errh}')

    except requests.exceptions.ConnectionError as errc:
        bot.reply_to(message, f'Hata! Bağlantı Hatası: {errc}')

    except requests.exceptions.Timeout as errt:
        bot.reply_to(message, f'Hata! Zaman Aşımı Hatası: {errt}')

    except requests.exceptions.RequestException as err:
        bot.reply_to(message, f'Hata! Genel Hata: {err}')

    except Exception as e:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, f'⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*', parse_mode="Markdown")



@bot.message_handler(commands=['ailepro'])
def handle_sorgu(message):
    if message.chat.type != "private":
        return

    user_id = message.from_user.id
    channel_username1 = '@CerenyTeam'
    channel_username2 = '@Bot4Chan'
    
    if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
        bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
        return
                
    user_id = message.from_user.id
    ban_info = get_ban_info(user_id)

    if ban_info:
        _, sebep, bitis_tarihi = ban_info
        bot.reply_to(message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için Hesabın ┃Engellendi*\n┃*📨 Sebep*: `{sebep}`\n┃*🕓 Bitiş Tarihi:* `{bitis_tarihi}`\n┃\n┃*/itiraz Komutunu Kullanarak İtiraz ┃Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")
        return

    if not is_user_logged_in(user_id):
        bot.send_message(user_id, "*🚫 Üzgünüm, önce /start komutu ile giriş yapmanız gerekiyor!*", parse_mode="Markdown")
        return
    try:
        session = requests.Session()
        session.headers = {
            'User-Agent': 'Your User Agent String',
            'Authorization': 'Your Authorization Token',
        }
        tc = message.text.split()[1]
        response = session.get(f"http://20.121.61.198/orj/sulale/aile.php?tc={tc}").json()
        if response:
            formatted_result = ""
            kayit_sayisi = 0  # Kayıt sayısını tutmak için sayaç
            
            for person in response:
                kayit_sayisi += 1
                
                formatted_result += f"\n╭─━━━━━━━━━━━━─╮\n┃*Kayıt Sayısı:* `{kayit_sayisi}`\n┃─━━━━━━━━━━━━─\n┃ *Yakınlık Derecesi:* `{person['Yakınlık'] or 'Bulunamadı'}`\n"
                formatted_result += f"┃ *T.C Kimlik Numarası:* `{person['TcKm'] or 'Bulunamadı'}`\n"
                formatted_result += f"┃ *Adı:* `{person['Adı'] or 'Bulunamadı'}`\n"
                formatted_result += f"┃ *Soyadı:* `{person['Soyadı'] or 'Bulunamadı'}`\n"
                formatted_result += f"┃ *Doğum Tarihi:* `{person['DoğumGünü'] or 'Bulunamadı'}`\n"
                formatted_result += f"┃ *Nüfus İl:* `{person['Nufüsil'] or 'Bulunamadı'}`\n"  # None yerine Bilinmiyor
                formatted_result += f"┃ *Nüfus İlçe:* `{person['Nufüsilçe'] or 'Bulunamadı'}`\n"
                formatted_result += f"┃ *Telefon Numarası:* `{person['GSM'] or 'Bulunamadı'}`\n"
                formatted_result += f"╰─━━━━━━━━━━━━─╯"
                
                if len(formatted_result) > 3500:
                    bot.send_chat_action(message.chat.id, 'typing')
                    time.sleep(0.1)
                    bot.send_message(message.chat.id, formatted_result, parse_mode="Markdown")
                    
                    formatted_result = ""
            
            if formatted_result:
                bot.send_chat_action(message.chat.id, 'typing')
                time.sleep(0.1)
                bot.send_message(message.chat.id, formatted_result, parse_mode="Markdown")
                bot.send_chat_action(message.chat.id, 'typing')
                time.sleep(0.1)
                bot.send_message(message.chat.id, f"*Toplam Kayıt Sayısı:* `{kayit_sayisi}` *Adet*", parse_mode="Markdown")
                increment_query_count()
    except IndexError:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.send_message(message.chat.id, "*⚠️ Lütfen geçerli bir T.C. Kimlik Numarası girin!.\n\nÖrnek:* `/ailepro 11111111110`", parse_mode="Markdown")
    except Exception as e:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.send_message(message.chat.id, f"⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*", parse_mode="Markdown")





@bot.message_handler(commands=['aile'])
def handle_sorgu(message):
    if message.chat.type != "private":
        return

    user_id = message.from_user.id
    channel_username1 = '@CerenyTeam'
    channel_username2 = '@Bot4Chan'
    
    if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
                bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
                return
                
    user_id = message.from_user.id
    ban_info = get_ban_info(user_id)

    if ban_info:
        _, sebep, bitis_tarihi = ban_info
        bot.reply_to(message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için Hesabın ┃Engellendi*\n┃*📨 Sebep*: `{sebep}`\n┃*🕓 Bitiş Tarihi:* `{bitis_tarihi}`\n┃\n┃*/itiraz Komutunu Kullanarak İtiraz ┃Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")
        return

    if not is_user_logged_in(user_id):
            bot.send_message(user_id, "*🚫 Üzgünüm, önce /start komutu ile giriş yapmanız gerekiyor!*", parse_mode="Markdown")
            return
    try:

        session = requests.Session()
        session.headers = {
            'User-Agent': 'Your User Agent String',
            'Authorization': 'Your Authorization Token',
        }
        tc = message.text.split()[1]
        response = session.get(f"http://20.121.61.198/orj/aile/api.php?tc={tc}").json()
        if response:
            formatted_result = ""
            kayit_sayisi = 0  # Kayıt sayısını tutmak için sayaç
            
            for person in response:
                kayit_sayisi += 1
                
                formatted_result += f"\n╭─━━━━━━━━━━━━─╮\n┃*Kayıt Sayısı:* `{kayit_sayisi}`\n┃─━━━━━━━━━━━━─\n┃ *Yakınlık:* `{person['YAKINLIK']}`\n"
                formatted_result += f"┃ *T.C Kimlik Numarası* `{person['TC']}`\n"
                formatted_result += f"┃ *Adı:* `{person['ADI']}`\n"
                formatted_result += f"┃ *Soyadı:* `{person['SOYADI']}`\n"
                formatted_result += f"┃ *Doğum Tarihi:* `{person['DOGUMTARIHI']}`\n"
                formatted_result += f"┃ *Nüfus İl:* `{person['NUFUSIL']}`\n"
                formatted_result += f"┃ *Nüfus İlçe:* `{person['NUFUSILCE']}`\n"
                formatted_result += f"┃ *Baba Adı:* `{person['BABAADI']}`\n"
                formatted_result += f"┃ *Baba T.C:* `{person['BABATC']}`\n"
                formatted_result += f"┃ *Anne T.C:* `{person['ANNETC']}`\n"
                formatted_result += f"┃ *Anne Adı:* `{person['ANNEADI']}`\n"
                formatted_result += f"┃ *Uyruk:* `{person['UYRUK']}`\n╰─━━━━━━━━━━━━─╯"
                
                if len(formatted_result) > 3500:
                	bot.send_chat_action(message.chat.id, 'typing')
                	time.sleep(0.1)
                	bot.send_message(message.chat.id, formatted_result, parse_mode="Markdown")
                	
                	formatted_result = ""
            
            if formatted_result:
            	bot.send_chat_action(message.chat.id, 'typing')
            	time.sleep(0.1)
            	bot.send_message(message.chat.id, formatted_result, parse_mode="Markdown")
            	bot.send_chat_action(message.chat.id, 'typing')
            	time.sleep(0.1)
            	bot.send_message(message.chat.id, f"*Toplam Kayıt Sayısı:* `{kayit_sayisi}` *Adet*", parse_mode="Markdown")
            	increment_query_count()
            
        else:
        	bot.send_chat_action(message.chat.id, 'typing')
        	time.sleep(0.1)
        	bot.send_message(message.chat.id, "⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*", parse_mode="Markdown")
    except IndexError:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.send_message(message.chat.id, "*⚠️ Lütfen geçerli bir T.C. Kimlik Numarası girin!.\n\nÖrnek:* `/aile 11111111110`", parse_mode="Markdown")
    except Exception as e:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.send_message(message.chat.id, f"⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*", parse_mode="Markdown")




API_ENDPOINT = 'http://20.121.61.198/orj/sulale/api.php?tc={}'
total_messages = 0

MAX_MESSAGE_LENGTH = 4096

@bot.message_handler(commands=['sulale'])
def sulale(message):
    if message.chat.type != "private":
        return

    user_id = message.from_user.id

            
    global total_messages
    # Check if a parameter (TC) is provided
    if len(message.text.split()) > 1:
        tc = message.text.split()[1]
        api_url = API_ENDPOINT.format(tc)
        
        # Make request to the API
        response = requests.get(api_url)
        
        try:
            # Attempt to parse the response as JSON
            data = response.json()

            # Check if any data is returned
            if data and isinstance(data, list) and data[0].get("TC"):
                # Increment kayit_sayisi for each record
                kayit_sayisi = len(data)

                text = f"╭─━━━━━━━━━━━━━─╮\n┃*Toplam:* `{kayit_sayisi}` *Kişi.*\n╰─━━━━━━━━━━━━━─╯"

                for i, record in enumerate(data):
                    yakınlık = record.get("YAKINLIK", "Bilgi Yok")
                    tc_km = record.get("TC", "Bilgi Yok")
                    adı = record.get("ADI", "Bilgi Yok")
                    soyadı = record.get("SOYADI", "Bilgi Yok")
                    doğum_tarihi = record.get("DOGUMTARIHI", "Bilgi Yok")
                    nufüsil = record.get("NUFUSIL", "Bilgi Yok")
                    nufüsilçe = record.get("NUFUSILCE", "Bilgi Yok")
                    anne_adi = record.get("ANNEADI", "Bilgi Yok")
                    anne_tc = record.get("ANNETC", "Bilgi Yok")
                    baba_adi = record.get("BABAADI", "Bilgi Yok")
                    baba_tc = record.get("BABATC", "Bilgi Yok")
                    uyruk = record.get("UYRUK", "Bilgi Yok")

                    record_text = (                 
                        f"\n╭─━━━━━━━━━━━━━─╮\n┃*Sonuç No:* `{i}`\n"
                        f"┃─━━━━━━━━━━━━━─\n╭─━━━━━━━━━━━━━─╮\n┃*Adı:* `{adı}`\n"
                        f"┃*Soyadı:* `{soyadı}`\n"
                        f"┃*Yakinlik:* `{yakınlık}`\n"
                        f"┃*TC Kimlik Numarası:* `{tc_km}`\n"
                        f"┃*Doğum Tarihi:* `{doğum_tarihi}`\n"
                        f"┃*Nüfus İL:* `{nufüsil}`\n"
                        f"┃*Nüfus İLÇE:* `{nufüsilçe}`\n"
                        f"┃*Anne Adı:* `{anne_adi}`\n"
                        f"┃*Anne TC:* `{anne_tc}`\n"
                        f"┃*Baba Adı:* `{baba_adi}`\n"
                        f"┃*Baba TC:* `{baba_tc}`\n"
                        f"┃*Uyruk:* `{uyruk}`\n"
                        f"╰─━━━━━━━━━━━━━─╯\n\n"
                    )

                    # Check if the current message length exceeds the limit
                    if len(text + record_text) > MAX_MESSAGE_LENGTH:
                        bot.send_message(user_id, text, parse_mode="Markdown")
                        text = ""  # Reset text for the next message

                    text += record_text

                # Send any remaining text
                if text:
                    bot.send_message(user_id, text, parse_mode="Markdown")

            else:
                bot.send_chat_action(message.chat.id, 'typing')
                time.sleep(0.1)
                bot.reply_to(message, "⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*", parse_mode="Markdown")
        except ValueError:
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(0.1)
            bot.reply_to(message, "⚠️ API'den Yanıt alınamıyor Lütfen Yönetici ile iletişime geçin!", parse_mode="Markdown")
    else:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, "*⚠️ Lütfen geçerli bir T.C. Kimlik Numarası girin!.\nÖrnek:* `/sulale 11111111110`", parse_mode="Markdown")





API_ENDPOINT = 'http://20.121.61.198/orj/sulale/api.php?tc={}'
total_messages = 0

MAX_MESSAGE_LENGTH = 4096

@bot.message_handler(commands=['sulale'])
def sulale(message):
    if message.chat.type != "private":
        return

    user_id = message.from_user.id
    channel_username1 = '@CerenyTeam'
    channel_username2 = '@Bot4Chan'
    
    if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
        bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
        return
                
    user_id = message.from_user.id
    ban_info = get_ban_info(user_id)

    if ban_info:
        _, sebep, bitis_tarihi = ban_info
        bot.reply_to(message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için Hesabın ┃Engellendi*\n┃*📨 Sebep*: `{sebep}`\n┃*🕓 Bitiş Tarihi:* `{bitis_tarihi}`\n┃\n┃*/itiraz Komutunu Kullanarak İtiraz Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")
        return

    if not is_user_logged_in(user_id):
        bot.send_message(user_id, "*🚫 Üzgünüm, önce /start komutu ile giriş yapmanız gerekiyor!*", parse_mode="Markdown")
        return
            
    global total_messages
    if len(message.text.split()) > 1:
        tc = message.text.split()[1]
        api_url = API_ENDPOINT.format(tc)
        
        response = requests.get(api_url)
        
        try:
            data = response.json()

            if data and isinstance(data, list) and data[0].get("TC"):
                kayit_sayisi = len(data)

                text = f"╭─━━━━━━━━━━━━━─╮\n┃*Toplam:* `{kayit_sayisi}` *Kişi.*\n╰─━━━━━━━━━━━━━─╯\n"

                for i, record in enumerate(data):
                    yakınlık = record.get("YAKINLIK", "Bilgi Yok")
                    tc_km = record.get("TC", "Bilgi Yok")
                    adı = record.get("ADI", "Bilgi Yok")
                    soyadı = record.get("SOYADI", "Bilgi Yok")
                    doğum_tarihi = record.get("DOGUMTARIHI", "Bilgi Yok")
                    nufüsil = record.get("NUFUSIL", "Bilgi Yok")
                    nufüsilçe = record.get("NUFUSILCE", "Bilgi Yok")
                    anne_adi = record.get("ANNEADI", "Bilgi Yok")
                    anne_tc = record.get("ANNETC", "Bilgi Yok")
                    baba_adi = record.get("BABAADI", "Bilgi Yok")
                    baba_tc = record.get("BABATC", "Bilgi Yok")
                    uyruk = record.get("UYRUK", "Bilgi Yok")

                    record_text = (                 
                        f"┃─━━━━━━━━━━━━━─\n┃*Sonuç No:* `{i}`\n┃─━━━━━━━━━━━━━─\n"
                        f"╭─━━━━━━━━━━━━━─╮\n┃*Adı:* `{adı}`\n"
                        f"┃*Soyadı:* `{soyadı}`\n"
                        f"┃*Yakinlik:* `{yakınlık}`\n"
                        f"┃*TC Kimlik Numarası:* `{tc_km}`\n"
                        f"┃*Doğum Tarihi:* `{doğum_tarihi}`\n"
                        f"┃*Nüfus İL:* `{nufüsil}`\n"
                        f"┃*Nüfus İLÇE:* `{nufüsilçe}`\n"
                        f"┃*Anne Adı:* `{anne_adi}`\n"
                        f"┃*Anne TC:* `{anne_tc}`\n"
                        f"┃*Baba Adı:* `{baba_adi}`\n"
                        f"┃*Baba TC:* `{baba_tc}`\n"
                        f"┃*Uyruk:* `{uyruk}`\n"
                        f"╰─━━━━━━━━━━━━━─╯\n\n"
                    )

                    # Check if the current message length exceeds the limit
                    if len(text + record_text) > MAX_MESSAGE_LENGTH:
                        bot.send_message(user_id, text, parse_mode="Markdown")
                        increment_query_count()
                        text = ""

                    text += record_text

                if text:
                    bot.send_message(user_id, text, parse_mode="Markdown")
                    increment_query_count()

            else:
                bot.send_chat_action(message.chat.id, 'typing')
                time.sleep(0.1)
                bot.reply_to(message, "⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*", parse_mode="Markdown")
        except ValueError:
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(0.1)
            bot.reply_to(message, "⚠️ API'den Yanıt alınamıyor Lütfen Yönetici ile iletişime geçin!", parse_mode="Markdown")
    else:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, "*⚠️ Lütfen geçerli bir T.C. Kimlik Numarası girin!.\nÖrnek:* `/sulale 11111111110`", parse_mode="Markdown")




@bot.message_handler(commands=['yardim'])
def help(message):
    try:
        command = message.text.split(' ', 1)[1]
    except IndexError:
        bot.reply_to(message, "*Hatalı format girdiniz. Lütfen /yardim <Komut> şeklinde girin.\n\nÖrnek: /yardim sorgu")
        return

    if command == "sorgu":
        bot.reply_to(message, "`/sorgu -isim • -soyisim • -il • -ilce •`\n\n*Eyer 2 isimli ise* `/sorgu -isim Esma+Nur -soyisim uslu` *şeklinde girin!.*\n\n • *Yazan yerlere Lütfen Bilgileri Girin Ve gönderin.*", parse_mode="Markdown")
    elif command == "gsmtc":
        bot.reply_to(message, "`/gsmtc (+90)` *olmadan 5457483139 şeklinde girin!.*\n\n*Örnek:* `/gsmtc 5457483139`", parse_mode="Markdown")
    else:
        bot.reply_to(message, f"`{command}` *için yardım mesajı bulunamadı.*", parse_mode="Markdown")



from io import BytesIO

API_BASE_URL = "http://20.121.61.198/orj/adsoyad/api.php"
WAIT_TIME = 3

user_last_query_time = {}

@bot.message_handler(commands=['sorgu'])
def sorgu(message):
    if message.chat.type != "private":
        return
    chat_id = message.chat.id
    user_first_name = message.from_user.first_name
    user_id = message.from_user.id
    channel_username1 = '@CerenyTeam'
    channel_username2 = '@Bot4Chan'
    
    if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
                bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
                return
                
    user_id = message.from_user.id
    ban_info = get_ban_info(user_id)

    if ban_info:
        _, sebep, bitis_tarihi = ban_info
        bot.reply_to(message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için Hesabın ┃Engellendi*\n┃*📨 Sebep*: `{sebep}`\n┃*🕓 Bitiş Tarihi:* `{bitis_tarihi}`\n┃\n┃*/itiraz Komutunu Kullanarak İtiraz ┃Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")
        return

    if not is_user_logged_in(user_id):
            bot.send_message(user_id, "*🚫 Üzgünüm, önce /start komutu ile giriş yapmanız gerekiyor!*", parse_mode="Markdown")
            return

    try:

        user_id = message.from_user.id

        last_query_time = user_last_query_time.get(user_id, 0)
        current_time = time.time()

        if current_time - last_query_time < WAIT_TIME:
            bot.reply_to(message, f"⏳ *Lütfen bekle, spama düşmüşsün 5 saniye sonra tekrar dene!.*", parse_mode="Markdown")
            return

        
        user_last_query_time[user_id] = current_time

        parameters = message.text.split()[1:]
        if len(parameters) < 4 or parameters[0] != '-isim' or parameters[2] != '-soyisim':
            raise IndexError
        isim = parameters[1]
        soyisim = parameters[3]
        il = parameters[5] if len(parameters) > 5 and parameters[4] == '-il' else ''
        ilce = parameters[7] if len(parameters) > 7 and parameters[6] == '-ilce' else ''

        response = requests.get(f"{API_BASE_URL}?adi={isim}&soyadi={soyisim}&nufusil={il}&nufusilce={ilce}").json()

        if response and isinstance(response, list) and response[0].get("TC"):
            kayit_sayisi = len(response)
            file_content = f"╭─━━━━━━━━━━━━━─╮\n┃Toplam {kayit_sayisi} Kişi.\n╰─━━━━━━━━━━━━━─╯"

            for i, record in enumerate(response):
                file_content += f"\n╭─━━━━━━━━━━━━━─╮\n┃Sonuç No {i + 1}\n┃JiTeM_ID: {record.get('id', 'Bilgi Yok')}\n┃─━━━━━━━━━━━━━─\n" \
                                f"┃Adı: {record.get('ADI', 'Bilgi Yok')}\n" \
                                f"┃Soyadı: {record.get('SOYADI', 'Bilgi Yok')}\n" \
                                f"┃TC Kimlik Numarası: {record.get('TC', 'Bilgi Yok')}\n" \
                                f"┃Doğum Tarihi: {record.get('DOGUMTARIHI', 'Bilgi Yok')}\n" \
                                f"┃Nüfus İL: {record.get('NUFUSIL', 'Bilgi Yok')}\n" \
                                f"┃Nüfus İLÇE: {record.get('NUFUSILCE', 'Bilgi Yok')}\n" \
                                f"┃Anne Adı: {record.get('ANNEADI', 'Bilgi Yok')}\n" \
                                f"┃Anne TC: {record.get('ANNETC', 'Bilgi Yok')}\n" \
                                f"┃Baba Adı: {record.get('BABAADI', 'Bilgi Yok')}\n" \
                                f"┃Baba TC: {record.get('BABATC', 'Bilgi Yok')}\n" \
                                f"┃Uyruk: {record.get('UYRUK', 'Bilgi Yok')}\n╰─━━━━━━━━━━━━━─╯"

            file_content_bytes = file_content.encode("utf-8")
            file_io = BytesIO(file_content_bytes)
            file_io.name = f"{user_id}_adsoyad.txt"
            bot.send_document(message.chat.id, file_io)

        else:
            bot.reply_to(message, "⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*", parse_mode="Markdown")
    except IndexError:
        bot.reply_to(message, "⚠️ *Geçersiz Komut, Parametreleri*\n	*Örnek:* `/sorgu -isim Mehmet -soyisim Yılmaz -il İstanbul -ilce Esenler`\n\n*Eyer 2 isimli ise* `/sorgu -isim Esma+Nur` *şeklinde girin!.*", parse_mode="Markdown")





@bot.message_handler(commands=['haciz'])
def handle_haciz(message):
    if message.chat.type != "private":
        return

    user_id = message.from_user.id
    channel_username1 = '@CerenyTeam'
    channel_username2 = '@Bot4Chan'
    
    if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
                bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
                return
                
    user_id = message.from_user.id
    ban_info = get_ban_info(user_id)

    if ban_info:
        _, sebep, bitis_tarihi = ban_info
        bot.reply_to(message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için Hesabın ┃Engellendi*\n┃*📨 Sebep*: `{sebep}`\n┃*🕓 Bitiş Tarihi:* `{bitis_tarihi}`\n┃\n┃*/itiraz Komutunu Kullanarak İtiraz ┃Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")
        return

    if not is_user_logged_in(user_id):
            bot.send_message(user_id, "*🚫 Üzgünüm, önce /start komutu ile giriş yapmanız gerekiyor!*", parse_mode="Markdown")
            return
            
    try:
        
        tc_kimlik = message.text.split()[1]

        
        api_url = f'http://20.121.61.198/orj/haciz/api.php?tc={tc_kimlik}'
        response = requests.get(api_url)
        data = response.json()

        
        tc_kimlik = data.get('TcKm', '')
        adi = data.get('Adı', '')
        soyadi = data.get('Soyadı', '')
        haciz_durumu = data.get('Haciz', '')
        telegram_link = data.get('Telegram', '')

        response_text = f'╭─━━━━━━━━━━━━━─╮\n┃*T.C. Kimlik Numarası:* `{tc_kimlik}`\n┃*Adı:* `{adi}`\n┃*Soyadı:* `{soyadi}`\n┃*Haciz Durumu:* `{haciz_durumu}`\n╰─━━━━━━━━━━━━━─╯'
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, response_text, parse_mode="Markdown")
        increment_query_count()
    except IndexError:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, '*⚠️ Lütfen geçerli bir T.C. Kimlik Numarası girin!.\nÖrnek:* `/haciz 11111111110`', parse_mode="Markdown")




def create_connection():
    conn = sqlite3.connect("query_count.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS counts (id INTEGER PRIMARY KEY, count INTEGER)")
    conn.commit()
    return conn

def get_query_count():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT count FROM counts WHERE id = 1")
    count = cursor.fetchone()
    conn.close()
    if count:
        return count[0]
    else:
        return 0

def increment_query_count():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT count FROM counts WHERE id = 1")
    count = cursor.fetchone()
    if count:
        new_count = count[0] + 1
        cursor.execute("UPDATE counts SET count = ?", (new_count,))
    else:
        new_count = 1
        cursor.execute("INSERT INTO counts (id, count) VALUES (?, ?)", (1, new_count))
    conn.commit()
    conn.close()
    return new_count



@bot.message_handler(content_types=['new_chat_members'])
def welcome_message(message):
    new_members = message.new_chat_members
    greetings = ["Hayatın, senin gibi güzel insanlarla dolu olması ne harika! Aramıza hoş geldin, burada olduğun için mutluluk duyuyoruz. Umarım beğenirsin!", "Seni burada görmek harika! Yeni macerana hoş geldin. Umarım seninle birlikte geçirdiğimiz zaman senin için keyifli olur.", "Güzel sözlerinle bize ışık saçan sevgili arkadaşım, Hoş geldin"]

    for member in new_members:
        random_greeting = random.choice(greetings)
        photo_path = 'hosgeldin.png'
        with open(photo_path, 'rb') as photo:
        	caption = f"*{random_greeting}, {member.first_name}!* (`{member.id}`)"
        	bot.send_chat_action(message.chat.id, 'typing')
        	time.sleep(2)
        	bot.send_photo(message.chat.id, photo, caption=caption, parse_mode='Markdown')






API_ENDPOINT = 'https://apis.xditya.me/write?text={}'

@bot.message_handler(commands=['yaz'])
def yaz(message):
    if message.chat.type != "private":
        return

    user_id = message.from_user.id
    channel_username1 = '@CerenyTeam'
    channel_username2 = '@Bot4Chan'
    
    if not is_user_in_channel(user_id, channel_username1) or not is_user_in_channel(user_id, channel_username2):
                bot.send_message(user_id, text="*Üzgünüm, @JitemSorgu ve @JitemChats gruplarına katılmak zorunludur!*", parse_mode="Markdown")
                return
                
    user_id = message.from_user.id
    ban_info = get_ban_info(user_id)

    if ban_info:
        _, sebep, bitis_tarihi = ban_info
        bot.reply_to(message, f"*╭─━━━━━━━━━━━━━─╮\n┃🚫 Kurallara Uymadığın için Hesabın ┃Engellendi*\n┃*📨 Sebep*: `{sebep}`\n┃*🕓 Bitiş Tarihi:* `{bitis_tarihi}`\n┃\n┃*/itiraz Komutunu Kullanarak İtiraz ┃Edebilirsiniz!*\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")
        return

    if not is_user_logged_in(user_id):
            bot.send_message(user_id, "*🚫 Üzgünüm, önce /start komutu ile giriş yapmanız gerekiyor!*", parse_mode="Markdown")
            return
    try:
        text = message.text.split(maxsplit=1)[1]
       
        api_url = API_ENDPOINT.format(text)
        response = requests.get(api_url)
        
        if response.status_code == 200:
            bot.send_photo(message.chat.id, response.content)
        else:
            bot.send_message(message.chat.id, "⚠️ *API'de sorun var Lütfen Yönetici ile iletişime geçin!.*", parse_mode="Markdown")
    
    except IndexError:
        bot.send_message(message.chat.id, "*⚠️ Lütfen geçerli bir Mesaj girin!.\nÖrnek:* `/yaz Merhaba`", parse_mode="Markdown")



    
admin_file = "admins.txt"


def load_admins():
    try:
        with open(admin_file, "r") as file:
            admins = [int(line.strip()) for line in file]
        return admins
    except FileNotFoundError:
        print(f"⚠️ {admin_file} dosyası bulunamadı.")
        return []


def save_admins(admins):
    with open(admin_file, "w") as file:
        for admin in admins:
            file.write(str(admin) + "\n")


def admins_only(func):
    def wrapper(message):
        user_id = message.from_user.id
        admins = load_admins()
        if user_id in admins:
            func(message)
        else:
            bot.send_message(message.chat.id, "*⚠️ Üzgünüm, Bu, Komuta, Erişim Yetkiniz, Yok!*", parse_mode="Markdown")
            
    return wrapper






@bot.message_handler(commands=['ban'])
@admins_only
def ban_user(message):
    if message.chat.type != "private":
        return

    parameters = message.text.split()

    if len(parameters) >= 4:  # Check if duration is provided
        try:
            user_id = parameters[1]

            # Check if the user is already banned
            if is_user_banned(user_id):
                bot.reply_to(message, "*⚠️ Bu Kullanıcı Zaten Banlı!.*", parse_mode="Markdown")
                return

            mesaj = ' '.join(parameters[2:-1])  # Exclude the last element as it's the duration
            duration_in_days = int(parameters[-1])  # Take the last element as duration
            end_date = datetime.now() + timedelta(days=duration_in_days)

            # Save ban information to ban.db
            with sqlite3.connect("ban.db") as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO bans (user_id, reason, end_date) VALUES (?, ?, ?)",
                               (user_id, mesaj, end_date))
                conn.commit()

            bot.reply_to(message, f"╭─━━━━━━━━━━━━━─╮\n┃(`B.A.N`) *Başarıyla 7 Kahinatının amına \n┃postalandı:*\n┃*ID:* `{user_id}`\n┃*Sebep:* `{mesaj}`\n┃*Süre:* `{duration_in_days}` gün\n┃\n╰─━━━━━━━━━━━━━─╯", parse_mode="Markdown")
        except ValueError:
            bot.reply_to(message, "*⚠️ Geçersiz süre formatı. Süre, tam sayı olarak girilmelidir.*", parse_mode="Markdown")
    else:
        bot.reply_to(message, "*⚠️ Geçersiz Komut formatı.* `/ban <kullanıcı_ID> <Sebep> <Süre>` *Şeklinde girin!.*", parse_mode="Markdown")


def cleanup_expired_bans():
    while True:
        time.sleep(25)  # Her 25 saniyede bir kontrol et

        with sqlite3.connect("ban.db") as conn:
            cursor = conn.cursor()
            current_time = datetime.now()

            # Süresi biten banları seç
            cursor.execute("SELECT * FROM bans WHERE end_date <= ?", (current_time,))
            expired_bans = cursor.fetchall()

            # Banları kaldır
            for ban in expired_bans:
                cursor.execute("DELETE FROM bans WHERE user_id = ?", (ban[0],))
                conn.commit()

# cleanup_expired_bans fonksiyonunu başlat
cleanup_thread = threading.Thread(target=cleanup_expired_bans)
cleanup_thread.start()




def is_user_banned(user_id):
    with sqlite3.connect("ban.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bans WHERE user_id = ? AND end_date > ?", (user_id, datetime.now()))
        return cursor.fetchone() is not None



def send_membership_expiry_notification(user_id, first_name, chat_id):
    try:
        notification_text = f"Süresi biten kullanıcı:\nID: {user_id}\nİsim: {first_name}"

        chat_id = chat_id or -1002031422125
        bot.send_message(chat_id, notification_text)
    except Exception as notification_error:
        print(f"Bildirim gönderme hatası: {notification_error}")








conn = sqlite3.connect('premium.db', check_same_thread=False)
cursor = conn.cursor()
db_lock = threading.Lock()

# premium tablosunu oluştur
cursor.execute('''
    CREATE TABLE IF NOT EXISTS premium (
        id INTEGER PRIMARY KEY,
        expiration_date INTEGER
    )
''')
conn.commit()


@bot.message_handler(commands=['uyelik'])
def uyelik(message):
    try:
        # Kullanıcıdan gelen komut
        args = message.text.split()

        # Hatalı komut kontrolü
        if len(args) != 5 or args[1] != '-id' or args[3] != '-gun':
            bot.reply_to(message, "Geçersiz komut formatı. Örnek: /uyelik -id ID -gun 3")
            return

        user_id = int(args[2])
        days = int(args[4])

        # Premium üyelik tarihini hesapla
        expiration_date = int((datetime.now() + timedelta(days=days)).timestamp())

        # Veritabanına ekle
        with db_lock, sqlite3.connect('premium.db', check_same_thread=False) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO premium (id, expiration_date) VALUES (?, ?)', (user_id, expiration_date))
            conn.commit()

        # ID'yi metin dosyasına ekle
        with open('premium.txt', 'a') as file:
            file.write(f"{user_id}\n")

        bot.reply_to(message, f"{user_id} ID'sine {days} gün premium üyelik eklenmiştir.")

    except ValueError:
        bot.reply_to(message, "ID ve gün değerleri tam sayı olmalıdır.")

# Sürekli olarak premium üyelikleri kontrol et
def continuous_check_premium():
    while True:
        current_time = int(datetime.now().timestamp())
        with db_lock, sqlite3.connect('premium.db', check_same_thread=False) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM premium WHERE expiration_date < ?', (current_time,))
            conn.commit()
        time.sleep(60)  # Her dakika kontrol et

# Sürekli kontrol işlemi başlat
check_premium_thread = threading.Thread(target=continuous_check_premium)
check_premium_thread.start()






@bot.message_handler(commands=['cevapla'])
@admins_only
def handle_destekle(message):
    user_id = message.from_user.id
    kullanici = f"{message.from_user.first_name} {message.from_user.last_name}" if message.from_user.last_name else message.from_user.first_name
    mesaj = message.text.split(maxsplit=2)
    
    if len(mesaj) > 2 and mesaj[1].isdigit():
        destek_user_id = int(mesaj[1])
        destek_mesaj = mesaj[2]
        bot.send_message(destek_user_id, f"*Yöneticiden Mesaj Var!: {destek_mesaj}*")
        bot.reply_to(message, "*Mesajınız gönderildi*.", parse_mode="Markdown")
    else:
        bot.reply_to(message, "⚠️ *Lütfen geçerli bir kullanıcı ID'si ve destek mesajı girin. Örnek:* `/cevapla ID Merhaba, size destek olabilir miyim?`", parse_mode="Markdown")



@bot.message_handler(commands=['destekle'])
@admins_only
def handle_destekle(message):
    user_id = message.from_user.id
    kullanici = f"{message.from_user.first_name} {message.from_user.last_name}" if message.from_user.last_name else message.from_user.first_name
    mesaj = message.text.split(maxsplit=2)
    
    if len(mesaj) > 2 and mesaj[1].isdigit():
        destek_user_id = int(mesaj[1])
        destek_mesaj = mesaj[2]
        bot.send_message(destek_user_id, f"*Yöneticiden Mesaj Var!: {destek_mesaj}*")
        bot.reply_to(message, "*Destek mesajınız gönderildi*.", parse_mode="Markdown")
    else:
        bot.reply_to(message, "⚠️ *Lütfen geçerli bir kullanıcı ID'si ve destek mesajı girin. Örnek:* `/destekle ID Merhaba, size destek olabilir miyim?`", parse_mode="Markdown")




@bot.message_handler(commands=['uyesil'])
@admins_only
def handle_uyesil(message):
    command_parts = message.text.split()

    if len(command_parts) != 3:
        bot.reply_to(message, "*⚠️ Geçersiz Komut formatı. Örnek:* `/uyesil <kullanıcı_ID> <uyelik>` *Şeklinde girin!.*", parse_mode="Markdown")
        return

    user_id = command_parts[1]
    membership = command_parts[2].lower()

    try:
        conn = sqlite3.connect(get_membership_db_filename(membership))
        cursor = conn.cursor()
        cursor.execute('DELETE FROM memberships WHERE user_id=?', (user_id,))
        rows_affected = cursor.rowcount
        conn.commit()

        if rows_affected > 0:
            bot.reply_to(message, f"*{membership.capitalize()} Üyeliği Başarıyla Silindi.*", parse_mode="Markdown")
        else:
            bot.reply_to(message, f"*⚠️ {membership.capitalize()} Üyeliği zaten yok.*", parse_mode="Markdown")
    except sqlite3.Error as e:
        print(f"SQLite Hatası (Üye Silme): {e}")
        bot.reply_to(message, "*⚠️ Veritabanı hatası! Üyelik silinemedi.*", parse_mode="Markdown")
    finally:
        if conn:
            conn.close()








def get_connection():
    return sqlite3.connect('veritabani.db')


        
@bot.message_handler(commands=['ara'])
def handle_ara(message):
    if message.chat.type != "private":
        return
    user_id = message.from_user.id
    username = message.text.split(' ', 1)[1].strip()

    user_info = get_user_info(username)
    
    if user_info:
        response = f"*Kullanıcı Adı:* `{user_info['username']}`\n*Şifre:* `{user_info['password']}`\n*Kullanıcı ID:* `{user_info['user_id']}`"
    else:
        response = "*⚠️ Girdiğiniz Kullanıcı Adına dair Herhangi Bir Bilgi Bulunamadı*"

    bot.send_message(user_id, response, parse_mode="Markdown")

def get_user_info(username):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT user_id, username, password FROM users WHERE username=?', (username,))
        result = cursor.fetchone()

        if result:
            user_id, username, password = result
            return {'user_id': user_id, 'username': username, 'password': password}
        else:
            return None
            



def is_user_banned(user_id):
    with sqlite3.connect("ban.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bans WHERE user_id = ? AND end_date > ?", (user_id, datetime.now()))
        return cursor.fetchone() is not None





@bot.message_handler(commands=['unban'])
@admins_only
def unban_user(message):
    if message.chat.type != "private":
        return

    parameters = message.text.split()

    if len(parameters) == 2:
        user_id = parameters[1]
        
        if is_user_banned(user_id):
            remove_ban(user_id)
            bot.reply_to(message, "✅ *Kullanıcının Banı Başarılı şekilde Açıldı!*", parse_mode="Markdown")
        else:
            bot.reply_to(message, "*⚠️ Bu Kullanıcı Banlı değil!.*", parse_mode="Markdown")
    else:
        bot.reply_to(message, "*⚠️ Geçersiz Komut Formatı. `/unban <kullanıcı_ID>` *şeklinde girin*", parse_mode="Markdown")



def remove_ban(user_id):
    with sqlite3.connect("ban.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM bans WHERE user_id = ?", (user_id,))
        conn.commit()

def get_connection():
    return sqlite3.connect('veritabani.db')


@bot.message_handler(commands=['admin'])
@admins_only
def handle_toplam(message):
    if message.chat.type != "private":
        return
    first_name = message.from_user.first_name
    bot.send_message(message.chat.id, f"*Merhaba, {first_name}*\n\n*Admin Bölümüne Hoş geldin!*\n\n`/toplam` *Toplam Kullanıcı Sayısını Verir*\n`/ban` *ID'den Kullanıcıyı Yassaklar*\n`/unban` *ID'den Kullanıcının Banını Kaldırır*\n`/ara` *Kullanıcı Adın'dan Bilgiler Verir*\n`/bakiye` *ID'den Kullanıcıya Bakiye Verir*\n`/uyekle` *ID'den Kullanıcıya Üyelik Verir*\n`/uyesil` *ID'den Kullanıcının Üyeliği Siler*\n`/liste` *Kullanıcı Liste Atar*\n\n*Yeni Özelikler İle Geleceğiz!*", parse_mode="Markdown")



@bot.message_handler(commands=['toplam'])
@admins_only
def handle_toplam(message):
    if message.chat.type != "private":
        return
    user_id_count = get_user_id_count()
    bot.send_message(message.chat.id, f"*Toplam Kullanıcı Sayısı:* `{user_id_count}`", parse_mode="Markdown")

def get_user_id_count():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(DISTINCT user_id) FROM users')
        result = cursor.fetchone()
        return result[0] if result else 0


def main():
    bot.polling()

if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            print(e)
            time.sleep(1)
