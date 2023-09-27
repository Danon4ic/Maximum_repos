import requests
import json
url =('https://www.cbr-xml-daily.ru/daily_json.js')
urls=requests.get(url).json()
USD=urls['Valute']['USD']["Value"]
EUR=urls['Valute']['EUR']["Value"]
AUD=urls['Valute']['AUD']["Value"]
print(f"курс доллара США: {USD} рублей")
print(f"курс евро: {EUR} рублей")
print(f"курс австралийского доллара: {AUD} рублей")
#Ссылка кривая, ее надо чутка поменять; MOL нет на сайте, взял евро;Чутка переделал код,чтобы выводил в строку