import subprocess
from termcolor import colored
import socket

def get_ip_from_domain(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror as e:
        return f"Hata: {e}"

def get_whois_info(target):
    try:
        result = subprocess.check_output(["whois", target], universal_newlines=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Hata: {e}"
print("\n")
def main():
    while True:
        print(colored(" INOVA pasif bilgi toplama aracına hoş geldiniz", 'red', attrs=['bold']))
        print("""
        1) Bilgi toplama aracını başlat
        2) Çıkış
        """)

        islemno = input("İşlem numarasını giriniz: ")

        if islemno == "1":
            hedef = input("Hedef IP veya alan adını giriniz: ")

            # Eğer hedef alan adıysa IP adresini al
            if not hedef.replace('.', '').isdigit():
                ip_adresi = get_ip_from_domain(hedef)
                print(f"{hedef} IP Adresi: {ip_adresi}")
                whois_info = get_whois_info(ip_adresi)
            else:
                whois_info = get_whois_info(hedef)

            print("\nWHOIS Bilgisi:")
            print(whois_info)
        elif islemno == "2":
            print("Araçtan çıkılıyor.")
            break
        else:
            print("Hatalı seçim yaptınız.")

if __name__ == "__main__":
    main()
