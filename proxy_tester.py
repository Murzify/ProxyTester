import os, time, json

try:
    import requests
    from colorama import init, Back, Fore
    from bs4 import BeautifulSoup as bs
except:
    print("Установка модклей...")
    os.system("pip install -r requirements.txt")
    print("Запустите файл снова!")
    exit()

init()
banner = Fore.BLUE +\
"""
 ███████████                                            ███████████                   █████                      
░░███░░░░░███                                          ░█░░░███░░░█                  ░░███                       
 ░███    ░███ ████████   ██████  █████ █████ █████ ████░   ░███  ░   ██████   █████  ███████    ██████  ████████ 
 ░██████████ ░░███░░███ ███░░███░░███ ░░███ ░░███ ░███     ░███     ███░░███ ███░░  ░░░███░    ███░░███░░███░░███
 ░███░░░░░░   ░███ ░░░ ░███ ░███ ░░░█████░   ░███ ░███     ░███    ░███████ ░░█████   ░███    ░███████  ░███ ░░░ 
 ░███         ░███     ░███ ░███  ███░░░███  ░███ ░███     ░███    ░███░░░   ░░░░███  ░███ ███░███░░░   ░███     
 █████        █████    ░░██████  █████ █████ ░░███████     █████   ░░██████  ██████   ░░█████ ░░██████  █████    
░░░░░        ░░░░░      ░░░░░░  ░░░░░ ░░░░░   ░░░░░███    ░░░░░     ░░░░░░  ░░░░░░     ░░░░░   ░░░░░░  ░░░░░     
                                              ███ ░███                                                           
                                             ░░██████                                                            
                                              ░░░░░░                                                             
"""

print(banner)

with open("proxies.json") as p:
    proxies = json.load(p)["proxies"]
p.close()
for proxy in proxies:
    protocol = proxy.split("://")[0]
    ip = proxy.split("://")[1].split(":")[0]
    p = {
        protocol: proxy
    }

    try:
        t1 = time.time()
        r = requests.get("https://2ip.ru/", proxies=p)
        t2 = time.time()
        speed = t2 - t1
    except requests.exceptions.ProxyError as err:
        print(Fore.WHITE, Back.RED, f"{proxy} : не удалось подключится")
        print(Fore.WHITE, Back.RED, str(err).split("[WinError 10060] ")[1].replace("')))", ""), "\n")
        # print("Error:\n", err)
        continue

    html = r.text
    soup = bs(html, "html.parser")
    find = soup.find_all("div", class_="ip")
    if ip in find[0].text:
        print(Fore.WHITE, Back.GREEN, f"{proxy} : работет!\nSpeed: {round(speed, 3)}s\n")
    else:
        print(Fore.WHITE, Back.RED, f"{proxy} : ip не изменился\n")

input("Press Enter to exit...")