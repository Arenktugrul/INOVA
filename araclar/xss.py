import requests
import colorama
from colorama import Fore, Style
from termcolor import colored
import os
colorama.init()

# Tarayıcı kullanıcı ajanı (User-Agent) başlığı
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'}

def xssfunc():
    os.system("clear")
    print(Fore.GREEN + """
     _  ____________
    | |/ / ___/ ___/
    |   /\__ \\__ \ 
   /   |___/ ___/ / 
  /_/|_/____/____/\n""" + Style.RESET_ALL)
    
    print("\n")
    print(colored(" INOVA xss kontrol aracına hoş geldiniz", 'blue', attrs=['bold']))
    # Saldırı türü belirleme: POST veya GET
    print("\n")
    attack_type = input("Saldırı türünü seçin (POST mu GET mi?) (p/g): ")

    if attack_type not in ["p", "g" , "G" , "P"]:
        print("Bilinmeyen bir seçenek, lütfen 'g' veya 'p' girin.")
        return
    print("\n")
    # Hedef URL'yi kullanıcıdan alın
    site = input("Hedef URL: ")
    try:
        req = requests.get(site)
        if req.status_code == 200:
            print(Fore.GREEN + "URL aktif\n" + Style.RESET_ALL)
        else:
            print(Fore.RED + "URL yanıt vermiyor")
            return
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Bir hata oluştu: {e}")
        return

    # Payload (saldırı vektörü) dosyasının yolu
    payload_file = input("Wordlist dosyasının yolu (araclar dosyası içerisinde xsslist.txt) :")
    try:
        with open(payload_file, "r") as payload_open:
            payloads = payload_open.read().splitlines()
    except FileNotFoundError:
        print(f"Dosya '{payload_file}' bulunamadı. Lütfen tekrar deneyin.")
        return

    print(Fore.YELLOW + "Saldırı işlemi devam ediyor\n" + Style.RESET_ALL)
    for payload in payloads:
        full_url = site + payload

        try:
            response = requests.get(full_url, headers=header)
            if payload in response.text:
                print(Fore.GREEN + f"XSS TESPİT EDİLDİ: {full_url}" + Style.RESET_ALL)
            else:
                print(f"{payload} için sonuç yok")
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"{full_url} için bir hata oluştu: {e}")

if __name__ == "__main__":
    xssfunc()
