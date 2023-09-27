import requests
import json
import datetime
# lat=55.45
# lon=37.36
# API_KEY="a7c92db35e7308e22edb493ffa32f1ed"
# url=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
# response=requests.get(url).json()
# timestamp= response.get("sys").get("sunrise")
# print(datetime.datetime.fromtimestamp(timestamp))
# print(response)

current_date = datetime.date.today()
print(current_date)
