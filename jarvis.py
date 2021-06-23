import numpy as np
import pyttsx3
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

def Speak(audio):
    print("  ")
    Assistant.say(audio)
    print(f": {audio}")
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

def TaskExe():

 Speak("")
Speak("Hello, I am Jarvis Sir. Please tell me How Can I help you")

def Music():
        Speak("Tell me The name of the song")
        musicName = takecommand()

        if 'Alert Kudey' in query:
                os.startfile('D:\Songs\PANJABI SONG\PUNJABI SONGS//Alert Kudey')

        else:
            pywhatkit.playonyt(musicName)

        Speak("Your song has been started , Enjoy that")


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

     elif 'search youtube' in query:
         Speak("Ok Sir, This is What I found for your search! ")
         query = query.replace("jarvis","")
         query = query.replace("search youtube","")
         web = 'https://www.youtube.com/results?search_query=' + query
         webbrowser.open(web)
         Speak("Done Sir")

     elif 'search google' in query:
         Speak("This is what I Found")
         query = query.replace("jarvis", "")
         query = query.replace("search google","")
         pywhatkit.search(query)
         Speak("Done Sir")

     elif 'website' in query:
         Speak("Ok sir,Launching...")
         query = query.replace("jarvis", "")
         query = query.replace("website", "")
         web1 = query.replace("open","")
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
         URL = "http://26.83.158.25:8080/shot.jpg"
         while True:
             img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
             img = cv2.imdecode(img_arr,-1)
             cv2.imshow('IPWebcam',img)
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

     elif 'Mummy is Scrolling me' in query:
         Speak("Kunal is a very good boy")
         Speak("dont dare to scroll him ")
         Speak("You are mad or what")

     elif 'kunal is scrolling me' in query:
         Speak("hahahaha My sir is correct")
         Speak("my sir scrolls me when someone do bad things")
         Speak("My sir is so intelligent hahahaha")

     elif 'you can sleep ' in query:
         Speak("ok sir i am going to sleep")
         Speak("You can call me anytime")
         break

     elif 'remember that' in query:

         remeberMsg = query.replace("remember that","")
         remeberMsg = remeberMsg.replace("jarvis","")
         Speak("You tell Me To Remind You that :"+remeberMsg)
         remeber = open('data.txt','w')
         remeber.write(remeberMsg)
         remeber.close()

     elif 'what do you remember' in query:
         remeber = open('data.txt','r')
         Speak("You tell me to remember this" + remeber.read())


     elif "temperature" in query:
         Temp()

     elif 'send message' in query:
         pywhatkit.sendwhatmsg("+918987510264", "Hello my name is heheheh",20,43)









TaskExe()