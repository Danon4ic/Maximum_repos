from pygame import mixer
from gtts import gTTS
# mixer.init()
# # mixer.music.load("krik-podsadnoj-utki-u.mp3")
# # mixer.music.play()
# # while mixer.music.get_busy():
# #     pass
# tts=gTTS(text="Пум пурум", lang="ru")
# tts.save("abc.mp3")
# mixer.init()
# mixer.music.load("abc.mp3")
# mixer.music.play()
# while mixer.music.get_busy():
#     pass
# import os
# mixer.quit()
# os.remove("abc.mp3")
import speech_recognition as sr
import pyaudio
p=pyaudio.PyAudio()
device_index=None
for i in range(p.get_device_count()):
    device_info=p.get_device_info_by_index(i)
    if device_info.get("defaultSampleRate")==44100.0:
        device_index=0
        break
def recognize_speech():
    rec=sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Скажите что-нибудь")
            audio=rec.listen(source, phrase_time_limit=5)
        try:
            text= rec.recognize_google(audio,language="ru_RU").lower()
            
            return print(text)
        except sr.UnknownValueError: 
            print("Повторите запрос")    
        except sr.RequestError as e:
            print("Ошибка сервера")
recognize_speech()