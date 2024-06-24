#SamilBen
#Samilbots

import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.events import StopPropagation

import os
import heroku3
from telethon import TelegramClient, events
from pyrogram import Client 
from pyrogram import filters
import logging

from pyrogram.types.messages_and_media import Message
import time
from pyrogram import Client, filters, __version__
from pyrogram.types import Message
from pyrogram.errors import (
    FloodWait,
    InputUserDeactivated,
    PeerIdInvalid,
    UserIsBlocked,
)


logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

DATABASE_URL = "mongodb+srv://matesamusic:matesamusic@cluster0.gvs02.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
BOT_USERNAME = "VTaggerBot"
LOG_CHANNEL = -1001757359371
GROUP_SUPPORT = "developersohbet"
GONDERME_TURU = os.environ.get("GONDERME_TURU", False) # Botunuzun yanıtladığınız mesajı gönderme türü. Eğer direkt iletmek isterseniz False, kopyasını göndermek isterseniz True olarak ayarlayın.
OWNER_ID = "5237976814"
LANGAUGE = "TR"

api_id = 2583
api_hash = "3d9cccd1f2c551c"
bot_token = ":zGCi6BHoGV6U4gax0KtSRE"

USERNAME = "EtikettagerBot"
group = -10019371
startmesaj = "**Ben grubunuzdaki üyeleri etiketleyebilen bir botum. Beni grubunuza alıp çalıştırabilirsiniz.**\n\n**Komutlar için /help yazın.**"
komutlar = "Komutlar:\n\n/utag -text- Kullanıcıları 5'li etiketlerim.\n/atag -text- Yöneticileri etiketlerim.\n/tektag Üyeleri tek tek etiketlerim.\n/etag - Üyeleri emoji ile etiketlerim.\n/soztag - Üyeleri sözler ile etiketlerim.\n/gisimtag - Üyeleri güzel isimlerle etiketlerim.\n/cancel - Etiket işlemini iptal ederim .\n\nYalnızca yöneticiler bu komutları kullanabilir."
qrupstart = "**Şu an aktif olarak çalışmaktayım.** 🕊🍃\n\n**Komutlar hakkında bilgi için /help yazın."
sahib = "SamilBen"
support = "developersohbet"
sahib = "samilben"
ozel_list = 5237976814
DATABASE_URL = "mongodb+srv://@cluster0.gvs02.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
OWNER_ID = 5237976814 

client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

app = Client("GUNC",
             api_id=api_id,
             api_hash=api_hash,
             bot_token=bot_token
             )

anlik_calisan = []

ozel_list = [5237976814]
anlik_calisan = []
grup_sayi = []
etiketuye = []
rxyzdev_tagTot = {}
rxyzdev_initT = {}


@client.on(events.NewMessage(pattern="^/start$"))
async def info(event):
  await event.reply("**Merhaba Benim Ve Sahibim Hakkında Bilgi\n\nPython: 3.8.2\nKütüphanem: Telethon\n\nSahibim:  Gruplarınızda Üyeleri Etiketlemek için Yaratılmışım**",
                    buttons=(
                      [
                       Button.url('Beni Grubuna Ekle ➕', 'https://t.me/EtikeettagerBot?startgroup=a')
                      ],
                      [
                       Button.url('📢 Kanal', 'https://t.me/developersohbet'),
                       Button.url('🇹🇷 Sahibim', 'https://t.me/samilben')
                      ],
                     
                    ),
                    link_preview=False
                   )

@client.on(events.NewMessage(pattern="^/cancel$"))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"❌**Etiket işlemi durduruldu.\n\n Etiketlerin Sayı: {rxyzdev_tagTot[event.chat_id]}**")


@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await client.send_message(-1001757359371, f"ℹ️ **Yeni Kullanıcı -** {ad}")
     return await event.reply(f"**Merhaba \nGrubunuzdakı Üyeleri Etiketleye Bilirim\nKomutlar için Komutlar Düğmesine Tıklaya Bilirsiz**", buttons=(
                      [
                       Button.inline("Komutlar", data="komutlar")
                      ],
                      [
                       Button.url('Beni Grubuna Ekle', 'https://t.me/EtikettagerBot?startgroup=a'),
                       Button.url('Kanal', 'https://t.me/Samilbots')
                      ],
                      [
                       Button.url('Sahibim', 'https://t.me/SamilBen')
                      ],
                    ),
                    link_preview=False)


  if event.is_group:
    return await client.send_message(event.chat_id, f"**Beni Grubuna Aldığın için Teşekkürler ✨**")

# Başlanğıc Button
@client.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.edit(f"**Merhaba Ben @EtikettagerBot\nGrubunuzdakı Üyeleri Etiketleye Bilirim\nKomutlar için Komutlar Düğmesine Tıklaya Bilirsiz**", buttons=(
                      [
                       Button.inline("Komutlar", data="komutlar")
                      ],
                      [
                       Button.url('Beni Grubuna Ekle', 'https://t.me/EtikettagerBot?startgroup=a'),
                       Button.url('Kanal', 'https://t.me/Samilbots')
                      ],
                      [
                       Button.url('Sahibim', 'https://t.me/SamilBen')
                      ],
                    ),
                    link_preview=False)

# gece kusu
@client.on(events.callbackquery.CallbackQuery(data="komutlar"))
async def handler(event):
    await event.edit(f"**Komutlarım:\n\n/all -text-\n/atag -text-\n/cancel - İşlemi Durdururum...\n\n❕ Yalnızca yöneticileri bu komutları kullanabilir.**", buttons=(
                      [
                      Button.inline("◀️ Geri", data="start")
                      ]
                    ),
                    link_preview=False)


@client.on(events.NewMessage())
async def mentionalladmin(event):
  global etiketuye
  if event.is_group:
    if event.chat_id in etiketuye:
      pass
    else:
      etiketuye.append(event.chat_id)

soz = (
'𝐾𝑎𝑙𝑏𝑖 𝑔ü𝑧𝑒𝑙 𝑜𝑙𝑎𝑛ı𝑛 𝑔ö𝑧ü𝑛𝑑𝑒𝑛 𝑦𝑎ş 𝑒𝑘𝑠𝑖𝑘 𝑜𝑙𝑚𝑎𝑧𝑚ış', 
'İ𝑦𝑖𝑦𝑖𝑚 𝑑𝑒𝑠𝑒𝑚 𝑖𝑛𝑎𝑛𝑎𝑐𝑎𝑘 𝑜 𝑘𝑎𝑑𝑎𝑟 ℎ𝑎𝑏𝑒𝑟𝑠𝑖𝑧 𝑏𝑒𝑛𝑑𝑒𝑛', 
'𝑀𝑒𝑠𝑎𝑓𝑒𝑙𝑒𝑟 𝑈𝑚𝑟𝑢𝑚𝑑𝑎 𝐷𝑒ğ𝑖𝑙, İç𝑖𝑚𝑑𝑒 𝐸𝑛 𝐺ü𝑧𝑒𝑙 𝑌𝑒𝑟𝑑𝑒𝑠𝑖𝑛',
'𝐵𝑖𝑟 𝑀𝑢𝑐𝑖𝑧𝑒𝑦𝑒 İℎ𝑡𝑖𝑦𝑎𝑐ı𝑚 𝑉𝑎𝑟𝑑ı 𝐻𝑎𝑦𝑎𝑡 𝑆𝑒𝑛𝑖 𝐾𝑎𝑟şı𝑚𝑎 Çı𝑘𝑎𝑟𝑑ı', 
'Ö𝑦𝑙𝑒 𝑔ü𝑧𝑒𝑙 𝑏𝑎𝑘𝑡ı 𝑘𝑖 𝑘𝑎𝑙𝑏𝑖 𝑑𝑒 𝑔ü𝑙üşü𝑛 𝑘𝑎𝑑𝑎𝑟 𝑔ü𝑧𝑒𝑙 𝑠𝑎𝑛𝑚ış𝑡ı𝑚', 
'𝐻𝑎𝑦𝑎𝑡 𝑛𝑒 𝑔𝑖𝑑𝑒𝑛𝑖 𝑔𝑒𝑟𝑖 𝑔𝑒𝑡𝑖𝑟𝑖𝑟 𝑛𝑒 𝑑𝑒 𝑘𝑎𝑦𝑏𝑒𝑡𝑡𝑖ğ𝑖𝑛 𝑧𝑎𝑚𝑎𝑛ı 𝑔𝑒𝑟𝑖 𝑔𝑒𝑡𝑖𝑟𝑖𝑟', 
'𝑆𝑒𝑣𝑚𝑒𝑘 𝑖ç𝑖𝑛 𝑠𝑒𝑏𝑒𝑝 𝑎𝑟𝑎𝑚𝑎𝑑ı𝑚 ℎ𝑖ç 𝑠𝑒𝑠𝑖 𝑦𝑒𝑡𝑡𝑖 𝑘𝑎𝑙𝑏𝑖𝑚𝑒', 
'𝑀𝑢𝑡𝑙𝑢𝑦𝑢𝑚 𝑎𝑚𝑎 𝑠𝑎𝑑𝑒𝑐𝑒 𝑠𝑒𝑛𝑙𝑒', 
'𝐵𝑒𝑛 ℎ𝑒𝑝 𝑠𝑒𝑣𝑖𝑙𝑚𝑒𝑘 𝑖𝑠𝑡𝑒𝑑𝑖ğ𝑖𝑚 𝑔𝑖𝑏𝑖 𝑠𝑒𝑣𝑖𝑛𝑑𝑖𝑚', 
'𝐵𝑖𝑟𝑖 𝑣𝑎𝑟 𝑛𝑒 ö𝑧𝑙𝑒𝑚𝑒𝑘𝑡𝑒𝑛 𝑦𝑜𝑟𝑢𝑙𝑑𝑢𝑚 𝑛𝑒 𝑠𝑒𝑣𝑚𝑒𝑘𝑡𝑒𝑛', 
'Ç𝑜𝑘 𝑧𝑜𝑟 𝑏𝑒 𝑠𝑒𝑛𝑖 𝑠𝑒𝑣𝑚𝑒𝑦𝑒𝑛 𝑏𝑖𝑟𝑖𝑛𝑒 𝑎şı𝑘 𝑜𝑙𝑚𝑎𝑘', 
'Ç𝑜𝑘 ö𝑛𝑒𝑚𝑠𝑒𝑑𝑖𝑘 𝑖ş𝑒 𝑦𝑎𝑟𝑎𝑚𝑎𝑑ı 𝑎𝑟𝑡ı𝑘 𝑏𝑜ş𝑣𝑒𝑟𝑖𝑦𝑜𝑟𝑢𝑧', 
'𝐻𝑒𝑟𝑘𝑒𝑠𝑖𝑛 𝑏𝑖𝑟 𝑔𝑒ç𝑚𝑖ş𝑖 𝑣𝑎𝑟, 𝐵𝑖𝑟𝑑𝑒 𝑣𝑎𝑧𝑔𝑒ç𝑚𝑖ş𝑖', 
'𝐴şı𝑘 𝑜𝑙𝑚𝑎𝑘 𝑔ü𝑧𝑒𝑙 𝑏𝑖𝑟 ş𝑒𝑦 𝑎𝑚𝑎 𝑠𝑎𝑑𝑒𝑐𝑒 𝑠𝑎𝑛𝑎', 
'𝐴𝑛𝑙𝑎𝑦𝑎𝑛 𝑦𝑜𝑘𝑡𝑢, 𝑆𝑢𝑠𝑚𝑎𝑦ı 𝑡𝑒𝑟𝑐𝑖ℎ 𝑒𝑡𝑡𝑖𝑚', 
'𝑆𝑒𝑛 ç𝑜𝑘 𝑠𝑒𝑣 𝑑𝑒 𝑏ı𝑟𝑎𝑘ı𝑝 𝑔𝑖𝑑𝑒𝑛 𝑦𝑎𝑟 𝑢𝑡𝑎𝑛𝑠ı𝑛', 
'𝑂 𝑔𝑖𝑡𝑡𝑖𝑘𝑡𝑒𝑛 𝑠𝑜𝑛𝑟𝑎 𝑔𝑒𝑐𝑒𝑚 𝑔ü𝑛𝑑ü𝑧𝑒 ℎ𝑎𝑠𝑟𝑒𝑡 𝑘𝑎𝑙𝑑ı', 
'𝐻𝑒𝑟 ş𝑒𝑦𝑖𝑛 𝑏𝑖𝑡𝑡𝑖ğ𝑖 𝑦𝑒𝑟𝑑𝑒 𝑏𝑒𝑛𝑑𝑒 𝑏𝑖𝑡𝑡𝑖𝑚 𝑑𝑒ğ𝑖ş𝑡𝑖𝑛 𝑑𝑖𝑦𝑒𝑛𝑙𝑒𝑟𝑖𝑛 𝑒𝑠𝑖𝑟𝑖𝑦𝑖𝑚', 
'𝐺ü𝑣𝑒𝑛𝑚𝑒𝑘 𝑠𝑒𝑣𝑚𝑒𝑘𝑡𝑒𝑛 𝑑𝑎ℎ𝑎 𝑑𝑒ğ𝑒𝑟𝑙𝑖, 𝑍𝑎𝑚𝑎𝑛𝑙𝑎 𝑎𝑛𝑙𝑎𝑟𝑠ı𝑛', 
'İ𝑛𝑠𝑎𝑛 𝑏𝑎𝑧𝑒𝑛 𝑏ü𝑦ü𝑘 ℎ𝑎𝑦𝑒𝑙𝑙𝑒𝑟𝑖𝑛𝑖 𝑘üçü𝑘 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟𝑙𝑎 𝑧𝑖𝑦𝑎𝑛 𝑒𝑑𝑒𝑟', 
'𝐾𝑖𝑚𝑠𝑒 𝑘𝑖𝑚𝑠𝑒𝑦𝑖 𝑘𝑎𝑦𝑏𝑒𝑡𝑚𝑒𝑧 𝑔𝑖𝑑𝑒𝑛 𝑏𝑎ş𝑘𝑎𝑠ı𝑛ı 𝑏𝑢𝑙𝑢𝑟, 𝑘𝑎𝑙𝑎𝑛 𝑘𝑒𝑛𝑑𝑖𝑛𝑖', 
'𝐺üç𝑙ü 𝑔ö𝑟ü𝑛𝑒𝑏𝑖𝑙𝑖𝑟𝑖𝑚 𝑎𝑚𝑎 𝑖𝑛𝑎𝑛 𝑏𝑎𝑛𝑎 𝑦𝑜𝑟𝑔𝑢𝑛𝑢𝑚', 
'Ö𝑚𝑟ü𝑛ü𝑧ü 𝑠𝑢𝑠𝑡𝑢𝑘𝑙𝑎𝑟ı𝑛ı𝑧ı 𝑑𝑢𝑦𝑎𝑛  𝑏𝑖𝑟𝑖𝑦𝑙𝑒 𝑔𝑒ç𝑖𝑟𝑖𝑛', 
'𝐻𝑎𝑦𝑎𝑡 𝑖𝑙𝑒𝑟𝑖𝑦𝑒 𝑏𝑎𝑘ı𝑙𝑎𝑟𝑎𝑘 𝑦𝑎ş𝑎𝑛ı𝑟 𝑔𝑒𝑟𝑖𝑦𝑒 𝑏𝑎𝑘𝑎𝑟𝑎𝑘 𝑎𝑛𝑙𝑎şı𝑙ı𝑟', 
'𝐴𝑟𝑡ı𝑘 ℎ𝑖ç𝑏𝑖𝑟 ş𝑒𝑦 𝑒𝑠𝑘𝑖𝑠𝑖 𝑔𝑖𝑏𝑖 𝑑𝑒ğ𝑖𝑙 𝐵𝑢𝑛𝑎 𝑏𝑒𝑛𝑑𝑒 𝑑𝑎ℎ𝑖𝑙𝑖𝑚', 
'𝐾ı𝑦𝑚𝑒𝑡 𝑏𝑖𝑙𝑒𝑛𝑒 𝑔ö𝑛ü𝑙𝑑𝑒 𝑣𝑒𝑟𝑖𝑙𝑖𝑟 ö𝑚ü𝑟𝑑𝑒', 
'𝐵𝑖𝑟 ç𝑖ç𝑒𝑘𝑙𝑒 𝑔ü𝑙𝑒𝑟 𝑘𝑎𝑑ı𝑛 𝑏𝑖𝑟 𝑙𝑎𝑓𝑙𝑎 ℎü𝑧ü𝑛', 
'𝑈𝑠𝑙ü𝑝 𝑘𝑎𝑟𝑎𝑘𝑡𝑒𝑟𝑖𝑑𝑖𝑟 𝑖𝑛𝑠𝑎𝑛ı𝑛', 
'𝐻𝑒𝑟 ş𝑒𝑦𝑖 𝑏𝑖𝑙𝑒𝑛 𝑑𝑒ğ𝑖𝑙 𝑘ı𝑦𝑚𝑒𝑡 𝑏𝑖𝑙𝑒𝑛 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟 𝑜𝑙𝑠𝑢𝑛 ℎ𝑎𝑦𝑎𝑡ı𝑛ı𝑧𝑑𝑎', 
'𝑀𝑒𝑠𝑎𝑓𝑒 𝑖𝑦𝑖𝑑𝑖𝑟 𝑁𝑒 ℎ𝑎𝑑𝑑𝑖𝑛𝑖 𝑎ş𝑎𝑛 𝑜𝑙𝑢𝑟 𝑛𝑒 𝑑𝑒 𝑐𝑎𝑛ı𝑛ı 𝑠ı𝑘𝑎𝑛', 
'𝑌ü𝑟𝑒ğ𝑖𝑚𝑖𝑛 𝑡𝑎𝑚 𝑜𝑟𝑡𝑎𝑠ı𝑛𝑑𝑎 𝑏ü𝑦ü𝑘 𝑏𝑖𝑟 𝑦𝑜𝑟𝑔𝑢𝑛𝑙𝑢𝑘 𝑣𝑎𝑟', 
'𝑉𝑒𝑟𝑖𝑙𝑒𝑛 𝑑𝑒ğ𝑒𝑟𝑖𝑛 𝑛𝑎𝑛𝑘ö𝑟ü 𝑜𝑙𝑚𝑎𝑦ı𝑛 𝑔𝑒𝑟𝑖𝑠𝑖 ℎ𝑎𝑙𝑙𝑜𝑙𝑢𝑟', 
'𝐻𝑒𝑚 𝑔üç𝑙ü 𝑜𝑙𝑢𝑝 ℎ𝑒𝑚 ℎ𝑎𝑠𝑠𝑎𝑠 𝑘𝑎𝑙𝑝𝑙𝑖 𝑏𝑖𝑟𝑖 𝑜𝑙𝑚𝑎𝑘 ç𝑜𝑘 𝑧𝑜𝑟', 
'𝑀𝑢ℎ𝑡𝑎ç 𝑘𝑎𝑙ı𝑛 𝑦ü𝑟𝑒ğ𝑖 𝑔ü𝑧𝑒𝑙 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟𝑎', 
'İ𝑛𝑠𝑎𝑛 𝑎𝑛𝑙𝑎𝑑ığı 𝑣𝑒 𝑎𝑛𝑙𝑎şı𝑙𝑑ığı 𝑖𝑛𝑠𝑎𝑛𝑑𝑎 ç𝑖ç𝑒𝑘 𝑎ç𝑎𝑟', 
'İ𝑠𝑡𝑒𝑦𝑒𝑛 𝑑𝑎ğ𝑙𝑎𝑟ı 𝑎ş𝑎𝑟 𝑖𝑠𝑡𝑒𝑚𝑒𝑦𝑒𝑛 𝑡ü𝑚𝑠𝑒ğ𝑖 𝑏𝑖𝑙𝑒 𝑔𝑒ç𝑒𝑚𝑒𝑧', 
'İ𝑛ş𝑎𝑙𝑙𝑎ℎ 𝑠𝑎𝑏ı𝑟𝑙𝑎 𝑏𝑒𝑘𝑙𝑒𝑑𝑖ğ𝑖𝑛 ş𝑒𝑦 𝑖ç𝑖𝑛 ℎ𝑎𝑦ı𝑟𝑙ı 𝑏𝑖𝑟 ℎ𝑎𝑏𝑒𝑟 𝑎𝑙ı𝑟𝑠ı𝑛', 
'İ𝑦𝑖 𝑜𝑙𝑎𝑛 𝑘𝑎𝑦𝑏𝑒𝑡𝑠𝑒 𝑑𝑒 𝑘𝑎𝑧𝑎𝑛ı𝑟', 
'𝐺ö𝑛𝑙ü𝑛ü𝑧𝑒 𝑎𝑙𝑑ığı𝑛ı𝑧 𝑔ö𝑛𝑙ü𝑛ü𝑧ü 𝑎𝑙𝑚𝑎𝑦ı 𝑏𝑖𝑙𝑠𝑖𝑛', 
'𝑌𝑖𝑛𝑒 𝑦ı𝑟𝑡ı𝑘 𝑐𝑒𝑏𝑖𝑚𝑒 𝑘𝑜𝑦𝑚𝑢ş𝑢𝑚 𝑢𝑚𝑢𝑑𝑢', 
'Ö𝑙𝑚𝑒𝑘 𝐵𝑖 ş𝑒𝑦 𝑑𝑒ğ𝑖𝑙 𝑦𝑎ş𝑎𝑚𝑎𝑚𝑎𝑘 𝑘𝑜𝑟𝑘𝑢𝑛ç', 
'𝑁𝑒 𝑖ç𝑖𝑚𝑑𝑒𝑘𝑖 𝑠𝑜𝑘𝑎𝑘𝑙𝑎𝑟𝑎 𝑠ığ𝑎𝑏𝑖𝑙𝑑𝑖𝑚 𝑁𝑒 𝑑𝑒 𝑑ış𝑎𝑟ı𝑑𝑎𝑘𝑖 𝑑ü𝑛𝑦𝑎𝑦𝑎', 
'İ𝑛𝑠𝑎𝑛 𝑠𝑒𝑣𝑖𝑙𝑚𝑒𝑘𝑡𝑒𝑛 ç𝑜𝑘 𝑎𝑛𝑙𝑎şı𝑙𝑚𝑎𝑦ı 𝑖𝑠𝑡𝑖𝑦𝑜𝑟𝑑𝑢 𝑏𝑒𝑙𝑘𝑖 𝑑𝑒', 
'𝐸𝑘𝑚𝑒𝑘 𝑝𝑎ℎ𝑎𝑙ı 𝑒𝑚𝑒𝑘 𝑢𝑐𝑢𝑧𝑑𝑢', 
'𝑆𝑎𝑣𝑎ş𝑚𝑎𝑦ı 𝑏ı𝑟𝑎𝑘ı𝑦𝑜𝑟𝑢𝑚 𝑏𝑢𝑛𝑢 𝑣𝑒𝑑𝑎 𝑠𝑎𝑦'
) 


@client.on(events.NewMessage(pattern="^/soztag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("Bu komutu sadece grup veya kanallarda kullanabilirsiniz.")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔️ Bu komutu sadece yöneticiler kullanabilir!**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski Mesajlar için Üyelerden Bahsedemem! (gruba eklemeden önce gönderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**ℹ️ Lütfen bir etiket sebebi yazın veya bir mesajı yanıtlayarak komutu girin.**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Etiket işlemi başladı.**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(soz)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"\n📣 - [{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiket Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(soz)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiket Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")



gisim = ['Üzümlü kek ✨', 'Nar çiçeği ✨', 'Papatya 🌼', 'Karanfil ✨', 'Gül 🌹', 'Ayıcık 🐻', 'Mutlu panda 🐼', 'Ay pare ✨', 'Ballı lokma ✨', 'Lale 🌷', 'Zambak ⚜', 'Nergis ✨', 'Sümbül ☘️', 'Nilüfer ☘️', 'Menekşe ⚜️', 'Lavanta ✨', 'Gül pare ✨', 'Reyhan 🌷', 'Kaktüs ⚜️', 'Böğürtlen ☘️', 'Orkide ☘️', 'Manolya ✨', 'Ayçiçeği ✨', 'Tweety 🐥', 'Star ✨', 'Yonca 🍀', 'Ateş böceği ✨',]

#güzel isimler @Samilben tarafından.

@client.on(events.NewMessage(pattern="^/gisimtag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("Bu komutu sadece grup veya kanallarda kullanabilirsiniz.")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔️ Bu komutu sadece yöneticiler kullanabilir!**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski Mesajlar için Üyelerden Bahsedemem! (gruba eklemeden önce gönderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**ℹ️ Lütfen bir etiket sebebi yazın veya bir mesajı yanıtlayarak komutu girin.**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Etiket işlemi başladı.**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(gisim)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"\n📣 - [{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiket Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(gisim)}](tg://user?id={usr.id})"
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiket Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")





emoji = "🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍧 🍨".split(" ")


@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("Bu komutu sadece grup veya kanallarda kullanabilirsiniz.")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔️ Bu komutu sadece yöneticiler kullanabilir!**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski Mesajlar için Üyelerden Bahsedemem! (gruba eklemeden önce gönderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**ℹ️ Lütfen bir etiket sebebi yazın veya bir mesajı yanıtlayarak komutu girin.**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Etiket işlemi başladı.**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"\n📣🔮 - [{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiket Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"\n📣 - [{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiket Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")


@client.on(events.NewMessage(pattern="^/utag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("Bu komutu sadece grup veya kanallarda kullanabilirsiniz.")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔️ Bu komutu sadece yöneticiler kullanabilir!**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski Mesajlar için Üyelerden Bahsedemem! (gruba eklemeden önce gönderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**ℹ️ Lütfen bir etiket sebebi yazın veya bir mesajı yanıtlayarak komutu girin.**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Etiket işlemi başladı.**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n📣 - [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"\n📣 - [{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiket Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"📣 - [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiket Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")

@client.on(events.NewMessage(pattern="^/atag ?(.*)"))
async def mentionalladmin(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu komutu sadece grup veya kanallarda kullanabilirsin.**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔️ Bu komutu sadece yöneticiler kullanabilir!**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski Mesajlar için Üyelerden Bahsedemem! (gruba eklemeden önce gönderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**ℹ️ Lütfen bir etiket sebebi yazın veya bir mesajı yanıtlayarak komutu girin.**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Etiket işlemi başladı.**")
  
    async for usr in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("Etiket İşlemi Bitti 🤗")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n\n{usrtxt}")
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
      usrnum += 1
      usrtxt += f"\n[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**✅ Etiket işlemi durduruldu.**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""

    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiket Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")



@client.on(events.NewMessage(pattern="^/riviatag ?(.*)"))
async def mentionall(event):
  global anlik_calisan,ozel_list
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("Bu komutu sadece grup veya kanallarda kullanabilirsiniz.")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in ozel_list:
    return await event.respond("**⛔️👨🏻‍💻 Bu komutu sadece bot yöneticileri kullanabilir!**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski Mesajlar için Üyelerden Bahsedemem! (gruba eklemeden önce gönderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**ℹ️ Lütfen bir etiket sebebi yazın veya bir mesajı yanıtlayarak komutu girin.**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Etiket işlemi başladı.**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n📣 - [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(1.5)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"\n📣 - [{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiket Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"📣 - [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(1.5)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiket Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")

@client.on(events.NewMessage(pattern="^/atag ?(.*)"))
async def mentionalladmin(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu komutu sadece grup veya kanallarda kullanabilirsin.**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔️ Bu komutu sadece yöneticiler kullanabilir!**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski Mesajlar için Üyelerden Bahsedemem! (gruba eklemeden önce gönderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**ℹ️ Lütfen bir etiket sebebi yazın veya bir mesajı yanıtlayarak komutu girin.**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Etiket işlemi başladı.**")
  
    async for usr in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("Etiket İşlemi Bitti 🤗")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n\n{usrtxt}")
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
      usrnum += 1
      usrtxt += f"\n[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**✅ Etiket işlemi durduruldu.**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""

    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiket Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")





@client.on(events.NewMessage(pattern="^/tektag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("Bu komutu sadece grup veya kanallarda kullanabilirsiniz.")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔️ Bu komutu sadece yöneticiler kullanabilir!**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski Mesajlar için Üyelerden Bahsedemem! (gruba eklemeden önce gönderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**ℹ️ Lütfen bir etiket sebebi yazın veya bir mesajı yanıtlayarak komutu girin.**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Etiket işlemi başladı.**")
    
        #Samil iş başında
        #Samilben
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"📣 - [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"\n📣 - [{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiket Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"📣 - [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiket Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")

@client.on(events.NewMessage(pattern='^/stats ?(.*)'))
async def son_durum(event):
    global anlik_calisan,grup_sayi,ozel_list
    sender = await event.get_sender()
    if sender.id not in ozel_list:
      return
    await event.respond(f"**VipTagger İstatistikleri 🤖**\n\nToplam Grup: `{len(grup_sayi)}`\nAnlık Çalışan Grup: `{len(anlik_calisan)}`")


@client.on(events.NewMessage(pattern='^/reklam ?(.*)'))
async def duyuru(event):
 
  global grup_sayi,ozel_list
  sender = await event.get_sender()
  if sender.id not in ozel_list:
    return
  reply = await event.get_reply_message()
  await event.respond(f"Toplam {len(grup_sayi)} Gruba'a mesaj gönderiliyor...")
  for x in grup_sayi:
    try:
      await client.send_message(x,f"**{reply.message}**")
    except:
      pass
  await event.respond(f"Gönderildi.")

@client.on(events.NewMessage(pattern='^/botcum'))
async def event(ups):
  if ups.sender_id == 641319713:
    await ups.reply("**Selam Şamil! Şu an çalışmaktayım. ✨**")
  else:
    await ups.reply("**Sizi tanımıyorum. 🧐**")




################## KULLANICI KONTROLLERİ #############
async def handle_user_status(bot: Client, cmd: Message): # Kullanıcı kontrolü
    chat_id = cmd.chat.id
    if not await db.is_user_exist(chat_id):
        if cmd.chat.type == "private":
            await db.add_user(chat_id)
            await bot.send_message(LOG_CHANNEL,LAN.BILDIRIM.format(cmd.from_user.first_name, cmd.from_user.id, cmd.from_user.first_name, cmd.from_user.id))
        else:
            await db.add_user(chat_id)
            chat = bot.get_chat(chat_id)
            if str(chat_id).startswith("-100"):
                new_chat_id = str(chat_id)[4:]
            else:
                new_chat_id = str(chat_id)[1:]
            await bot.send_message(LOG_CHANNEL,LAN.GRUP_BILDIRIM.format(cmd.from_user.first_name, cmd.from_user.id, cmd.from_user.first_name, cmd.from_user.id, chat.title, cmd.chat.id, cmd.chat.id, cmd.message_id))

    ban_status = await db.get_ban_status(chat_id) # Yasaklı Kullanıcı Kontrolü
    if ban_status["is_banned"]:
        if int((datetime.date.today() - datetime.date.fromisoformat(ban_status["banned_on"])).days) > int(ban_status["ban_duration"]):
            await db.remove_ban(chat_id)
        else:
            if GROUP_SUPPORT:
                msj = f"@{GROUP_SUPPORT}"
            else:
                msj = f"[{LAN.SAHIBIME}](tg://user?id={OWNER_ID})"
            if cmd.chat.type == "private":
                await cmd.reply_text(LAN.PRIVATE_BAN.format(msj), quote=True)
            else:
                await cmd.reply_text(LAN.GROUP_BAN.format(msj),quote=True)
                await bot.leave_chat(cmd.chat.id)
            return
    await cmd.continue_propagation()




############### Broadcast araçları ###########
broadcast_ids = {}


async def send_msg(user_id, message): # Mesaj Gönderme
    try:
        if GONDERME_TURU is False:
            await message.forward(chat_id=user_id)
        elif GONDERME_TURU is True:
            await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(int(e.x))
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id}: {LAN.NOT_ONLINE}\n"
    except UserIsBlocked:
        return 400, f"{user_id}: {LAN.BOT_BLOCKED}\n"
    except PeerIdInvalid:
        return 400, f"{user_id}: {LAN.USER_ID_FALSE}\n"
    except Exception:
        return 500, f"{user_id}: {traceback.format_exc()}\n"

async def main_broadcast_handler(m, db): # Ana Broadcast Mantığı
    all_users = await db.get_all_users()
    broadcast_msg = m.reply_to_message
    while True:
        broadcast_id = "".join(random.choice(string.ascii_letters) for i in range(3))
        if not broadcast_ids.get(broadcast_id):
            break
    out = await m.reply_text(
        text=LAN.BROADCAST_STARTED)
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    failed = 0
    success = 0
    broadcast_ids[broadcast_id] = dict(total=total_users, current=done, failed=failed, success=success)
    async with aiofiles.open("broadcast-logs-Samilbots.txt", "w") as broadcast_log_file:
        async for user in all_users:
            sts, msg = await send_msg(user_id=int(user["id"]), message=broadcast_msg)
            if msg is not None:
                await broadcast_log_file.write(msg)
            if sts == 200:
                success += 1
            else:
                failed += 1
            if sts == 400:
                await db.delete_user(user["id"])
            done += 1
            if broadcast_ids.get(broadcast_id) is None:
                break
            else:
                broadcast_ids[broadcast_id].update(
                    dict(current=done, failed=failed, success=success))
    if broadcast_ids.get(broadcast_id):
        broadcast_ids.pop(broadcast_id)
    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await asyncio.sleep(3)
    await out.delete()
    if failed == 0:
        await m.reply_text(text=LAN.BROADCAST_STOPPED.format(completed_in, total_users, done, success, failed), quote=True,)
    else:
        await m.reply_document(document="broadcast-logs-Samilbots.txt", caption=LAN.BROADCAST_STOPPED.format(completed_in, total_users, done, success, failed), quote=True,)
    os.remove("broadcast-logs-Samilbots.txt")





# Botu ilk başlatan kullanıcıların kontrolünü sağlar.
@app.on_message()
async def G4RIP(bot: Client, cmd: Message):
    await handle_user_status(bot, cmd)



# Broadcast komutu
@app.on_message(filters.command("broadcast") & filters.user(OWNER_ID) & filters.reply)
async def broadcast_handler_open(_, m: Message):
    await main_broadcast_handler(m, db)



# Bir kullanıcı yasaklama komutu
@app.on_message(filters.command("block") & filters.user(OWNER_ID))
async def ban(c: Client, m: Message):
    if m.reply_to_message:
        user_id = m.reply_to_message.from_user.id
        if len(m.command) <= 1:
            ban_duration = 9999
            ban_reason = LAN.BAN_REASON.format(USERNAME)
        elif len(m.command) == 2:
            ban_duration = 9999
            ban_reason = " ".join(m.command[1:])
    else:
        if len(m.command) <= 1:
            return await m.reply(LAN.NEED_USER)
        elif len(m.command) == 2:
            user_id = int(m.command[1])
            ban_duration = 9999
            ban_reason = LAN.BAN_REASON.format(USERNAME)
        elif len(m.command) == 3:
            user_id = int(m.command[1])
            ban_duration = 9999
            ban_reason = " ".join(m.command[2:])
    
        if str(user_id).startswith("-"):
            try:    
                ban_log_text = LAN.BANNED_GROUP.format(m.from_user.mention, user_id, ban_duration, ban_reason)
                await c.send_message(user_id, LAN.AFTER_BAN_GROUP.format(ban_reason))
                await c.leave_chat(user_id)
                ban_log_text += LAN.GROUP_BILGILENDIRILDI
            except BaseException:
                traceback.print_exc()
                ban_log_text += LAN.GRUP_BILGILENDIRILEMEDI.format(traceback.format_exc())
        else:
            try:    
                ban_log_text = LAN.USER_BANNED.format(m.from_user.mention, user_id, ban_duration, ban_reason)
                await c.send_message(user_id, LAN.AFTER_BAN_USER.format(ban_reason))
                ban_log_text += LAN.KULLANICI_BILGILENDIRME
            except BaseException:
                traceback.print_exc()
                ban_log_text += LAN.KULLANICI_BILGILENDIRMEME.format(traceback.format_exc())
        await db.ban_user(user_id, ban_duration, ban_reason)
        await c.send_message(LOG_CHANNEL, ban_log_text)
        await m.reply_text(ban_log_text, quote=True)



# Bir kullanıcın yasağını kaldırmak komutu
@app.on_message(filters.command("unblock") & filters.user(OWNER_ID))
async def unban(c: Client, m: Message):
        if m.reply_to_message:
            user_id = m.reply_to_message.from_user.id
        else:
            if len(m.command) <= 1:
                return await m.reply(LAN.NEED_USER)
            else:
                user_id = int(m.command[1])
        unban_log_text = LAN.UNBANNED_USER.format(m.from_user.mention, user_id)
        if not str(user_id).startswith("-"):
            try:
                await c.send_message(user_id, LAN.USER_UNBAN_NOTIFY)
                unban_log_text += LAN.KULLANICI_BILGILENDIRME
            except BaseException:
                traceback.print_exc()
                unban_log_text += LAN.KULLANICI_BILGILENDIRMEME.format(traceback.format_exc())
        await db.remove_ban(user_id)
        await c.send_message(LOG_CHANNEL, unban_log_text)
        await m.reply_text(unban_log_text, quote=True)



# Yasaklı listesini görme komutu
@app.on_message(filters.command("blocklist") & filters.user(OWNER_ID))
async def _banned_usrs(_, m: Message):
    all_banned_users = await db.get_all_banned_users()
    banned_usr_count = 0
    text = ""
    async for banned_user in all_banned_users:
        user_id = banned_user["id"]
        ban_duration = banned_user["ban_status"]["ban_duration"]
        banned_on = banned_user["ban_status"]["banned_on"]
        ban_reason = banned_user["ban_status"]["ban_reason"]
        banned_usr_count += 1
        text += LAN.BLOCKS.format(user_id, ban_duration, banned_on, ban_reason)
    reply_text = LAN.TOTAL_BLOCK.format(banned_usr_count, text)
    if len(reply_text) > 4096:
        with open("banned-user-list.txt", "w") as f:
            f.write(reply_text)
        await m.reply_document("banned-user-list.txt", True)
        os.remove("banned-user-list.txt")
        return
    await m.reply_text(reply_text, True)



############## BELİRLİ GEREKLİ DEF'LER ###########
def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "K", 2: "M", 3: "G", 4: "T"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"




app.run()
print(">> Bot çalışıyor @samilben Tarafından Kuruldu<<")
client.run_until_disconnected()
