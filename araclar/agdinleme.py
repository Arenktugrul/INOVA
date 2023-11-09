from scapy.all import *
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
def packet_callback(packet):
    if packet.haslayer(IP) and packet.haslayer(Ether):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        mac_src = packet[Ether].src
        mac_dst = packet[Ether].dst

    if packet.haslayer(TCP):
        tcp_sport = packet[TCP].sport
        tcp_dport = packet[TCP].dport
        print(Fore.BLUE + Style.BRIGHT +  f"Kaynak IP	: " + Fore.RESET + Fore.RED + f"{ip_src}		" + Fore.RESET + Fore.BLUE + f"  	 Hedef IP	: " + Fore.RESET + Fore.RED + f"{ip_dst}"+ Fore.RESET)
        print(Fore.BLUE + Style.BRIGHT +  f"Kaynak MAC	: " + Fore.RESET + Fore.RED + f"{mac_src}	" + Fore.RESET + Fore.BLUE + f" 	 Hedef MAC	: " + Fore.RESET + Fore.RED + f"{mac_dst}"+ Fore.RESET)
        print(Fore.BLUE + Style.BRIGHT +  f"Kaynak TCP Port : " + Fore.RESET + Fore.RED + f"{tcp_sport}	" + Fore.RESET + Fore.BLUE + f" 			 Hedef TCP Port : " + Fore.RESET + Fore.RED + f"{tcp_dport}"+Fore.RESET+"\n")
sniff(prn=packet_callback, store=0)

