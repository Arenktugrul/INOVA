#!/usr/bin/env python
import os
import socket
from termcolor import colored

def get_ip_from_domain(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror as e:
        return f"Hata: {e}"
print("\n")
def main():
    print(colored(" INOVA Sunucu zafiyet analizi aracına hoş geldiniz", 'red', attrs=['bold']))
    print("\n")
    hedef_domain = input("Hedef domaini giriniz: ")

    # Domaini IP adresine çevir
    hedef_ip = get_ip_from_domain(hedef_domain)
    print(f"{hedef_domain} için IP Adresi: {hedef_ip}")

    os.system(f"nikto -h {hedef_ip}")

if __name__ == "__main__":
    main()
