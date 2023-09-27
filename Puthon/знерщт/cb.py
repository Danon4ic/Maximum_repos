import requests
from bs4 import BeautifulSoup
from datetime import datetime
url="http://www.cbr.ru/scripts/XML_daily.asp?"
date=datetime.today()
date_str=date.strftime("%d/%m/%Y")
params={"date_req":date_str}
response=requests.get(url=url,params=params)
html=BeautifulSoup(response.content,"html.parser")
def getCourse(id):
    return html.find("valute", attrs={"id":id}).value.text.replace(",",".")
print(float(getCourse("R01235")))
f=open("course.txt","w")
f.write("$:"+getCourse("R01235")+ "\n" )
f.write("euro:"+getCourse("R01239")+ "\n" )
f.close()