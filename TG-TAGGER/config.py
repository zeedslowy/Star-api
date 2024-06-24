import os
import heroku3
from telethon import TelegramClient, events

from pyrogram import Client
from pyrogram import filters
import logging
#
# Burayı gurcalama
# 
# 
#api_id = 24647583
#api_hash = "f41a6516ad6fba3b43d9cccd1f2c551c"
#bot_token = "6116997441:AAFF9bqrIam6UzGCi6BHoGV6U4gax0KtSRE"

# Telethon 
#client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
#
#USERNAME = "VTaggerBot"
group = -1001757359371
startmesaj = "**Ben grubunuzdaki üyeleri etiketleyebilen bir botum. Beni grubunuza alıp çalıştırabilirsiniz.**\n\n**Komutlar için /help yazın.**"
komutlar = "Komutlar:\n\n/utag -text- Kullanıcıları 5'li etiketlerim.\n/atag -text- Yöneticileri etiketlerim.\n/tektag Üyeleri tek tek etiketlerim.\n/etag - Üyeleri emoji ile etiketlerim.\n/soztag - Üyeleri sözler ile etiketlerim.\n/gisimtag - Üyeleri güzel isimlerle etiketlerim.\n/cancel - Etiket işlemini iptal ederim .\n\nYalnızca yöneticiler bu komutları kullanabilir."
qrupstart = "**Şu an aktif olarak çalışmaktayım.** 🕊🍃\n\n**Komutlar hakkında bilgi için /help yazın."
sahib = "SamilBen"
support = "developersohbet"
sahib = "samilben"
ozel_list = 5237976814
#
app = Client("GUNC",
             api_id=api_id,
             api_hash=api_hash,
             bot_token=bot_token
             )
