import os
import random
from termcolor import colored
from connection import check_connection
from attack import start_attack
from user_input import get_ip_address, get_protocol, get_thread_num
from pick import pick 
from time import sleep
def main():
  os.system("clear")
  print()
  print(colored("Inova Down başlıyor, lütfen bekleyin!", "red"))
  print(colored("Bunu yasal amaçlarla kullandığınızdan eminim - Echo", "red"))
  print()

  check_connection()
  os.system("clear")
  print(colored('''
	$$$$$$\ $$\   $$|$$$$$$ |$$|  $$|$$$$$$\  
	\_$$ _| $$$\  $$|$$ __$$|$$| |$$|$$ __$$|
	  $$ |  $$$$\ $$|$$ / $$|$$| |$$|$$ / $$|
	  $$ |  $$ $$\$$|$$ | $$|$$| |$$|$$$$$$$|
	  $$ |  $$ \$$$$|$$ | $$|\$$\$$/|$$ __$$|
	  $$ |  $$ |\$$$|$$ | $$| \$$$/ |$$  |$$|
	$$$$$$\ $$ | \$$|$$$$$$ |  \$/  |$$  |$$|
	\______|\__| \__|\______/   \/   \__| \_|
                                                  ''', 'red'))
  print(colored("         Piyasadaki en güçlü DDoS aracı INOVA DDOS","blue",attrs=["bold"],))
  print()
  menu_selections = [
    'Başlat',
    'Krediler',
    'Çıkış' ]
  sleep(2)
  menu_selection = pick(menu_selections, 'Bir seçenek seçin...(Enter)', '> ')[0]
  match menu_selection:
    case 'Başlat':
      ip = get_ip_address()
      protocol = get_protocol()
      threads = get_thread_num()
      print(colored("Launched with " + str(threads) + " threads.", "cyan"))
      print()
      start_attack(ip, protocol, threads)
    case 'Credits':
      print(colored('                        INOVADOWN', attrs=['bold']))
      print(colored('''
            Discort sunucumuz
            https://discord.gg/344RzMa4
            
            Developers;
             
	         By Arenk Tuğrul
            Discort    :@arenklord
	    Telegram   : @Arenk_SP
            ''', 'green'))
    case 'Exit':
      exit(0)
  

if __name__ == "__main__":
  main()
