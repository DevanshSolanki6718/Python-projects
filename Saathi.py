import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import os
import subprocess
import time
import pyautogui
import pyperclip
import traceback
import cv2

# Function to convert text to speech
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 120)  # Set speaking speed
    engine.say(text)
    engine.runAndWait()

# Function to capture speech and convert to text
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        data = recognizer.recognize_google(audio, language="en-in")
        print("You said:", data)
        return data.upper()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""

# Function to respond based on voice command
def respond_to_command(command):
    # Introduction
    if "YOUR NAME" in command:
        speak("My name is Saathi, your voice assistant.")

    # Tell current time
    elif "TIME" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
   
    # Open Google
    elif "OPEN GOOGLE" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")

    # Search on Google
    elif "SEARCH" in command and "GOOGLE" in command:
        try:
            search_data = command.split("SEARCH")[1].split("ON GOOGLE")[0].strip()
            if search_data:
                search_url = f"https://www.google.com/search?q={search_data.replace(' ','+')}"
                webbrowser.open(search_url)
                speak(f"Searching Google for {search_data}")
            else:
                speak("Please say what you want to search after 'search' and before 'on Google'.")    
        except Exception as e:
            speak("Sorry, I couldn't understand your search request.")
            print(e)

    # Close specific Google tab
    elif "CLOSE GOOGLE TAB" in command:
        try:
            keyword = command.replace("CLOSE GOOGLE TAB", "").strip()
            if not keyword:
                speak("Please say what you want to close after 'Close Google tab'.")
                return

            speak(f"Looking for a Google search tab related to {keyword}. Please make sure Chrome is in focus.")
            time.sleep(2)

            found = False
            for _ in range(10):  # Try up to 10 tabs
                pyautogui.hotkey('ctrl', 'l')      # Focus address bar
                time.sleep(0.5)
                pyautogui.hotkey('ctrl', 'c')      # Copy URL
                time.sleep(0.5)
                url = pyperclip.paste().strip().lower()

                print(f"URL found: {url}")

                if "google.com/search" in url and keyword.lower().replace(" ", "+") in url:
                    pyautogui.hotkey('ctrl', 'w')  # Close current tab
                    speak(f"Closed the Google tab for {keyword}")
                    found = True
                    break
                else:
                    pyautogui.hotkey('ctrl', 'tab')  # Move to next tab
                    time.sleep(0.5)

            if not found:
                speak(f"Could not find a Google tab for {keyword}")
        except Exception as e:
            speak("An error occurred while trying to close the Google tab.")
            print("Exception details:", e)
            traceback.print_exc()

    # Open YouTube
    elif "OPEN YOUTUBE" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")

    # Open Specific YouTube Channel
    elif "YOUTUBE CHANNEL" in command:
        parts = command.split("OPEN YOUTUBE CHANNEL")
        if len(parts) > 1:
            channel_name = parts[1].strip()
            if channel_name:
                search_url = f"https://www.youtube.com/results?search_query={channel_name}"
                webbrowser.open(search_url)
                speak(f"Opening YouTube channel {channel_name}")
            else:
                speak("Please say the channel name clearly after 'open YouTube channel'.")
        else:
            speak("Sorry, I didn't get the channel name.") 

    # Opening Camera
    elif "OPEN CAMERA" in command:
        try:
            speak("Opening Camera")
            os.system("start microsoft.windows.camera:")

        except Exception as e:
            speak("Unable to open the camera app.")
            print("Error:", e)   

    # Close Camera
    elif "CLOSE CAMERA" in command:
        try:
            speak("Closing Camera")
            time.sleep(1)
            pyautogui.hotkey('alt','f4')
        except Exception as e:
            speak("Unable to close the camera.")
            print("Error:", e) 

    #  Open Chrome
    elif "OPEN CHROME" in command:
        try:
            speak("Opening Chrome.")
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # Adjust if needed
            subprocess.Popen([chrome_path])          

        except Exception as e:
            speak("Unable to open the Chrome app.")
            print("Error:", e)   

    # Close Chrome
    elif "CLOSE CHROME" in command:
        try:
            speak("Closing Chrome")
            # time.sleep(1)
            pyautogui.hotkey('alt','f4')
        except Exception as e:
            speak("Unable to close the chrome.")
            print("Error:", e) 


    # Exit 
    elif "EXIT" in command or "STOP" in command:
        speak("Goodbye Devansh!")
        exit()

    # Fallback
    else:
        speak("Sorry, I didn't understand that.")

# Main loop
if __name__ == "__main__":
    speak("Welcome Devansh, This is Saathi - Your Voice Assistant.")
    while True:
        command = speech_to_text()
        if command:
            respond_to_command(command)
