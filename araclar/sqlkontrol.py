import os
import requests
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)
os.system("clear")
def is_sql_injection_vulnerable(url):
    dangerous_characters = ["'", "\"", ";", "--"]
    
    for char in dangerous_characters:
        test_url = url + char
        try:
            response = requests.get(test_url)
            response.raise_for_status()
            if "error" in response.text.lower():
                return True
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"Hata: {e}")
            return False
    
    return False

def ayristirma():
    print("\n")
    print(Fore.BLUE + Style.BRIGHT +" SQL injection kontrol işlemi başlatıldı lütfen bekleyiniz..."+ Fore.RESET )
    print("\n")
    mevcut_dizin = os.getcwd()
    ust_dizin = os.path.dirname(mevcut_dizin)
    
    hedef_dizin1 = "Hangar"
    hedef_dizin2 = "dorksonuç"
    gelen_dosya = "dorksonuç.txt"
    input_file_name = os.path.join(ust_dizin, hedef_dizin1, hedef_dizin2, gelen_dosya)
    
    hedef_dizin2 = "sqlsonuç"
    hedef_dosya = "sqlsonuç.txt"
    output_file_name = os.path.join(ust_dizin, hedef_dizin1, hedef_dizin2, hedef_dosya)
    
    try:
        with open(input_file_name, "r") as input_file:
            urls = input_file.readlines()
    except FileNotFoundError:
        print(f"'{input_file_name}' dosyası bulunamadı.")
        exit(1)
    
    with open(output_file_name, "w") as output_file:
        for url in urls:
            url = url.strip()
            
            if is_sql_injection_vulnerable(url):
                result = url + "\n"
                output_file.write(result)
                print(Fore.GREEN + f"{url}" + Fore.RESET + Fore.BLUE + "  - SQL injection açığı var.")
            else:
                # Sadece URL'leri yazdır
                print(Fore.WHITE + f"{url}")
    

    print("Tarama tamamlandı. Açık olan sitelerin sonuçları 'Hangar/sqlsonuç/sqlsonuç.txt' dosyasına kaydedildi.")
if __name__ == "__main__":
    try:
        ayristirma()
    except KeyboardInterrupt:
        # CTRL+C ile işlem kesildiğinde burada uygun temizlik işlemleri yapılabilir.
        print("Kullanıcı tarafından işlem kesildi.")
