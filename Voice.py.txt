import ctypes
import datetime
import json
import os
import shutil
import smtplib,ssl,csv
import subprocess
import time
from tkinter import Frame
from turtle import speed
import turtle
import webbrowser
from cv2 import VideoCapture
from ecapture import ecapture as ec
from urllib.request import urlopen

from newsapi import NewsApiClient
from numpy import true_divide
import pyjokes
import pyttsx3
import requests
import speech_recognition as sr
import wikipedia
import winshell
import wolframalpha
from twilio.rest import Client
import cv2
import requests,json
import pygame
from translate import Translator

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    assname = ("Ela")
    speak("I am your Assistant")
    speak(assname)
    speak("How can i Help you")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return takeCommand()

    return query

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

for i in range(6):
    for colours in ["red","magenta","blue","cyan","green","yellow","white"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)

turtle.hideturtle()

if __name__ == '__main__':
    clear = lambda: os.system('cls')


    clear()
    wishMe()

    while True:

        query = takeCommand().lower()

        if 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

            
        elif 'open insta' in query:
            speak("Here you go to Instagram\n")
            webbrowser.open("instagram.com")

        elif 'open facebook' in query:
            speak("Here you go to Facebook\n")
            webbrowser.open("facebook.com")

        elif 'play music' in query or "play a song" in query:
            speak("Here you go with music")
            music_dir = "D:\\music\\AUD-20201214-WA0104.mp3"
            songs = os.system(music_dir)
            print(songs)


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open chrome' in query:
            codePath = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)

        elif 'open whatsapp' in query:
            codePath = r"C:\\Users\\abin\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(codePath)

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Abin and jibin.")

        elif 'joke' in query or 'comedy' in query:
            speak(pyjokes.get_joke())

        elif "calculate" in query:

            app_id = 'LXUEPH-YXR8WKAYL2'
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif 'search' in query:

            query = query.replace("search", "")
            webbrowser.open(query)
      
        elif 'play' in query:

            query = query.replace("play", "")
            webbrowser.open("https://www.youtube.com/results?search_query/" + query + "")

        elif "who i am" in query:
            speak("If you talk then definitely your human.")

        elif "why you came" in query:
            speak("Thanks to Abin and jibin. further It's a secret")

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Abin and jibin")

        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister Abin and Jibin ")

        elif 'change wallpaper' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,0,"D:\\IMG_0409.JPG",0)
            speak("Background changed successfully")


        elif 'news' in query:

            try:
                jsonObj = urlopen(
                    '''https://newsapi.org/v2/top-headlines?country=in&apiKey=a76dba6e43064501bac75a4b5011421a''')
                data = json.load(jsonObj)
                i = 1

                speak('here are some top news')
                print('''=============== TOP NEWS  ============''' + '\n')

                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:

                print(str(e))




        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop ela from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.co.in/maps/place/" + location + "")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown /h")

        elif "shutdown" in query:
            speak("Make sure all the application are closed before sign-out.See you again")
            subprocess.call("shutdown /s")

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('abin.txt', "r+")
            file.truncate(0)
            file.write(note)
            file.close()
            speak("Successfully created note")


        elif "show note" in query or "show me the note" in query or "notes" in query:
            speak("Showing Notes")
            
            with open('abin.txt') as file:
                file = open('abin.txt', "r")
                print(file.read())
                speak("file.read()")

        elif "camera" in query:
            speak("Opening camera")
            vid = cv2.VideoCapture(0)
            speak("press Q for closing the camera")
            while(True):
                ret,frame = vid.read()
                cv2.imshow('frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q','Q'):
                    break
            vid.release()
            cv2.destroyAllwindows()




        elif "ela" in query:

            wishMe()
            speak("Hello there, How can i be of service")

        elif "weather" in query:
            api_key = 'b2cc8eb41ce2745977176f86529d7722'
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            city_name = "kalpatta"
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " + str(
                    current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                    current_pressure) + "\n humidity (in percentage) = " + str(
                    current_humidiy) + "\n description = " + str(weather_description))
                speak(" Temperature (in kelvin unit) = " + str(
                    current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                    current_pressure) + "\n humidity (in percentage) = " + str(
                    current_humidiy) + "\n description = " + str(weather_description))
            else:
                speak(" City Not Found ")

        elif "send message " in query:
            account_sid = 'AC2fbfea9275bd5e320d98da7284700801'
            auth_token = '191b400bc72a19adcd56b8b657125867'
            client = Client(account_sid, auth_token)

            message = client.messages.create(body=takeCommand(),from_='+17854250334',to='+917558840018')

            print(message.sid)

        elif "wikipedia" in query:
            speak("What shuld i check in wikipedia")
            note_text = takeCommand()
            speak('Searching Wikipedia')

            results = wikipedia.summary('note_text')
            wiki = results
            speak('According to Wikipedia')
            speak(wiki)

        elif "Good Morning" in query:
            speak("A warm" + query)
            speak("How are you Mister")

        # most asked question from google Assistant
        elif "will you be my " in query:
            speak("I'm not sure about, may be you should give me some time")

        elif "how are you" in query:
            speak("I'm fine, glad you me that")

        elif "i love you" in query:
            speak("It's hard to understand")

        elif "thank you" in query or "thanks" in query:
            speak("your wellcome")

        elif "translate" in query:
            speak("What shuld i translate")
            note_text = takeCommand()
            translator= Translator(from_lang="english",to_lang="spanish")
            translation = translator.translate(note_text)
            print(translation)
            speak("in spaninsh"+str(translation))
            translator1= Translator(from_lang="english",to_lang="german")
            translation1 = translator1.translate(note_text)
            print(translation1)
            speak("in german"+str(translation1))

        elif "send mail" in query:
            speak("What shuld i send")
            message = takeCommand()
            from_address = "abinshaji60@gmail.com"
            password = "abin@123"

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(from_address, password)
                with open("contacts_file.csv") as file:
                    reader = csv.reader(file)
                    email = "abinshaji.shaji1@gmail.com"
                    next(reader)  # Skip header row
                    server.sendmail(from_address,email,message,)

        if "what is" in query or "who is" in query:


            client = wolframalpha.Client("GKPV5U-XT9W7478JA")
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                speak("No results found. please try again")
                print("No results")

        elif "stop" in query or "exit" in query or "bye" in query:
            speak("Ok bye and take care")
            break
