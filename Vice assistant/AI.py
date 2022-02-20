from __future__ import division
import math
from pdb import pm
from posixpath import split
from random import choice, random
from tkinter import Image
from winreg import QueryReflectionKey
import cv2
from httpcore import request
from matplotlib import image
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os, subprocess
import smtplib
from youtubesearchpython import *
import random
import pyautogui #screenshot
import time
from bs4 import BeautifulSoup
import requests
import numpy as np

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak(" Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('prakhargurjar02@gmail.com', 'prakhargurjar27')
    server.sendmail('prakhargurjar02@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        
        #search on wikipidia
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        #open yt
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
            speak('opening youtube')    

        #search on yt
        elif 'search on youtube' in query:
            speak('Searching on youtube...')
            query = query.replace('search on youtube', "")
            url = 'https://www.youtube.com/results?search_query='+query
            webbrowser.open(url)
            speak('Got the output opening on youtube')

        #open google
        elif 'open google' in query:
            webbrowser.open("https://google.com")
            speak('opening google')    

        #search on google
        elif 'search on google' in query:
            speak("searching on google")
            query = query.replace('search on google', '')
            url = 'https://www.google.com/search?q='+query
            webbrowser.open(url)
            speak('Heres what i found on google')

        #open stackoverflow
        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")  
            speak('opening stackoverflow')     

        #open instagram
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")
            speak('opening Instagram')     
           
        # open google doc
        elif 'open document' in query:
            url = "https://docs.google.com/document/u/0/?tgif=d"
            webbrowser.open(url)
            speak('opening Google docs')

        #open mail
        elif 'open mail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")     
            speak('opening mail')    
        
        #get your locarion
        elif 'what is my location' in query:
             url = "https://www.google.com/maps/search/Where+am+I+?/"
             webbrowser.get().open(url)     

        #finding a location  
        elif 'find a location' in  query:
            speak('Which location you want me to find?')
            location = takeCommand()
            webbrowser.open("https://www.google.com/maps/place/"+location)   
            speak('here is what i found for '+location)

        #play music
        elif 'play music' in query:
            music_dir = 'C:\\Song'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        #introducing
        elif 'introduce yourself' in query: 
            speech = 'Hello there; I am a prototype voice assistant ; i can do few of basic task like; simple calculation ; sending mail ; and even i can play with you  '
            speak(speech)





            #take screen shot
        elif 'capture my screen' in query:
            speak('taking screenshot')
            myScreenShot = pyautogui.screenshot()
            myScreenShot.save('./ScreenShots/screen.png')
            
        #rock paper scissor
        elif 'play with me' in query:
            speak('Lets play rock paper scissors')
            time.sleep(0.5)
            speak('please give your move among rock; paper; scissor;')
            pmove = takeCommand()
            moves = ['rock', 'paper', 'scissors']
            if ('rock' in pmove or 'paper' in pmove or 'scissor' in pmove):
                cmove = random.choice(moves)
                speak('the computer choses ' + cmove)
                
                if pmove==cmove:
                    speak("the match is draw")
                elif pmove== "rock" and cmove== "scissor":
                    speak("Player wins")
                elif pmove== "rock" and cmove== "paper":
                    speak("Computer wins")
                elif pmove== "paper" and cmove== "rock":
                    speak("Player wins")
                elif pmove== "paper" and cmove== "scissor":
                    speak("Computer wins")
                elif pmove== "scissor" and cmove== "paper":
                    speak("Player wins")
                elif pmove== "scissor" and cmove== "rock":
                    speak("Computer wins")
            else:
                speak('you didnt chose right word')
        
        
        #conversation
        elif 'hello' in query:
            speak("HELLO sir ,How are you?")
        elif "I am fine"in query:
            speak("Thats Great sir!")
        elif "how are you" in query:
            speak("Perfect sir!")
        elif "thank you "in query:
            speak("you are Welcome,Sir!")        

        #open camera  
        elif 'open camera'in query:
            speak('opening camera')
            subprocess.run('start microsoft.windows.camera:', shell=True)


        #get time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        #get temperature
        elif "temperature" in query:
            search = "temperature in indore"
            url = f"https://www.google.com/search?q={search}"
            r  = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current{search} is {temp}")

        #time table 
        elif 'open time table' in query:
            path = "E:\WhatsApp Image 2022-02-13 at 8.08.34 PM.jpeg"
            imageT= cv2.imread(path)
            window_name = "time table"
            speak('here is your time table')
            cv2.imshow(window_name, imageT)
            cv2.waitKey(0)

        #open vs code
        elif 'open code' in query:
            codePath = "C:\\Users\\gurja\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codePath)

        #toss a coin
        elif 'toss a coin' in query:
            moves = ['head', 'tail']
            computerChoice = random.choice(moves)
            flipingCoinResult = random.choice(moves)
            speak('The computer choses ' + computerChoice)

            if (flipingCoinResult == computerChoice):
                speak('The coin shows '+ flipingCoinResult + ' and the computer wins')
            else:
                speak('The coin shows '+ flipingCoinResult + ' and you won')
        
        #calculator
        elif 'calculate' in query:
            speak("Pleas Provide me with the calculation i have to do")
            equation = takeCommand()
            firstnumber = equation.split()[0]
            secondnumber = equation.split()[2]
            opr = equation.split()[1]
            
            speak("You Asked me for " + firstnumber + opr +secondnumber)
            if opr == '+':
                addition = (float(firstnumber)) + (float(secondnumber))
                speak("The answer is " + addition.__str__())
            if opr == '-' :
                subtraction = (float(firstnumber)) - (float(secondnumber))
                speak("The answer is " + subtraction.__str__())
            if  opr ==  'x':
                multiplication = (float(firstnumber)) * (float(secondnumber))
                speak("The answer is " + multiplication.__str__())
            if opr == 'divide' or opr ==  '/':
                division =   (float(firstnumber)) / (float(secondnumber)) 
                speak("The answer is " + division.__str__())
            if opr == 'power' :
                power = (float(firstnumber)) ** (float(secondnumber))
                speak("The answer is " + power.__str__())

            
            

        #send mail 
        elif 'email to prakhar' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "gurjardrhariom@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")
        

        
        #exit 
        elif 'exit' in query:
            speak('Going to sleep sir! Good Bye')
            exit()          
