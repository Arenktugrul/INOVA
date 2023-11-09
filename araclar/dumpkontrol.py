import os
from otosql import dump_all
from termcolor import colored
from colorama import Fore, Back, Style

os.system("clear")
print("\n")
print(Fore.BLUE + Style.BRIGHT +" Oto Dump işlemi balşatılıyor...(Sqlmapp)"+ Fore.RESET )
print("\n")
dump_all()
