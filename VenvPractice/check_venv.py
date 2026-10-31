import requests

print("Библиотека requests работает!")
response = requests.get("https://api.github.com")
print(f"Статус ответа от GitHub: {response.status_code}")