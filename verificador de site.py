import requests

url = "https://www.virustotal.com/api/v3/urls"
headers = {
    "x-apikey": "SUA_CHAVE_AQUI"
}
data = {"url": "http://site-suspeito.com"}

res = requests.post(url, headers=headers, data=data)
print(res.json())
