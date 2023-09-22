import pyttsx3, datetime, os, speech_recognition as sr, os.path
import cv2
import random
import urllib
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import sys
import time
import requests
import pyautogui


keshava = pyttsx3.init('sapi5')
voices = keshava.getProperty('voices');
keshava.setProperty('voices', voices[0].id)




def virinchi(audio):
    keshava.say(audio)
    print("virinchi - ",audio)
    keshava.runAndWait()

def  mic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=4,phrase_time_limit=5)
    try:
        print("Recognizing...")
        micin = r.recognize_google(audio, language='en-in')
        print("user said: ", micin)
        
    except Exception as e:
        print("Say that again please...")
        return "none"
    return micin


def updatetime():
    hour = int(datetime.datetime.now().hour)
    ct = time.strftime("%I:%M %p")
    if hour >= 0 and hour <= 12:
        virinchi("good morning, its "+ct)
    elif hour >= 12 and hour <= 18:
        virinchi("good afternoon, its "+ct)
    else:
        virinchi("good evening, its "+ct)
        

def songs():
    virinchi("You are now into the entertainment zone, which type of song do you prefer to listen.")
    while True:
        micin = mic().lower()
        if "hindi" in micin:
            kit.playonyt("Hit hindi songs")
        elif "old" in micin:
            kit.playonyt("Evergreen old songs")
        elif "english" in micin:
            kit.playonyt("best English hit songs")
        elif "punjabi" in micin:
            kit.playonyt("best punjabi hits ")
        else:
            virinchi("Sorry, I am currently not developed to perform this action")
        main()

def suffer():
    virinchi("Fasten Your seat belt and tell me your browser")
    while True:
        micin = mic().lower()
        if "Chrome" in  micin:
            npath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(npath)

        elif"msedge" in micin:
            npath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            os.startfile(npath)

def main():
    
    while True:
        micin = mic().lower()
        if "open notepad" in micin or "open the notepad" in micin:
                npath = "C:\\Windows\\system32\\notepad.exe"
                virinchi('opening notepad')
                os.startfile(npath)
        elif "close notepad" in micin or "close the notepad" in micin:
            virinchi("closing notepad")
            os.system("taskkill /f /im notepad.exe")
        
        elif 'hi' in micin :
            virinchi('Hello sir, how may I help you?')

        elif "open command prompt" in micin or "open the command prompt" in micin or "open cmd" in micin:
            virinchi('opening command prompt')
            os.system("start cmd")
        elif "close command prompt" in micin or "close cmd" in micin:
            virinchi("closing command prompt")
            os.system("taskkill /f /im cmd")

        elif "ip address" in micin:
            ip = get('https://api.ipify.org').text
            virinchi(f"your IP address is {ip}")

        elif "wikipedia" in micin or "who is" in micin:
            virinchi("searching ")
            micin = micin.replace("wikipedia","")
            results = wikipedia.summary(micin, sentences=2)
            virinchi("according to my search")
            virinchi(results)

        elif "time" in micin:
            updatetime()

        elif "play songs" in micin or "play song" in micin:
            songs()
        elif "play" in micin:
            micin = micin.replace("play","")
            virinchi("playing"+micin)
            kit.playonyt(micin)
        elif "close youtube" in micin or "close the youtube" in micin:
            virinchi("closing youtube")
            os.system("taskkill /f /youtube.com")
    
        elif "what is " in micin:
            url = "https://www.google.co.in/" + micin
            virinchi("searching about"+micin)
            webbrowser.open_new_tab(url)


        
        elif "shut down the system" in micin:
            os.system("shutdown /s /t 5")

        elif "restart the system" in micin:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in micin:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            
        elif 'switch the window' in micin:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif"online" in micin:
            suffer()

      
            
        else:
            virinchi("")

def password():
    
    while True:
        micin = mic().lower()
        if "hey virinchi" in micin or "hi virinchi" in micin:
            virinchi("Welcome")
            updatetime()
            main()
        else:
            virinchi("Say that again please")
        password()
password()










    
