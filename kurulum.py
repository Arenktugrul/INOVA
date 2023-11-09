import os
import webbrowser

os.system("clear")
print("\n")
print("INOVA AREN ALL aracı kurulumu başlatılıyor...")
print("\n")
print("Gnome terminal indiriliyor...")
os.system("sudo apt-get install gnome-terminal")
os.system("sudo apt install veil")
os.system("clear")


print("Gerekli kütüphaneler yükleniyor...")

os.system("pip install requests")
os.system("pip install colorama")
os.system("pip install beautifulsoup4")   
os.system("pip install fake-useragent")  
os.system("pip install termcolor")    
os.system("pip install pydub")   
os.system("pip install SpeechRecognition")
os.system("pip install scapy")   
os.system("pip install pynput")
os.system("pip install pick") 
os.system("pip install halo")   

os.system("clear")


sms = input("Sms bomber kurulumu yapılsın mı e/h: ")
if sms == "e":
    der = input("Açılacak web sayfasından Node.js'i bilgisayarınıza indirip yükleyin. (Anlaşıldımı?) e/h: ")
    if der == "e":
        print("Mainde Görüşürüz")
        url = "https://nodejs.org/en/download"
        webbrowser.open(url)
    else:
        print("Sms bomber, Node.js olmadan çalıştırılamaz.")
else:
    print("Sms bomber kurulumu yapılmayacak")

os.system("rm kurulum.py")
