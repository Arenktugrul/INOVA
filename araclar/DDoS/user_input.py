import re
from termcolor import colored
from pick import pick # https://github.com/wong2/pick

def get_ip_address():
  print("Hedef IP Adresi Giriniz:")
  ip = input(colored("> ", "yellow"))

  if not re.match(r"^(\d{1,3}\.){3}\d{1,3}$", ip):
    print(colored("Hata : Python userInput'ta geçersiz IP adresi biçimi, söz reddedildi.", "red"))
    print(colored("Hata nedeniyle çıkılıyor, bu sizin hatanızdı. :(", "red"))
    exit("Geçersiz Kulanım")
    
  return ip

def get_protocol():
  print("Bir protokol seçin (TCP, UDP veya HTTP) :")
  protocol = input(colored("> ", "yellow"))
    
  if protocol not in ['TCP', 'UDP','HTTP']:
    print(colored("Hata : python userInput'ta geçersiz protokol, söz reddedildi.", "red"))
    print(colored("Hata nedeniyle çıkılıyor, bu sizin hatanızdı. :(", "red"))
    exit("Geçersiz Kulanım")
    
  return protocol
  
def get_thread_num():
  print("İş parçacığı sayısını girin (varsayılan 16) : ")

  threads = input(colored("> ", "yellow"))
  if threads == None:
    threads = 16
  else:
    try:
      threads = int(threads)
    except:
      print(colored("Hata : Python userInput'ta tamsayı olmayan değer, iş parçacığı başlatılamadı.", "red"))
      print(colored("Hata nedeniyle çıkılıyor, bu sizin hatanızdı :(", "red"))
      exit("Geçersiz Kulanım")
  return threads
