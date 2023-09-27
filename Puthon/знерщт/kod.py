import requests
from bs4 import BeautifulSoup
url="https://ru.wikipedia.org/wiki/250_%D0%BB%D1%83%D1%87%D1%88%D0%B8%D1%85_%D1%84%D0%B8%D0%BB%D1%8C%D0%BC%D0%BE%D0%B2_%D0%BF%D0%BE_%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D0%B8_IMDb"
r = requests.get(url=url)
soup = BeautifulSoup(r.content, 'html.parser')
table = soup.find("table")
films = table.find_all("tr")[1:251]
num=0
for film in films:
    num+=1
    td = film.find_all("td")
    title = td[1].text.strip("\n")
    print(f"Топ {num} - {title}")