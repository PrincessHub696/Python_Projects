import requests
import json

# Заходим на сайт
ur1 = "https://www.cbr-xml-daily.ru/daily_json.js"
response = requests.get(ur1)

data = json.loads(response.text)

usd = data["Valute"]["USD"]["Value"]
print(f"Курс доллара: {usd}")