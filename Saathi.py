import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os

def speech_to_text():
    response = pyttsx3.init()
    response.say("Welcome Devansh")
    response.runAndWait()
    
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.pause_threshold = 1
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio, language = "en-in")
            print(data)
        except sr.UnknownValueError:
            print("Didn't get it")


speech_to_text()