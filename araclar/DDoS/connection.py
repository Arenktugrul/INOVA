import time
import random
from termcolor import colored
from halo import Halo

waitTime = 0.5

def check_connection():
  with Halo(text=colored("Bağlantı Kontrol Ediliyor", "yellow"), spinner="dots") as h1:
    time.sleep(waitTime)
    h1.succeed(colored(" Bağlantı Kontrol Edildi", "green"))

  with Halo(text=colored("Paketler İçe Aktarılıyor", "yellow"), spinner="dots") as h2:
    time.sleep(waitTime)
    h2.succeed(colored(" Paketler İçe Aktarıldı", "green"))

  with Halo(text=colored("Betikler İndiriliyor", "yellow"), spinner="dots") as h3:
    time.sleep(waitTime)
    h3.succeed(colored(" Betikler İndirildi", "green"))

  with Halo(text=colored("Dosyalar Alınıyor", "yellow"), spinner="dots") as h4:
    time.sleep(waitTime)
    h4.succeed(colored(" Dosyalar Alındı", "green"))

  with Halo(text=colored("Derleniyor", "yellow"), spinner="dots") as h5:
    time.sleep(waitTime)
    h5.succeed(colored(" Derleme Tamamlandı", "green"))

  with Halo(text=colored("Donanım Tespit Ediliyor", "yellow"), spinner="dots") as h6:
    time.sleep(waitTime)
    h6.succeed(colored(" Donanım Tespit Edildi", "green"))

  with Halo(text=colored("Proxy Başlatılıyor", "yellow"), spinner="dots") as h7:
    time.sleep(waitTime)
    h7.succeed(colored(" Proxy Başlatıldı", "green"))

  with Halo(text=colored("Barındırılan İş Parçaları Başlatılıyor", "yellow"), spinner="dots") as h8:
    time.sleep(waitTime)
    h8.succeed(colored(" Barındırılan İş Parçaları Başlatıldı", "green"))

  with Halo(text=colored("Sistemden RAM İsteme", "yellow"), spinner="dots") as h9:
    time.sleep(waitTime)
    h9.succeed(colored(" Sistemden RAM Alındı", "green"))

  with Halo(text=colored("Başlatılıyor", "yellow"), spinner="dots") as h10:
    time.sleep(waitTime)
    h10.succeed(colored(" Başlatıldı", "green"))
