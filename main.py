import os 
import requests
import time
import sys
import colorama 
from colorama import Fore

clear = lambda: os.system('cls') if os.name == 'nt' else os.system('clear');local = time.localtime();current = time.strftime("%H:%M:%S", local)

def write(text):
    for f in text: print('' + f, end="");sys.stdout.flush();time.sleep(0.005)

os.system("title Moon Proxy Scraper ^| Awaiting Proxy To Scrape");clear()

def socks5():
    os.system("title Scraping SOCKS5");r = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all");proxies = open("socks5.txt", "w");proxies.write(str(r.text));proxies.close();clear();print(banner);option()
 
def socks4():
    os.system("title Scraping SOCKS4");r = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all");proxies = open("socks4.txt", "w");proxies.write(str(r.text));proxies.close();clear();print(banner);option() 
 
def http():
    os.system("title Scraping HTTP");r = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all");proxies = open("http.txt", "w");proxies.write(str(r.text));proxies.close();clear();print(banner);option()
 
banner = f"""{Fore.MAGENTA}
                  ███╗   ███╗ ██████╗  ██████╗ ███╗   ██╗                  
                  ████╗ ████║██╔═══██╗██╔═══██╗████╗  ██║
                  ██╔████╔██║██║   ██║██║   ██║██╔██╗ ██║
                  ██║╚██╔╝██║██║   ██║██║   ██║██║╚██╗██║
                  ██║ ╚═╝ ██║╚██████╔╝╚██████╔╝██║ ╚████║
                  ╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝{Fore.RESET}
                             
{Fore.RESET}"""
clear();print(banner)

def option():
    write("What type of proxies would you like?\n");print("\nSOCKS5\nSOCKS4\nHTTP\n");choice = input(f"[{current}] > ")
    if choice == "SOCKS5":
        socks5()
    elif choice == "SOCKS4":
        socks4()
    elif choice == "HTTP":
        http()
    else:
        print(f"[{current}] Did you type the correct choice?");time.sleep(2);clear();print(banner);option()
        
option()
