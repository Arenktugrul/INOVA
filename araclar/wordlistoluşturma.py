import itertools
import os
import random
import string
from termcolor import colored

def generate_wordlist(min_length, max_length, characters, output_folder):
    while True:
        # Rastgele bir dosya adı oluştur
        file_name = ''.join(random.choices(string.ascii_lowercase, k=10)) + ".txt"
        output_file = os.path.join(output_folder, file_name)

        with open(output_file, 'w') as file:
            for length in range(min_length, max_length + 1):
                for combo in itertools.product(characters, repeat=length):
                    word = ''.join(combo)
                    file.write(word + '\n')

        print(f"Wordlist başarıyla oluşturuldu ve Hangar/wordlistdepo dosyasına kaydedildi.")

        istek = input("Başka bir wordlist oluşturmak ister misiniz? (Evet için 'e', Hayır için 'h'): ")
        if istek.lower() != 'e':
            break

if __name__ == "__main__":
    print(colored(" INOVA wordlist oluşturma aracına hoş geldiniz", 'red', attrs=['bold']))

    print("1) Aracı taraması başlat")
    print("2) Çıkış")
    choice = input("Seçiminizi yapın: ")

    if choice == '1':
        min_length = int(input("Minimum karakter uzunluğunu girin: "))
        max_length = int(input("Maksimum karakter uzunluğunu girin: "))
        characters = input("Karakter kümesini girin: ")
        mevcut_dizin = os.getcwd()
        ust_dizin = os.path.dirname(mevcut_dizin)
        hedef_dizin1 = "Hangar"
        os.chdir(os.path.join(ust_dizin, hedef_dizin1))
        output_folder = "wordlistdepo"

        generate_wordlist(min_length, max_length, characters, output_folder)
    elif choice == '2':
        print("Programdan çıkılıyor.")
    else:
        print("Geçersiz seçim. Lütfen 1 veya 2 seçin.")
