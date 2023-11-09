#!/usr/bin/env python
import os
from termcolor import colored

# chkrootkit kurulumunu root yetkileri ile yapmak için sudo ekledik.
#os.system("sudo apt-get install chkrootkit")
os.system("clear")
def main():
    while True:
        print("\n")
        print(colored(" INOVA rootkit tarama aracına hoş geldiniz", 'red', attrs=['bold']))
        print("\n")
        print("1) Rootkit taraması başlat")
        print("2) Çıkış")
        choice = input("Seçiminizi yapın: ")

        if choice == "1":
            os.system("chkrootkit")
        elif choice == "2":
            print("Programdan çıkılıyor.")
            break
        else:
            print("Geçersiz seçim. Lütfen 1 veya 2 seçin.")
print("\n")
if __name__ == "__main__":
    main()
print("\n")
