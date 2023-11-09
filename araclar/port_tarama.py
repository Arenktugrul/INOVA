#!/usr/bin/env python
from termcolor import colored
import subprocess
import sys
print("\n")
def main():
    while True:  # Sonsuz bir döngü oluşturuyoruz
        #clear_screen()
	
        print(colored(" INOVA port tarama aracına hoş geldiniz", 'red', attrs=['bold']))
        print("""
        1) Hizli tarama
        2) Servis ve Versiyon bilgisi
        3) İşletim sistemi bilgisi
        4) Çıkış
        """)
        
        islemno = input("İşlem numarasını giriniz: ")

        if islemno == "1":
            target_ip = input("Hedef IP giriniz: ")
            subprocess.call(["nmap", target_ip])
        elif islemno == "2":
            target_ip = input("Hedef IP giriniz: ")
            subprocess.call(["nmap", "-sS", "-sV", target_ip])
        elif islemno == "3":
            target_ip = input("Hedef IP giriniz: ")
            subprocess.call(["nmap", "-O", target_ip])
        elif islemno == "4":
            print("Araçtan çıkılıyor.")
            break  # Döngüyü sonlandır
        else:
            print("Hatalı seçim yaptınız.")

if __name__ == "__main__":
    main()
print("\n")
print("\n")
