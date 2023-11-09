#!/bin/bash

MOR='\033[1;35m'
KIRMIZI='\033[1;31m'
YESIL='\033[1;32m'
SARI='\033[1;33m'
MAVI='\033[1;34m'
PEMBE='\033[1;35m'
ACIK_MAVI='\033[1;36m'
BEYAZ='\033[1;37m'

clear  # Terminali temizle

printf """${MAVI}\n

██╗███╗   ██╗ ██████╗ ██╗  ██╗ █████╗ ███████╗██╗ ██╗██████╗
██║████╗  ██║██╔═══██╗██║  ██║██╔══██╗██╔════╝██║ ██║██╔══██╗
██║██╔██╗ ██║██║   ██║██║  ██║███████║███████╗██║ ██║██████╔╝
██║██║╚██╗██║██║   ██║██║  ██║██╔══██║╚════██║██║ ██║██╔══██╗
██║██║ ╚████║╚██████╔╝ █████╔╝██║  ██║███████║██████║██████╔╝
╚═╝╚═╝  ╚═══╝ ╚═════╝   ╚═══╝ ╚═╝  ╚═╝╚══════╝ ╚════╝╚═════╝
"""

printf "\n${SARI}[*] Gereksinimler Hazırlanıyor... Lütfen bekleyin!\n"
apt install toilet &> /dev/null

printf "${SARI}                            - ARENK TUĞRUL TARAFINDAN"

printf "\n\n${BEYAZ}[!] Alt Alanları Sıralamak İçin Alan Adını Girin: "
read -r url

printf "${MAVI}\n[*] Alt Alan Sıralama İşlemi Başladı!\n"

printf "${YESIL}\n[+] Subfinder İle Alt Alanlar Sıralanıyor..."
subfinder -d $url -silent > sub1
printf "${YESIL}\n[+] Assetfinder İle Alt Alanlar Sıralanıyor..."
assetfinder $url > sub2

printf "${YESIL}\n[+] crt.sh Üzerinden Alt Alanlar Sıralanıyor..."
curl -s "https://crt.sh/?q=$url" | grep "<TD>" | grep $url | cut -d ">" -f2 | cut -d "<" -f1 | sort -u | sed '/^*/d' > sub3
printf "${YESIL}\n[+] Rapiddns Üzerinden Alt Alanlar Sıralanıyor..."
curl -s "https://rapiddns.io/subdomain/$url#result" | grep "<td><a" | cut -d '"' -f 2 | grep http | cut -d '/' -f3 | sort -u > sub4
printf "${YESIL}\n[+] Bufferover Üzerinden Alt Alanlar Sıralanıyor..."
curl -s "https://dns.bufferover.run/dns?q=.$url" | jq -r .FDNS_A[] | cut -d '\' -f2 | cut -d "," -f2 |  sort -u > sub5
printf "${YESIL}\n[+] Ridder Üzerinden Alt Alanlar Sıralanıyor..."
curl -s "https://riddler.io/search/exportcsv?q=pld:$url" | grep -Po "(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | sort -u > sub6
printf "${YESIL}\n[+] Jldc Üzerinden Alt Alanlar Sıralanıyor..."
curl -s "https://jldc.me/anubis/subdomains/$url" | grep -Po "((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | cut -d "/" -f3 > sub7
printf "${YESIL}\n[+] Omnisint Üzerinden Alt Alanlar Sıralanıyor..."
curl -s "https://sonar.omnisint.io/subdomains/$url" | cut -d "[" -f1 | cut -d "]" -f1 | cut -d "\"" -f 2 > sub8

sort sub1 sub2 sub3 sub4 sub5 sub6 sub7 sub8 | uniq | tee ../$url-tum_alt_domainler
rm sub*

printf "${MAVI}\n[*] Alt Alan Sıralama İşlemi Tamamlandı!\n"
num=$(wc -l ../$url-tum_alt_domainler | awk '{print $1; exit}')
printf "${BEYAZ}\n[*] $url için $num alt alan bulundu\n"

printf "${MAVI}\n[!] Sonuçları görmek için $url-tum_alt_domainler dosyasını inceleyin!\n\n"
