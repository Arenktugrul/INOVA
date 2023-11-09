import os
import colorama
from termcolor import colored
from colorama import Fore, Back, Style
import time
import sys


colorama.init(autoreset=True)
calistirilan_dizin = os.getcwd()
dizin_yolu = calistirilan_dizin
a = (" .")
print("\n")

while True:
    os.system("clear")
    print(Fore.RED + Style.BRIGHT + "         _________"+ Fore.RESET + Fore.WHITE +"----- 🌟 -----"+ Fore.RESET + Fore.RED +"_________"+ Fore.RESET)
    print(Fore.BLUE + Style.BRIGHT +"""

        ██╗███╗   ██╗╔█████╗ ██╗ ██╗╔█████╗     
        ██║████╗  ██║██╔══██╗██║ ██║██╔══██╗    
        ██║██╔██╗ ██║██║  ██║██║ ██║███████║    
        ██║██║╚██╗██║██║  ██║██║ ██║██╔══██║    
        ██║██║ ╚████║╚█████╔╝╚████╔╝██║  ██║    
        ╚═╝╚═╝  ╚═══╝ ╚════╝  ╚═══╝ ╚═╝  ╚═╝    

    """)

    text = "    TURKISH CYBER EMPIRE - DEATH ARMIES BASE COMMANDER \n         ""            ⇛ 🌟🌟🌟⇚ \n      ""            ✺★★||★★||★★✺"
    color = 'green'

    for char in text:
        bold_char = colored(char, color, attrs=['bold'])
        print(bold_char, end='', flush=True)
        time.sleep(0.02)  # Her karakter arasında 0.02 saniye bekleyin

    print()  # Yazı bittiğinde yeni satıra geçmek için   				
    print("\n")
    print(Fore.BLUE +" [1]"+ Fore.RESET + Fore.WHITE +"  Dork tarama" + Fore.RESET + Fore.BLUE +"                 [11]"+ Fore.RESET + Fore.WHITE +" Ağ dinleme" )
    print(Fore.BLUE +" [2]"+ Fore.RESET + Fore.WHITE +"  SQL injection kontrol"+ Fore.RESET + Fore.BLUE +"       [12]"+ Fore.RESET + Fore.WHITE +" Brute force " )
    print(Fore.BLUE +" [3]"+ Fore.RESET + Fore.WHITE +"  Oto dump (sqlmap)" + Fore.RESET + Fore.BLUE +"           [13]"+ Fore.RESET + Fore.WHITE +" SMS Bomber" )
    print(Fore.BLUE +" [4]"+ Fore.RESET + Fore.WHITE +"  Oto shell (sqlmap)" + Fore.RESET + Fore.BLUE +"          [14]"+ Fore.RESET + Fore.WHITE +" XSS zaafiyet kontrol" )
    print(Fore.BLUE +" [5]"+ Fore.RESET + Fore.WHITE +"  DDOS Atağı" + Fore.RESET + Fore.BLUE +"                  [15]"+ Fore.RESET + Fore.WHITE +" keylogger" )
    print(Fore.BLUE +" [6]"+ Fore.RESET + Fore.WHITE +"  Exploit tarama" + Fore.RESET + Fore.BLUE +"              [16]"+ Fore.RESET + Fore.WHITE +" Rat oluşturma" )
    print(Fore.BLUE +" [7]"+ Fore.RESET + Fore.WHITE +"  Port tarama" + Fore.RESET + Fore.BLUE +"      		  [17]"+ Fore.RESET + Fore.WHITE +" Güvenlik duvarı tespiti" )
    print(Fore.BLUE +" [8]"+ Fore.RESET + Fore.WHITE +"  Subdomain Finder" + Fore.RESET + Fore.BLUE +"            [18]"+ Fore.RESET + Fore.WHITE +" Wordlist oluşturma" )
    print(Fore.BLUE +" [9]"+ Fore.RESET + Fore.WHITE +"  Rootkit tarama" + Fore.RESET + Fore.BLUE +"              [19]"+ Fore.RESET + Fore.WHITE +" Pasif bilgi toplama" )
    print(Fore.BLUE +"[10]"+ Fore.RESET + Fore.WHITE +"  Sunucu zaafiyet analizi" + Fore.RESET + Fore.BLUE +"     |[0]"+ Fore.RESET + Fore.WHITE+ Style.BRIGHT +" Çıkış")
    print("\n")
    secim=input(Fore.WHITE + Style.BRIGHT + "Lütfen yapmak istediğiniz işlemi seçiniz : ")

    if secim == '0':
        break
    if secim == "1":
        python_dosyasi = "dorktarama.py"
        komut = f"gnome-terminal --title INOVA  -- bash -c 'cd {dizin_yolu}/araclar && python3 {python_dosyasi}; bash'"
        os.system(komut)
    if secim == "2":
        python_dosyasi = "sqlkontrol.py"
        komut = f"gnome-terminal --title INOVA -- bash -c 'cd {dizin_yolu}/araclar && python3 {python_dosyasi}; bash'"
        os.system(komut)
    if secim == "3":
        python_dosyasi = "dumpkontrol.py"
        komut = f"gnome-terminal --title INOVA -- bash -c 'cd {dizin_yolu}/araclar/ && python3 {python_dosyasi}; bash'"
        os.system(komut)
    if secim == "4":
        python_dosyasi = "shellkontrol.py"
        komut = f"gnome-terminal --title INOVA -- bash -c 'cd {dizin_yolu}/araclar/ && python3 {python_dosyasi}; bash'"
        os.system(komut)
    if secim == "5":
        python_dosyasi = "inovadown.py"
        komut = f"gnome-terminal --title INOVA -- bash -c 'cd {dizin_yolu}/araclar/DDoS/ && python3 {python_dosyasi}; bash'"
        os.system(komut)
    if secim == "6":
        python_dosyasi = "exploit_tarama.py"
        komut = f"gnome-terminal --title INOVA  -- bash -c 'cd {dizin_yolu}/araclar && python3 {python_dosyasi}; bash'"
        os.system(komut)        
    if secim == "7":
        python_dosyasi = "port_tarama.py"
        komut = f"gnome-terminal --title INOVA -- bash -c 'cd {dizin_yolu}/araclar && python3 {python_dosyasi}; bash'"
        os.system(komut)      
    if secim == "8":
        python_dosyasi = "subdomain.sh"
        komut = f"gnome-terminal --title INOVA -- bash -c 'cd {dizin_yolu}/araclar && bash {python_dosyasi}; bash'"
        os.system(komut)
    if secim == "9":
        python_dosyasi = "rootkit_tarama.py"
        komut = f"gnome-terminal --title INOVA  -- bash -c 'cd {dizin_yolu}/araclar && python3 {python_dosyasi}; bash'"
        os.system(komut) 
    if secim == "10":
        python_dosyasi = "sunucuzafiyet_analizi.py"
        komut = f"gnome-terminal --title INOVA -- bash -c 'cd {dizin_yolu}/araclar && python3 {python_dosyasi}; bash'"
        os.system(komut)  
    if secim == "11":
        python_dosyasi = "agdinleme.py"
        komut = f"gnome-terminal --title INOVA  -- bash -c 'cd {dizin_yolu}/araclar && sudo python3 {python_dosyasi}; bash'"
        os.system(komut)  
    if secim == "12":
        python_dosyasi = "Brutfource.py"
        komut = f"gnome-terminal --title INOVA  -- bash -c 'cd {dizin_yolu}/araclar/Kabakuvvet/ && python3 {python_dosyasi}; bash'"
        os.system(komut)        
    if secim == "13":
        python_dosyasi = "bak.py"
        komut = f"gnome-terminal -- bash -c 'cd {dizin_yolu}/araclar/Sms_Bomber/ && python3 {python_dosyasi} && exit; bash'"
        os.system(komut)        
    if secim == "14":
        python_dosyasi = "xss.py"
        komut = f"gnome-terminal --title INOVA  -- bash -c 'cd {dizin_yolu}/araclar && python3 {python_dosyasi}; bash'"
        os.system(komut)
    if secim == "15":
        python_dosyasi = "keyloger.py"
        komut = f"gnome-terminal -- bash -c 'cd {dizin_yolu}/araclar/Keyloger/ && python3 {python_dosyasi}; bash'"
        os.system(komut)
    if secim == "16":
        python_dosyasi = "rat_oluşturma.py"
        komut = f"gnome-terminal --title INOVA -- bash -c 'cd {dizin_yolu}/araclar && python3 {python_dosyasi}; bash'"
        os.system(komut)
    if secim == "17":
        python_dosyasi = "güvenlik_duvarı_tesbiti.py"
        komut = f"gnome-terminal --title INOVA  -- bash -c 'cd {dizin_yolu}/araclar && python3 {python_dosyasi}; bash'"
        os.system(komut)
    if secim == "18":
        python_dosyasi = "wordlistoluşturma.py"
        komut = f"gnome-terminal --title INOVA  -- bash -c 'cd {dizin_yolu}/araclar && python3 {python_dosyasi}; bash'"
        os.system(komut)
    if secim == "19":
        python_dosyasi = "pasif_bilgi.py"
        komut = f"gnome-terminal --title INOVA  -- bash -c 'cd {dizin_yolu}/araclar && python3 {python_dosyasi}; bash'"
        os.system(komut)
os.system("exit")
sys.exit(0)
