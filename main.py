import requests
import os 
import colorama
import time 
from colorama import Fore

clear = lambda: os.system('cls') if os.name == 'nt' else os.system('clear')

def socks5():
    os.system('title Scraping SOCKS5 Proxies!')
    r = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all")
    proxies = open("socks5.txt", "w")
    proxies.write(str(r.text)) 
    proxies.close()
    clear()
    print(banner)
    option()


def http(): 
    os.system('title Scraping HTTP Proxies!')
    r = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all")
    proxies = open("http.txt", "w")
    proxies.write(str(r.text)) 
    proxies.close()
    clear() 
    print(banner)
    option()

def socks4():
    os.system('title Scraping SOCKS4 Proxies!')
    r = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all")
    proxies = open("socks4.txt", "w")
    proxies.write(str(r.text)) 
    proxies.close()
    clear()
    print(banner)
    option()

banner = f"""{Fore.MAGENTA}


                  ███╗   ███╗ ██████╗  ██████╗ ███╗   ██╗                  
                  ████╗ ████║██╔═══██╗██╔═══██╗████╗  ██║
                  ██╔████╔██║██║   ██║██║   ██║██╔██╗ ██║
                  ██║╚██╔╝██║██║   ██║██║   ██║██║╚██╗██║
                  ██║ ╚═╝ ██║╚██████╔╝╚██████╔╝██║ ╚████║
                  ╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝{Fore.RESET}
                    
                       [{Fore.MAGENTA}1{Fore.RESET}] HTTP       
                       [{Fore.MAGENTA}2{Fore.RESET}] SOCKS5             
                       [{Fore.MAGENTA}3{Fore.RESET}] SOCKS4             

{Fore.RESET}"""
clear()
print(banner)


def option():
    os.system(f'title Moon Proxy Scraper ^| https://github.com/6pj')
    print(f"[{Fore.MAGENTA}?{Fore.RESET}] What type of proxies do you want to scrape?")
    choice = input(f"{Fore.MAGENTA}> ")
    if choice == "1":
        http()
    elif choice == "2":
        socks5()
    elif choice == "3":
        socks4()
    else:
        print(f"{Fore.RESET}[{Fore.RED}!{Fore.RESET}] Did you type the correct choice?")
        time.sleep(3)
        clear()
        print(banner)
        option()

option()
