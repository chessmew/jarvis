import sys
import numpy as np
import pyautogui
from os import startfile
from PIL import Image
import wolframalpha
from pyautogui import click
from tkinter import Label
import pyttsx3
from tkinter import Entry
from tkinter import Button
from tkinter import Tk
from tkinter import StringVar
from pytube import YouTube
from keyboard import press
from keyboard import write
from time import sleep
from googletrans import Translator
import keyboard
import pyjokes
from PyDictionary import PyDictionary as dictionary
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia
from bs4 import BeautifulSoup
import os
import requests
import datetime
from playsound import playsound

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
#print(voices[1].id)
Assistant.setProperty('voice', voices[0].id)

Api_Key = "2152AISO0I3ykqsTeXc0v35ceY7AG7fRmuo93VZd"

def Speak(audio):
    print("  ")
    Assistant.say(audio)
    print(f": {audio}")
    print("  ")
    print("  ")
    Assistant.runAndWait()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        command.pause_threshold = 1
        audio = command.listen(source)
        try:
            print("Recognizing....")
            query = command.recognize_google(audio,language='en-in')
            print(f"You Said : {query}")
        except Exception as Error:
            return "none"
        return query.lower()

def NasaNews(Date):

    Speak("Extracting  Data from Nasa")

    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_Key)

    Params = {'date': str(Date)}

    r = requests.get(Url, params=Params)

    Data = r.json()

    Info = Data['explanation']

    Title = Data['title']

    Image_Url = Data['url']

    Image_r = requests.get(Image_Url)

    Filename = str(Date) + '.jpg'

    with open(Filename,'wb') as f:

        f.write(Image_r.content)

    Path_1 = "C:\\Users\\KUNAL\\Desktop\\kkk\\python\\Sample Generetor\\Jarvis Full Programs\\" + str(Filename)

    Path_2 = "C:\\Users\\KUNAL\\Desktop\\kkk\\Space Photos\\" + str(Filename)

    os.rename(Path_1, Path_2)

    img = Image.open(Path_2)

    img.show()




    Speak(f"Title : {Title}")
    Speak(f"According to Nasa : {Info}")



def WishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        Speak("Good Morning Sir!")
    elif hour >= 12 and hour <= 12:
        Speak("Good Afternoon Sir!")
    else:
        Speak("Good Evening Sir!")

    Speak(" I am Jarvis . please tell me how can I help you")




if __name__ == "__main__":
    WishMe()


def TaskExe():
 Speak("")

def Music():
        Speak("Tell me The name of the song")
        musicName = takecommand()
        if 'Alert Kudey' in query:
                os.startfile('D:\Songs\PANJABI SONG\PUNJABI SONGS//Alert Kudey')
        else:
            pywhatkit.playonyt(musicName)
        Speak("Your song has been started , Enjoy that")

def TakeHindi():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        command.pause_threshold = 1
        audio = command.listen(source)
        try:
            print("Recognizing....")
            query = command.recognize_google(audio,language='hi')
            print(f"You Said : {query}")
        except Exception as Error:
            return "none"
        return query.lower()

def Tran():
    Speak("Tell me the line !")
    line = TakeHindi()
    convert = Translator()
    result = convert.convert(line)
    Text = result.text
    Speak("The Translation for This Line is:"+Text)

def OpenApps():
    Speak("Ok Sir , Wait a second!")

    if 'open pycharm community' in query:
        os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.2\\bin\\pycharm64.exe")

    elif 'open edius 8' in query:
        os.startfile("C:\\Program Files\\Grass Valley\\EDIUS 8\\EDIUS.exe" )

    else:
        Speak("No program found")

def CloseApps():
    Speak("ok Sir Wait a second!")

    if 'close pycharm community' in query:
        os.system("TASKILL /F /in pycharm64.exe")

    elif 'close edius eight' in query:
        os.system("TASKILL /F /in EDIUS.exe")

def Solver(query):

    api_key = "Q9UQ6H-KLV2KE58XQ"

    requester = wolframalpha.Client(api_key)

    requested = requester.query(query)

    Answer = next(requested.results).text

    try:

        Answer = next(requested.results).text

        return Answer

    except:

        Speak("You are telling me a wrong question.")

def YoutubeAuto():
    Speak("Whats your command")
    key = takecommand()

    if 'pause the video ' in key:
        keyboard.press('k')

    elif 'unpause the video' in key:
        keyboard.press('k')

    elif 'restart the video' in key:
        keyboard.press('0')

    elif 'mute the video' in key:
        keyboard.press('m')

    elif 'unmute the video' in key:
        keyboard.press('m')

    elif 'skip the video' in key:
        keyboard.press('l')

    elif 'back the video' in key:
        keyboard.press('j')

    elif 'full screen' in key:
        keyboard.press('f')

    elif 'half screen' in key:
        keyboard.press('f')

    Speak("Done Sir")

def Dict():
    Speak("Activated Dictionary")
    Speak("Tell me the problem")
    problem = takecommand()

    if 'meaning' in problem:
        problem = problem.replace("what is the","")
        problem = problem.replace("jarvis","")
        problem = problem.replace("meaning of","")
        result = dictionary.meaning(problem)
        Speak(f"The meaning of {problem} is {result}")

    elif 'synonym' in problem:
        problem = problem.replace("what is the","")
        problem = problem.replace("jarvis","")
        problem = problem.replace("synonym of","")
        result = dictionary.synonym(problem)
        Speak(f"The Synonym of {problem} is {result}")

    elif 'antonym' in problem:
        problem = problem.replace("what is the", "")
        problem = problem.replace("jarvis", "")
        problem = problem.replace("antonym of", "")
        result = dictionary.antonym(problem)
        Speak(f"The Antonym of {problem} is {result}")

    Speak("Exited Dictionary!")

def ScreenShot():
    Speak("Ok Sir , what should I name the file")
    path = takecommand()
    path1name = path + ".png"
    path1 = "C:\\Jarvis\\Screenshots\\"+ path1name
    ss = pyautogui.Screenshot()
    ss.save(path1)
    os.startfile("\\Jarvis\\Screenshots\\")
    Speak("Here is you Screenshot")

def WhatsappMsg(name, message):
    startfile("C:\\Users\\KUNAL\\AppData\\Local\\WhatsApp\\WhatsApp.exe")

    sleep(15)

    click(x=99, y=96)

    sleep(1)

    write(name)

    sleep(1)

    click(x=188, y=249)

    sleep(1)

    click(x=571, y=690)

    sleep(1)

    write(message)

    press('enter')

def Whatsapp():
    Speak("Tell me the name of the person!")
    name = takecommand()

    if 'mummy' in name:
        Speak("Tell me the Message!")
        msg = takecommand()
        Speak("Tell me the time Sir!")
        Speak("Time in  Hour")
        hour = int(takecommand())
        Speak("Time in Minutes")
        min = int(takecommand())
        pywhatkit.sendwhatmsg("+919113712810", msg, hour, min, 20)
        Speak("Ok sir sending Whatsapp message!")
        sleep(5)
        press('enter')

    elif 'samosa' in name:
        Speak("Tell me the Message")
        msg = takecommand()
        Speak("Tell me the time Sir!")
        Speak("Time in  Hour")
        hour = int(takecommand())
        Speak("Time in Minutes")
        min = int(takecommand())
        pywhatkit.sendwhatmsg("+917070138355", msg, hour, min, 20)
        Speak("Ok sir sending Whatsapp message!")
        sleep(5)
        press('enter')

    elif 'Niraj' in name:
        Speak("Tell me the Message")
        msg = takecommand()
        Speak("Tell me the time Sir!")
        Speak("Time in  Hour")
        hour = int(takecommand())
        Speak("Time in Minutes")
        min = int(takecommand())
        pywhatkit.sendwhatmsg("+916204596093", msg, hour, min, 20)
        Speak("Ok sir sending Whatsapp message!")
        sleep(5)
        press('enter')

    else:

        Speak("Tell me the Phonenumber!")
        phone = int(takecommand())
        ph = '+91' + phone
        msg = takecommand()
        Speak("Tell me the time sir")
        Speak("Time in Hour!")
        hour = int(takecommand())
        Speak("Time in Minutes!")
        min = int(takecommand())
        pywhatkit.sendwhatmsg(phone, msg, hour, min, 20)
        Speak("ok Sir, Sending Whatsapp Message")
        sleep(5)
        press('enter')

def Temp():
        search = "temperature in jamshedpur"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_ = "BNeawe").text
        Speak(f"The temperature is {temperature} celcius ")

while True:
     query = takecommand()

     if 'hello' in query:
         Speak("  Hello sir I am Jarvis.")
         Speak("  Your personal AI Assistant.")
         Speak("  how May I help you")

     elif 'wikipedia' in query:
         Speak("Searching Wikipedia.....")
         query= query.replace("jarvis","")
         query = query.replace("wikipedia","")
         wiki = wikipedia.summary(query,sentences = 2)
         Speak(f"According To Wikipedia : {wiki}")

     elif 'kunal is mad' in query:
         Speak("  You shut up")
         Speak("  You are mad not my sir")
         Speak("  My sir is so intelligent")

     elif 'rekha is mad' in query:
         Speak("  Yes sir you are right ")
         Speak("  she is a mad")

     elif 'taniya is mad' in query:
         Speak("  Yes sir you are right ")
         Speak("  she is a mad")

     elif 'neha is mad' in query:
         Speak("  Yes sir you are right ")
         Speak("  she is a mad")

     elif 'gopal is mad' in query:
         Speak("  Yes sir you are right ")
         Speak("  she is a mad")


     elif 'mummy mobile details' in query:
         Speak("  Vivo1609")
         Speak("  your public ip address 2409:4064:2308:1801::259c:90b1")
         Speak("  Your IMEI number1 864165036628556")
         Speak("  Your second IMEI Number 864165036628549")

     elif 'dad mobile details' in query:
         Speak("  Your public ip address 2409:4064:e94:1050::18cb:3d01 ")
         Speak("  Your IMEI number1 869950045975998 ")
         Speak("  Youe second IMEI number 869950045975980 ")

     elif 'how are you' in query:
         Speak("   I am fine sir")
         Speak("    whats about you")

     elif 'you can quit' in query:
         Speak("  ok sir you can call me anytime!!")
         break

     elif 'jarvis give me water' in query:
         Speak("Sir call your Mon or dad to give water")
         Speak("I can only do computer work because i dont have hands")

     elif 'hi' in query:
         Speak("Hi sir")

     elif 'neha is telling something' in query:
         Speak("Chup ho ja 7thvi phel")
         Speak("apna ja apna aokad dekh")

     elif 'search youtube' in query:
         Speak("Ok Sir, This is What I found for your search! ")
         query = query.replace("jarvis", "")
         query = query.replace("search youtube", "")
         web = 'https://www.youtube.com/results?search_query=' + query
         webbrowser.open(web)
         Speak("Done Sir")

     elif 'search google' in query:
         Speak("This is what I Found")
         query = query.replace("jarvis", "")
         query = query.replace("search google", "")
         pywhatkit.search(query)
         Speak("Done Sir")

     elif 'website' in query:
         Speak("Ok sir,Launching...")
         query = query.replace("jarvis", "")
         query = query.replace("website", "")
         query = query.replace(" ","")
         web1 = query.replace("open", "")
         web2 = 'https://www.' + web1 + '.com'
         webbrowser.open(web2)
         Speak("Launched")

     elif 'music' in query:
         Music()

     elif 'you are amazing' in query:
         Speak("Thank you sir ")
         Speak("Thats all your progress")

     elif 'thank you ' in query:
         Speak("your are amazing sir")


     elif 'alarm' in query:
         Speak("Enter the time !")
         time = input(": Enter the time:")

         while True:
             Time_Ac = datetime.datetime.now()
             now = Time_Ac.strftime("%H:%M:%S")

             if now == time:
                 Speak("Time To wake up Sir")
                 playsound('Adam_Oh_-_Trapped_In_My_Mind_(Lyrics)(256k).mp3')
                 Speak("Alarm Closed")

             elif now > time:
                 break

     elif 'jarvis where is my phone' in query:
         import urllib.request
         import cv2
         import numpy
         import time

         URL = "http://100.83.88.12:8080/shot.jpg"
         while True:
             img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
             img = cv2.imdecode(img_arr, -1)
             cv2.imshow('IPWebcam', img)
             q = cv2.waitKey(1)
             if q == ord("q"):
                 break;

     elif '' in query:
         import urllib.request
         import cv2
         import numpy
         import time

         URL = "http://100.66.45.92:8080/shot.jpg"
         while True:
             img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
             img = cv2.imdecode(img_arr, -1)
             cv2.imshow('IPWebcam', img)
             q = cv2.waitKey(1)
             if q == ord("q"):
                 break;


     elif 'good morning ' in query:
         Speak("Good Morning sir")
         Speak("How can I help you sir")

     elif 'Good Afternoon' in query:
         Speak("Good Afternoon Sir")
         Speak("How can I help you sir")

     elif 'Good Evening' in query:
         Speak("Good Evening Sir")
         Speak("How can I help you sir")

     elif 'neha is scrolling me' in query:
         Speak("He dont dare to scroll")
         Speak("my sir")
         Speak("or you dont think what can i do")

     elif 'kunal is scrolling me' in query:
         Speak("hahahaha My sir is correct")
         Speak("my sir scrolls me when someone do bad things")
         Speak("My sir is so intelligent hahahaha")

     elif 'you can sleep ' in query:
         Speak("ok sir i am going to sleep")
         Speak("You can call me anytime")
         break

     elif 'remember that' in query:

         remeberMsg = query.replace("remember that", "")
         remeberMsg = remeberMsg.replace("jarvis", "")
         Speak("You tell Me To Remind You that :" + remeberMsg)
         remeber = open('data.txt', 'w')
         remeber.write(remeberMsg)
         remeber.close()

     elif 'what do you remember' in query:
         remeber = open('data.txt', 'r')
         Speak("You tell me to remember this" + remeber.read())


     elif "temperature" in query:
         Temp()

     elif "whatsapp message" in query:
         Whatsapp()

     elif "send whatsapp" in query:
         WhatsappMsg('niraj', 'lol')

     elif 'what are you doing' in query:
         Speak("I am thinking about you ")

     elif 'bye' in query:
         Speak("Ok bye sir")
         Speak("You can call me anytime")

     elif 'this are my friends' in query:
         Speak("Oh Hello ")
         Speak("My name is Jarvis ")
         Speak("What is your name")

     elif 'screenshot' in query:
         ScreenShot()

     elif 'open pycharm community' in query:
         OpenApps()

     elif 'open edius eight' in query:
         OpenApps()

     elif 'close pycharm community' in query:
         CloseApps()

     elif 'close edius eight' in query:
         CloseApps()

     elif 'kunal is mad' in query:
         Speak("  You shut up")
         Speak("  You are mad not my sir")

     elif "temperature" in query:
         Temp()

     elif 'send message' in query:
         pywhatkit.sendwhatmsg("+918987510264", "Hello my name is heheheh",20,43)
         Temp()

     elif 'pause the video ' in query:
         keyboard.press('k')

     elif 'unpause the video ' in query:
         keyboard.press('k')

     elif 'restart the video' in query:
         keyboard.press('0')

     elif 'mute the video' in query:
         keyboard.press('m')

     elif 'unmute the video' in query:
         keyboard.press('m')

     elif 'skip the video' in query:
         keyboard.press('l')

     elif 'back the video' in query:
         keyboard.press('j')

     elif 'full screen' in query:
         keyboard.press('f')

     elif 'half screen' in query:
         keyboard.press('f')

     elif 'youtube tools' in query:
         YoutubeAuto()

     elif "whatsapp message" in query:
         Whatsapp()

     elif "send whatsapp" in query:
         WhatsappMsg()

     elif ' joke' in query:
         get = pyjokes.get_joke()
         Speak(get)

     elif 'jarvis repeat my words' in query:
         Speak("ok Sir, I will repeat you words")
         tom = takecommand()
         Speak(f"You Said : {tom}")

     elif 'my location' in query:
         Speak("Ok Sir , Wait a second")
         webbrowser.open("")

     elif 'dictionary' in query:
         Dict()


     elif 'video downloader' in query:
         root = Tk()
         root.geometry('500x300')
         root.resizable(0, 0)
         root.title("Youtube Video Downloader")
         Speak("Enter Video Url Here !")
         Label(root, text="Youtube Video Downloader", font='arial 15 bold').pack()
         link = StringVar()
         Label(root, text="Paste Yt Video URL Here", font='arial 15 bold').place(x=160, y=60)
         Entry(root, width=70, textvariable=link).place(x=32, y=90)


         def VideoDownloader():
             url = YouTube(str(link.get()))
             video = url.streams.first()
             video.download()
             Label(root, text="Downloaded", font='arial 15').place(x=180, y=210)


         Button(root, text="Download", font='arial 15 bold', bg='pale violet red', padx=2,
                command=VideoDownloader).place(x=180, y=150)

         root.mainloop()
         Speak("Video Downloaded")

     elif 'jarvis translate' in query:
         Tran()

     elif 'nasa news' in query:

         from Nasa import NasaNews
         Speak("Enter the Date for News")
         Date = input("Enter the date")
         NasaNews(Date)

     elif 'near earth' in query:

         from Nasa import Astro
         Speak("Tell Me the start date")
         start = input("Enter The Starting date:")
         Speak("Tell me the End Date")
         End = input("Tell mee the end date")
         Astro(start,End)

     elif 'mars image' in query:

         from Nasa import MarsMission

         MarsMission()

     elif 'i have a question' in query:
         Solver()
         kk = Solver('temperature of Tamil nadu')
         print(kk)

     elif 'online class' in query:

         from features import OnlineClass

         Speak("Tell me the name of the Subject.")

         Class = takecommand()

         OnlineClass(Class)


TaskExe()

