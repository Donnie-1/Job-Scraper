import requests

proxy = '185.199.231.45:8382'

r = requests.get('https://httpbin.org/ip', proxies={'http': proxy, 'https': proxy }, timeout=3)

print(r.status_code); 
