# CREATED FOR CERENYFLEXQ
# NOTİCE : !! DENEME AŞAMASINDADIR !!

import telebot
from pyrogram import Client, filters,enums,idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from pyrogram.enums import ChatAction, ParseMode
from pyrogram.types import CallbackQuery
import yt_dlp
from pyrogram import filters
from youtube_search import YoutubeSearch
import os,sys,re,requests
import asyncio,time
from datetime import datetime
import logging

TOKEN = "{TOKEN}"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def botu_baslatma(message):
    bot.reply_to(message, "MERHABA MÜZİK BOTUNA HOŞGELDİNİZ GRUPLARINIZA EKLEYEREK KEYFİNİ YAŞAYABİLİRSİN.")

@bot.message_handler(commands=['komut'])
def send_help_message(message):
    bot.reply_to(message, """
/song = MÜZİK İNDİRME İŞLEMİ..
    """)

@bot.message_handler(commands=['song'])
def song(client, message):
    message.delete()
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    chutiya = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"

    query = ""
    for i in message.command[1:]:
        query += " " + str(i)
    print(query)
    m = message.reply("**» Bekleyiniz...**")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        # print(results)
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"thumb{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)

        duration = results[0]["duration"]
        results[0]["url_suffix"]
        views = results[0]["views"]

    except Exception as e:
        m.edit(
            "**Youtube İçerik Bulunamadı,"
        )
        print(str(e))
        return
    m.edit("» İndiriliyor...")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"**Başlık :** {title[:25]}\n**İzlenme :** `{duration}`\n**Süre :** `{views}`\n**Talep »** {chutiya}"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(dur_arr[i]) * secmul
            secmul *= 60
        message.reply_audio(
            audio_file,
            caption=rep,
            thumb=thumb_name,
            title=title,
            duration=dur,
        )
        m.delete()
    except Exception as e:
        m.edit(
            f"**» Başarısız,"
        )
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

bot.polling()
