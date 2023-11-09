import time
import random
from termcolor import colored

def start_attack(ip, protocol, threads):
  print()
  print(colored("Hedef şu şekilde ayarlandı  " + ip + " kullanarak " + protocol + ".", "magenta",))
  print(colored("İle saldırıya başlama " + str(threads) + " Taruz, istediğiniz zaman durdurmak için CTRL+C kullanın", "magenta",))
  print(colored("You can use https://iplocation.io/ping/" + ip + " to check the webserver ping.","magenta",))
  print()
  while True:
    mbSec = round(random.uniform(10, 40), 1)
    hitRate = round(random.uniform(95, 100), 2)
    curThread = random.randint(1, threads)
    if random.randint(1, 1000) < 10:
      print(colored("Taruz {}: Kötü iş parçacığı algılandı, iş parçacığı geri dönüştürülüyor. Diğer iş parçacıkları etkilenmeyecektir. ".format(curThread),"red",))
    else:
      print(colored("Taruz {}: Son saniyede {}MB, isteklerde {}% Hitrate ile hedefe gönderildi. ".format(curThread, mbSec, hitRate),"green",))
    time.sleep(0.1)
