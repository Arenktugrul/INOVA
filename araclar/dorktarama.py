#!/usr/bin/env python
import os
import requests
import time
import re
import colorama
from colorama import Fore, Back, Style
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from termcolor import colored
from urllib.parse import urlparse, urlsplit, urlunsplit
from pydub import AudioSegment
import speech_recognition as sr

search_engines = [
    "http://www.google.com/search?q={Key}&num=100&start=0",
    "https://www.bing.com/search?q={Key}&count=100&first=0",
    "https://search.yahoo.com/search?p={Key}&n=100&b=0",
]

def download_captcha(url):
    sonuc = "captcha.mp3"
    response = requests.get(url)
    with open(sonuc, "wb") as f:
        f.write(response.content)
    sound = AudioSegment.from_mp3(sonuc)
    sound.export("captcha.wav", format="wav")

def solve_captcha():
    r = sr.Recognizer()
    with sr.WavFile("captcha.wav") as source:
        audio = r.record(source)  
    text = r.recognize_google(audio, language='en-US')
    return text

def captcha_elements(soup, engine_url):
    iframe = soup.select_one("iframe[title='reCAPTCHA']")
    if not iframe:
        raise Exception("Captcha iframe bulunamadı.")

    wait_time = 3  # Bekleme süresini artırabilirsiniz.
    checkbox = soup.select_one(".recaptcha-checkbox-border")
    if not checkbox:
        raise Exception("Captcha onay kutusu bulunamadı.")
    checkbox.click()

    time.sleep(wait_time)

    iframe = soup.select_one("iframe[title='recaptcha challenge expires in two minutes']")
    if not iframe:
        raise Exception("Captcha ses düğmesi bulunamadı.")
    engine_domain = "{0.scheme}://{0.netloc}".format(urlsplit(engine_url))
    audio_button = soup.select_one(".rc-button.goog-inline-block.rc-button-audio")
    if audio_button:
        audio_url = engine_domain + audio_button['src']
        download_captcha(audio_url)
        result = solve_captcha()
        return result
    else:
        raise Exception("Captcha ses düğmesi bulunamadı.")

def get_random_user_agent():
    user_agent = UserAgent().random
    return user_agent

def print_symmetric_text(text):
    width = 80
    space = (width - len(text)) // 2
    print("=" * space + text + "=" * space)

def print_result_urls(urls):
    print("\nBulunan Siteler:")
    for idx, url in enumerate(urls, start=1):
        print(f"{idx}. {url}")
    print("=" * 80)

def perform_search(dorks, search_engine):
    url_list = []
    for dork in dorks:
        engine_url = search_engine.replace("{Key}", dork)
        headers = {'User-Agent': get_random_user_agent()}
        response = requests.get(engine_url, headers=headers)
        page_source = response.text
        soup = BeautifulSoup(page_source, "html.parser")

        if "captcha-form" in page_source:
            print_symmetric_text(Fore.BLUE + " Captcha çözülüyor..." + Fore.RESET)
            try:
                captcha_result = captcha_elements(soup, engine_url)
                captcha_input = soup.select_one("#g-recaptcha-response")
                captcha_input['value'] = captcha_result
            except Exception as e:
                print("CAPTCHA çözme hatası:", e)
        else:
            pattern = r'<a href="(.*?)"'
            matches = re.findall(pattern, page_source)

            for match in matches:
                if "google" not in match:
                    if "http" in match:
                        url = match.replace("&amp;", "&")
                        url_list.append(url)
    return url_list

def dork_tarama():
    os.system("clear")
    print("\n")
    print(colored("Dork tarama işlemi başlatılıyor...\n", 'blue', attrs=['bold']))

    mevcut_dizin = os.getcwd()
    ust_dizin = os.path.dirname(mevcut_dizin)
    hedef_dizin1 = "Hangar"
    hedef_dizin2 = "dorklar"
    os.chdir(os.path.join(ust_dizin, hedef_dizin1))
    os.chdir(hedef_dizin2)
    hedef_dosya = "dorklar.txt"
    
    with open(hedef_dosya, 'r') as dosya:
        dorks = dosya.read().splitlines()
        result_urls = []
        for search_engine in search_engines:
            result_urls.extend(perform_search(dorks, search_engine))

    unique_urls = []
    unique_domains = set()

    for url in result_urls:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        if "http://" + domain not in unique_domains and "https://" + domain not in unique_domains:
            if "https://" in url:
                unique_domains.add("https://" + domain)
            else:
                unique_domains.add("http://" + domain)
            unique_urls.append(url)

    mevcut_dizin = os.getcwd()
    ust_dizin = os.path.dirname(mevcut_dizin)
    hedef1_dizin2 = "dorksonuç"
    os.chdir(os.path.join(ust_dizin, hedef1_dizin2))
    yazma_dosya = "dorksonuç.txt"
    
    with open(yazma_dosya, 'w') as file:
        file.writelines("%s\n" % url for url in unique_urls)
    print_result_urls(unique_urls)
    print_symmetric_text(Fore.GREEN + " Sonuçlar Hangar/dorksonuç/dorksonuç.txt dosyasına kaydedildi!" + Fore.RESET)

def dork_tarama_sonuclar(unique_urls):
    mevcut_dizin = os.getcwd()
    ust_dizin = os.path.dirname(mevcut_dizin)
    #hedef1_dizin1 = "Hangar"
    hedef1_dizin2 = "dorksonuç"
    os.chdir(os.path.join(ust_dizin, hedef1_dizin2))
    #os.chdir(hedef1_dizin2)
    yazma_dosya = "dorksonuç.txt"
    
    with open(yazma_dosya, 'w') as file:
        file.writelines("%s\n" % url for url in unique_urls)
    print_result_urls(unique_urls)
    print_symmetric_text(Fore.GREEN + " Sonuçlar Hangar/dorksonuç/dorksonuç.txt dosyasına kaydedildi!" + Fore.RESET)

if __name__ == "__main__":
    try:
        dork_tarama()
    except KeyboardInterrupt:
        print("Kullanıcı tarafından işlem kesildi.")
