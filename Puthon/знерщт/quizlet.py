import requests
from googletrans import Translator
translator=Translator
url="https://opentdb.com/api.php?amount=10&category=24&type=boolean"
response=requests.get(url=url)
data_quiz=response.json()
for i in range(10):
    data_quiz["results"][i]["question"]=translator.translate(data_quiz["results"][i]["question"],dest="ru").text
    answ=input("True/False")
    if answ==data_quiz["results"][i]["correct_answer"].text:
        print("Верно")
    else:
        print("Неверно")