import telebot
import requests
#Kaizer Sorgu

TOKEN = "BOT_TOKEN"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def botu_baslatma(message):
    bot.reply_to(message, "@Kaizercheck Sorgu Bot'una Hoş geldiniz! Komutlar için /komut Yapın.")

@bot.message_handler(commands=['komut'])
def send_help_message(message):
    bot.reply_to(message, """
/adres komutu ile TC'den Adres Bulabilirsin.
/tc komutu kullanarak Kişi Bilgi Alabilirsin.
/sorgu komutu ile -Ad -Soyad -İl -İlce Sorgulama Yapar.
/aile komutu kullanarak aile sorgulama yapar.
/ipadres ile ip sorgu yapabilirsiniz.
/gsm ile Tel No Sorgulayabilirsiniz.
    """)

@bot.message_handler(commands=['adres'])
def adress_sorgu(message):
    try:
        chat_id = message.chat.id
        tc_number = message.text.split()[1]

        url = f"https://sowixapi.online/api/sowixapi/adres.php?tc={tc_number}"
        response = requests.get(url)
        data = response.json()

        if "success" in data and data["success"]:
            adres_data = data["data"]
            adres_message = f"""
Kimlik No: {adres_data["KimlikNo"]}
Ad Soyad: {adres_data["AdSoyad"]}
Doğum Yeri: {adres_data["DogumYeri"]}
Vergi Numarası: {adres_data["VergiNumarasi"]}
İkametgah: {adres_data["Ikametgah"]}
"""

            bot.reply_to(message, adres_message)
        else:
            bot.reply_to(message, "Bu TC numarasına ait adres bilgisi bulunamadı.")
    except IndexError:
        bot.reply_to(message, "Geçersiz komut. kullanım: /adres 12345678901")



@bot.message_handler(commands=['tc'])
def tc_sorgu(message):
    try:
        chat_id = message.chat.id
        tc_number = message.text.split()[1]

        url = f"https://sowixapi.online/api/sowixapi/tcpro.php?tc={tc_number}"
        response = requests.get(url)
        data = response.json()

        if "tc" in data:
            tc = data["tc"]
            ad = data["adı"]
            soyad = data["soyadı"]
            dogum_tarihi = data["dogumtarihi"]
            yas = data["yaş"]
            anne_ad = data["annead"]
            anne_tc = data["annetc"]
            baba_ad = data["babaad"]
            baba_tc = data["babatc"]
            il = data["il"]
            ilce = data["ilce"]
            gsm = data["gsm"]

            response_message = f"""
TC: {tc}
Ad: {ad}
Soyad: {soyad}
Doğum Tarihi: {dogum_tarihi}
Yaş: {yas}
Anne Adı: {anne_ad}
Anne TC: {anne_tc}
Baba Adı: {baba_ad}
Baba TC: {baba_tc}
İl: {il}
İlçe: {ilce}
"""
            bot.reply_to(message, response_message)
        else:
            bot.reply_to(message, "Bu TC numarasına ait veri bulunamadı.")
    except IndexError:
        bot.reply_to(message, "Geçersiz komut. kullanım: /tc 12345678901")

@bot.message_handler(commands=['sorgu'])
def kimlik_sorgu(message):
    try:
        chat_id = message.chat.id
        parameters = ' '.join(message.text.split()[1:]).split('-')[1:]
        query = {}
        for param in parameters:
            key_value = param.split()
            if len(key_value) == 2:
                key, value = key_value
                key = key.strip().lower()
                query[key] = value.strip()
        
        if query:
            url = f"https://sowixapi.online/api/sowixapi/adsoyadilce.php?{'&'.join([f'{key}={value}' for key, value in query.items()])}"
            response = requests.get(url)
            data = response.json()

            if "status" in data and data["status"] == "success":
                person_info = ""
                for person_data in data["data"]:
                    for key, value in person_data.items():
                        person_info += f"{key.capitalize()}: {value}\n"
                    person_info += "\n\n"
                
                bot.reply_to(message, person_info)
            else:
                bot.reply_to(message, "Böyle bir kişi bilgisi bulunamadı.")
        else:
            bot.reply_to(message, "Geçersiz komut. kullanım: /sorgu -ad Adnan -soyad Oktar -il Karabük -ilce Merkez")
    except IndexError:
        bot.reply_to(message, "Geçersiz komut kullanım. /sorgu -ad Adnan -soyad Oktar -il Karabük -ilce Merkez")



@bot.message_handler(commands=['aile'])
def aile_sorgu(message):
    try:
        chat_id = message.chat.id
        tc_number = message.text.split()[1]

        url = f"https://sowixapi.online/api/sowixapi/aile.php?tc={tc_number}"
        response = requests.get(url)
        data = response.json()

        if "success" in data and data["success"]:
            family_info = ""
            for member_data in data["data"]:
                for key, value in member_data.items():
                    family_info += f"{key.capitalize()}: {value}\n"
                family_info += "\n"
            
            bot.reply_to(message, family_info)
        else:
            bot.reply_to(message, "Aile bilgisi bulunamadı.")
    except IndexError:
        bot.reply_to(message, "Geçersiz komut kullanım: /aile 12345678901")

@bot.message_handler(commands=['iban'])
def iban_sorgu(message):
    try:
        chat_id = message.chat.id
        iban = message.text.split()[1]

        url = f"https://sowixapi.online/api/sowixapi/iban.php?iban={iban}"
        response = requests.get(url)
        data = response.json()

        if "Kod" in data:
            iban_info = ""
            for key, value in data.items():
                iban_info += f"{key}: {value}\n"
            
            bot.reply_to(message, iban_info)
        else:
            bot.reply_to(message, "IBAN bilgisi bulunamadı.")
    except IndexError:
        bot.reply_to(message, "Geçersiz komut kullanımı. Örnek: /iban TR******")

def ip_sorgula(ip_adresi):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip_adresi}')
        data = response.json()
        country = data['country']
        city = data['city']
        region = data['regionName']
        isp = data['isp']
        latitude = data['lat']
        longitude = data['lon']
        timezone = data['timezone']
        zip_code = data['zip']
        return f"IP adresi: {ip_adresi}\nÜlke: {country}\nBölge: {region}\nŞehir: {city}\nZIP Kodu: {zip_code}\nISP: {isp}\nEnlem: {latitude}\nBoylam: {longitude}\nZaman Dilimi: {timezone}"
    except Exception as e:
        return f"ip Adresi Hatalı."

@bot.message_handler(commands=['ipadres'])
def handle_ipadres(message):
    try:
        ip_adresi = message.text.split()[1]
        ip_bilgi = ip_sorgula(ip_adresi)
        bot.reply_to(message, ip_bilgi)
    except Exception as e:
        bot.reply_to(message, f"bir ip Adresi Girmelisin.")


def gsm_sorgula(gsm_numarasi):
    try:
        url = f'http://4.227.159.255/api/legaliapi/gsmdetay.php?gsm={gsm_numarasi}'
        response = requests.get(url)
        data = response.json()
        
        if "success" in data and data["success"]:
            gsm_detay = data["Data"]
            gsm_mesaj = f"""
TC: {gsm_detay["TC"]}
Adı: {gsm_detay["ADI"]}
Soyadı: {gsm_detay["SOYADI"]}
Doğum Tarihi: {gsm_detay["DOGUMTARIHI"]}
Nüfus İl: {gsm_detay["NUFUSIL"]}
Nüfus İlçe: {gsm_detay["NUFUSILCE"]}
Anne Adı: {gsm_detay["ANNEADI"]}
Anne TC: {gsm_detay["ANNETC"]}
Baba Adı: {gsm_detay["BABAADI"]}
Baba TC: {gsm_detay["BABATC"]}
Uyruk: {gsm_detay["UYRUK"]}
"""
            return gsm_mesaj
        else:
            return "Bu GSM numarasına ait bilgi bulunamadı."
    except Exception as e:
        return f"GSM sorgulanırken bir hata oluştu."

@bot.message_handler(commands=['gsm'])
def handle_gsm(message):
    try:
        gsm_numarasi = message.text.split()[1]
        gsm_bilgi = gsm_sorgula(gsm_numarasi)
        bot.reply_to(message, gsm_bilgi)
    except Exception as e:
        bot.reply_to(message, f"Bir Tel No Girmelisin.")

bot.polling()
