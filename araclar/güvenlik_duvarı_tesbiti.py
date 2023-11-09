#!/usr/bin/env python
import os
from termcolor import colored

def main():
    while True:
        print("\n")
        print(colored(" INOVA Güvenlik duvarı tesbiti aracına hoş geldiniz", 'red', attrs=['bold']))
        print("\n")
        print("1) Güvenlik duvarı tespitini başlat")
        print("2) Çıkış")
        choice = input("Seçiminizi yapın: ")

        if choice == '1':
            site = input("Site adresi giriniz: ")  # Site adresini burada almalısınız.
            os.system("wafw00f " + site)
        elif choice == '2':
            print("Programdan çıkılıyor.")
            break
        else:
            print("Geçersiz seçim. Lütfen 1 veya 2 seçin.")

if __name__ == "__main__":
    main()
