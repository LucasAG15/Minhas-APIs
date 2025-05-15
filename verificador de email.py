import requests

email = "teste@exemplo.com"
res = requests.get(
    f"https://emailvalidation.abstractapi.com/v1/?api_key=SUA_CHAVE&email={email}")
print(res.json())
