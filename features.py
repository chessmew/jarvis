from logging import PlaceHolder
from urllib.parse import uses_relative
from geopy import location
import pywhatkit
import wolframalpha
import os
import wikipedia
import click
from pywikihow import search_wikihow
import speech_recognition as sr
import webbrowser as web
import pyttsx3
from time import sleep
import requests

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
#print(voices[1].id)
Assistant.setProperty('voice', voices[0].id)

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

def DateConverter(Query):

    Date = Query.replace(" and ","-")
    Date = Date.replace(" and ","-")
    Date = Date.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace(" ","")

    return str(Date)

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

#kk = Solver('')
#print(kk)




def Pass(pass_inp):

    password = "jarvis its me"

    passs = str(password)

    if passs==str(pass_inp):

        Speak("Hello Sir, How are you Sir")

        import JarvisAi

    else:
        Speak("You are not my owner get lost immediately.")

#if __name__ == "__main__" :

  #  Speak("This file is for my sir and some particular people only ")
 #   Speak("If you want to access this file tell me the password first")

 #   pas = input("Enter the password :")

#    Pass(pas)

def OnlineClass(Subject):

    if 'science' in Subject:

        from Online import Science

        Link = Science()

        web.open(Link)

        sleep(8.5)

        click(x=1507, y=112)

        sleep(2.5)

        click(x=668, y=454)

        sleep(4.5)

        click(x=532, y=640)

        sleep(0.5)

        click(x=603, y=629)

        sleep(0.5)

        click(x=1109, y=490)

        Speak("Sir class has joined. Come fast")

    elif 'maths' in Subject:

        from Online import Maths

        Link = Maths()

        web.open(Link)

        sleep(8.5)

        click(x=1507, y=112)

        sleep(2.5)

        click(x=668, y=454)

        sleep(4.5)

        click(x=532, y=640)

        sleep(0.5)

        click(x=603, y=629)

        sleep(0.5)

        click(x=1109, y=490)

        Speak("Sir class has joined. Come fast")

    elif 'sst' in Subject:

        from Online import SST

        Link = SST()

        web.open(Link)

        sleep(8.5)

        click(x=1507, y=112)

        sleep(2.5)

        click(x=668, y=454)

        sleep(4.5)

        click(x=532, y=640)

        sleep(0.5)

        click(x=603, y=629)

        sleep(0.5)

        click(x=1109, y=490)

        Speak("Sir class has joined. Come fast")

    elif 'hindi' in Subject:

        from Online import Hindi

        Link = Hindi()

        web.open(Link)

        sleep(8.5)

        click(x=1507, y=112)

        sleep(2.5)

        click(x=668, y=454)

        sleep(4.5)

        click(x=532, y=640)

        sleep(0.5)

        click(x=603, y=629)

        sleep(0.5)

        click(x=1109, y=490)

        Speak("Sir class has joined. Come fast")

    elif 'english' in Subject:

        from Online import English

        Link = English()

        web.open(Link)

        sleep(8.5)

        click(x=1507, y=112)

        sleep(2.5)

        click(x=668, y=454)

        sleep(4.5)

        click(x=532, y=640)

        sleep(0.5)

        click(x=603, y=629)

        sleep(0.5)

        click(x=1109, y=490)

        Speak("Sir class has joined. Come fast")

    elif 'computer' in Subject:

        from Online import Computer

        Link = Computer()

        web.open(Link)

        sleep(8.5)

        click(x=1507, y=112)

        sleep(2.5)

        click(x=668, y=454)

        sleep(4.5)

        click(x=532, y=640)

        sleep(0.5)

        click(x=603, y=629)

        sleep(0.5)

        click(x=1109, y=490)

        Speak("Sir class has joined. Come fast")

    elif 'sanskrit' in Subject:

        from Online import Sanskrit

        Link = Sanskrit()

        web.open(Link)

        sleep(8.5)

        click(x=1507, y=112)

        sleep(2.5)

        click(x=668, y=454)

        sleep(4.5)

        click(x=532, y=640)

        sleep(0.5)

        click(x=603, y=629)

        sleep(0.5)

        click(x=1109, y=490)

        Speak("Sir class has joined. Come fast")

    elif 'gk' in Subject:

        from Online import GK

        Link = GK()

        web.open(Link)

        sleep(8.5)

        click(x=1507, y=112)

        sleep(2.5)

        click(x=668, y=454)

        sleep(4.5)

        click(x=532, y=640)

        sleep(0.5)

        click(x=603, y=629)

        sleep(0.5)

        click(x=1109, y=490)

        Speak("Sir class has joined. Come fast")

    else:
        Speak("There is no class of this name")

OnlineClass(Subject)

