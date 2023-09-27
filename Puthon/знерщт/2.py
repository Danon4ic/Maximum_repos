import requests
import json
url="https://swapi.dev/api"
urls=requests.get(url=url).json()
people_url=urls.get("people")
planets_url=urls.get("planets")
species_url=urls.get("species")
response=requests.get(people_url+"1").json()
response1=requests.get(planets_url+"1").json()
response2=requests.get(species_url+"1").json()
people=[]
nam=""
maxheight=0
for i in range (1,10):
    response=requests.get(people_url+str(i)).json()
    if response.get("height")!=None and response.get("height")!="n/a":
        people.append(response)
for stas in people:
    if int(response.get("height"))>maxheight:
        maxheight=int(response.get("height"))
        nam=stas.get("name")
print(maxheight, nam)