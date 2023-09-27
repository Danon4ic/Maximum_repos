import telebot
token="Token"
bot=telebot.TeleBot("6613866848:AAEN6EmLng6g65GgCfBQjFziQO2hxsmyZGU")
@bot.message_handler(commands=["start"])
def s_m(message):
    print(message)
    bot.send_message(message.chat.id,"Привет, напиши слово 'привет'")
@bot.message_handler(content_types=['text'])
# def get_name(message):
#     if message.text=="привет":
#         bot.send_message(message.from_user.id,"Напиши имя")
#         bot.register_next_step_handler(message,get_surname)
#     elif message.text == "/help":
#         bot.send_message(message.from_user.id, "Напиши привет")
#         bot.register_next_step_handler(message,get_surname)
#     else:
#         bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
# def get_surname(message):
#     global name
#     name=message.text
#     bot.send_message(message.from_user.id,"А фамилия?")
#     bot.register_next_step_handler(message,get_res)
# def get_res(message):
#     global surname
#     surname=message.text
#     bot.send_message(message.from_user.id,"Тебя зовут "+ name + " "+ surname + " " +",Приятно познакомиться")

@bot.message_handler(commands=["course"])
def send_course(message):
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
    bot.send_message(message.from_user.id,"USD"+getCourse("R01235") + "; euro"+getCourse("R01239"))


bot.polling(none_stop=True, interval=0)