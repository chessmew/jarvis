import requests
import os
from PIL import Image
import pyttsx3
import random

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

Api_Key = "2152AISO0I3ykqsTeXc0v35ceY7AG7fRmuo93VZd"


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

NasaNews('2020-10-15')

def Astro(start_date,end_date):

    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={Api_Key}"

    r = requests.get(url)

    Data = r.json()

    Total_Astro = Data['element_count']

    neo = Data['near_earth_objects']

    Speak(f"Total Astroid between {start_date} and {end_date} Is : {Total_Astro}")

    Speak("Exact Data for Those Astroids are listed Below.")

    for body in neo[start_date]:

        id = body['id']

        name = body['name']

        absolute = body['absolute_magnitude_h']

        print(id, name, absolute)

def MarsMission():

    name = 'curiosity'

    date = '2021-07-20'

    Api_ = str(Api_Key)

    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{name}/photos?earth_date={date}&api_key={Api_}"

    r = requests.get(url)

    Data = r.json()

    photos = Data['photos'][:10]

    try:

        for index , photo in enumerate(photos):

            camera = photo['camera']

            rover = photo['rover']

            rover_name = rover['name']

            camera_name = camera['name']

            full_camera_name = camera['full_name']

            date_of_photo = photo['earth_date']

            img_url = photo['img_src']

            p = requests.get(img_url)

            img = f'{index}.jpg'

            with open(img,'wb') as file:
                file.write(p.content)

            Path_1 = "C:\\Users\\KUNAL\\Desktop\\kkk\\python\\Sample Generetor\\Jarvis Full Programs\\" + str(img)

            Path_2 = "C:\\Users\\KUNAL\\Desktop\\kkk\\Mars Picture\\" + str(img)

            os.rename(Path_1,Path_2)

            os.startfile(Path_2)

            Speak(f"This image was captured With : {full_camera_name}")

            Speak(f"This image was Captured on : {date_of_photo}")
            Speak(f"Rover name : {rover_name}")

    except:
        Speak("Something went wrong")


def MoonMission():

    name = 'Apollo 15'

    date = '2009-08-14'

    Api_ = str(Api_Key)

    url = f"https://api.nasa.gov/moon-photos/api/v1/rovers/{name}/photos?earth_date={date}&api_key={Api_}"

    r = requests.get(url)

    Data = r.json()

    photos = Data['photos'][:10]

    try:

        for index , photo in enumerate(photos):

            camera = photo['camera']

            rover = photo['rover']

            rover_name = rover['name']

            camera_name = camera['name']

            full_camera_name = camera['full_name']

            date_of_photo = photo['earth_date']

            img_url = photo['img_src']

            p = requests.get(img_url)

            img = f'{index}.jpg'

            with open(img,'wb') as file:
                file.write(p.content)

            Path_1 = "C:\\Users\\KUNAL\\Desktop\\kkk\\python\\Sample Generetor\\Jarvis Full Programs\\" + str(img)

            Path_2 = "C:\\Users\\KUNAL\\Desktop\\kkk\\Moon Picture\\" + str(img)

            os.rename(Path_1,Path_2)

            os.startfile(Path_2)

            Speak(f"This image was captured With : {full_camera_name}")

            Speak(f"This image was Captured on : {date_of_photo}")
            Speak(f"Rover name : {rover_name}")

    except:
        Speak("Something went wrong")

def Summary(Boby):

    list__ = ('1','2','3','4','5','6','7','8','9','10')

    value = random.choice(list__)

    path = "C:\\Users\\KUNAL\\Desktop\\kkk\\Kam ka\\" + str(value) + ".jpg"

    os.startfile(path)

    name = str(Boby)

    url = "https://hubblesite.org/api/v3/glossary/" + str(name)

    r = requests.get(url)

    Data = r.json()

    if len(Data) != 0:

        retur =  Data['definition']

        Speak(f"According To The Nasa : {retur}")

    else:

        Speak("No Data Available , Try Again Later!")









