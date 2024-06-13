import os
try:
  import random
  import requests
  from threading import Thread
  from time import sleep as zzz
  from faker import Faker
  from ms4 import InfoIG
  from ms4 import Instagram
  from ms4 import RestInsta
  from ms4 import UserAgentGenerator
except:
	os.system("pip install faker")
	os.system("pip install ms4==2.10.0")
	
import random
import requests
from threading import Thread
from time import sleep as zzz
from faker import Faker
from ms4 import InfoIG
from ms4 import Instagram
from ms4 import RestInsta
from ms4 import UserAgentGenerator
E = '\033[1;31m'
X = '\033[1;33m'
F = '\033[2;32m'
M = '\x1b[1;37m'
B = '\x1b[38;5;208m'
memo = random.randint(100, 300)
O = f'\x1b[38;5;{memo}m'

print(f'''{B}{E}=============================={B}
|{F}[+] YouTube    : {B}
|{F}[+] TeleGram   : {B} 🔱WRX🔱ƦƠԼЄҲ
|{F}[+] Instagram  : {B} 
|{F}[+] Tool       : {B} VIP İNSTA|
{E}==============================''')

token = input(f' {F}({M}1{F}) {M} Enter Token Telegram @BotFather{F}  ' + O)
print(X + ' ═════════════════════════════════  ')
ID = input(f' {F}({M}2{F}) {M} Enter Chat ID{F}  ' + O)

def Tele(email):
    user = email.split("@")[0]
    try:
        rest = RestInsta.Rest(user)["email"]
    except:
        rest = "Nothing To Rest"

    inf = InfoIG.Instagram_Info(user)
    name = inf["Name"]
    Id = inf["ID"]
    fols = inf["Followers"]
    folg = inf["Following"]
    bio = inf["Bio"]
    po = inf["Posts"]
    pr = inf["Is Private"]

    tlg = f'''
⋘─────━*🔱WRX🔱ƦƠԼЄҲ*━─────⋙
[💌] Email ==> {email}
[💬] Email Rest ==> {rest}
[👻] Username ==> @{user}
[👱🏻] Name ==> {name}
[🔺] ID ==> {Id}
[🔁] Followers ==> {fols}
[🔂] Following ==> {folg}
[📺] Bio ==> {bio}
[🎥] Posts ==> {po}
[📲] Is Private ==> {pr}
[↩️] URL ==> https://www.instagram.com/{user}
⋘─────━❤️🌚━─────⋙
𝐁𝐘 : @dijvarhack 
'''
    print(F+tlg)
    requests.post(f"https://api.telegram.org/bot{token}/sendPhoto?chat_id={ID}&text={tlg}")

    with open('hits.txt', 'a') as f:
        f.write(tlg + '\n')

def Ch(email):
    IG = Instagram.CheckInsta(email)['Is_Available']
    if IG == 'true':
        print(f"{F}Good Email Hunt Insta : {email}")
        Tele(email)
    elif IG == 'false':
        print(f"{E}Bad Email : {email}")
    else:
        print("Turn VPN")
        zzz(10)

def Men():
    while True:
        try:
            faker = Faker()
            NEHAHHH = faker.user_name()  
            lsd = ''.join(random.choice('eQ6xuzk5X8j6_fGvb0gJrc') for _ in range(16))
            id = str(random.randrange(10000, 7407225345))
            headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/0s9s/',
                'user-agent': str(UserAgentGenerator()),
                'x-fb-lsd': 'mahos' + lsd,
            }
            data = {
                'lsd': 'mahos' + lsd,
                'variables': '{"id":"' + id + '","relay_header":false,"render_surface":"PROFILE"}',
                'doc_id': '7397388303713986',
            }
            NN = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data).json()
            Fuck = NN['data']['user']['username']
        except:
            Fuck = NEHAHHH
            pass
            HH = ''.join(random.choice('zxvcbnmlkjhgfdsapoiuyrtewq') for i in range(4))                      
            name = random.choice([HH, NEHAHHH, Fuck])
            email = name + "@gmail.com"
            Ch(email)

for i in range(5):
    Thread(target=Men).start()
