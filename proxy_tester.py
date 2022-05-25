import os, time, json, requests

try:
	import requests
except:
	print("Установка модклей...")
	os.system("pip install -r requirements.txt")
	print("Запустите файл снова!")
	exit()

with open("proxies.json") as p:
	proxies = json.load(p)["proxies"]
p.close()

for proxy in proxies:
	r = requests.get(f"http://ip-api.com/json/")
	real_ip = json.loads(r.text)["query"]
	protocol = proxy.split("://")[0]

	p = {
		protocol: proxy
	}

	try:
		t1 = time.time()
		r = requests.get(f"http://ip-api.com/json/", proxies=p)
		data = json.loads(r.text)
		t2 = time.time()
		speed = t2 - t1
	except requests.exceptions.ProxyError as err:
		print(f"{proxy} : не удалось подключится")
		continue
	except requests.exceptions.ConnectTimeout as err:
		print(f"{proxy} : не удалось подключится")
		continue

	if real_ip != data["query"]:
		print(f"{proxy} : работет!\nSpeed: {round(speed, 3)}s\n")
	else:
		print(f"{proxy} : ip не изменился\n")

input("Press Enter to exit...")
