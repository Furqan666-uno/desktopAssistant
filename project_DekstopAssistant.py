import pyttsx3
import speech_recognition as sr
import datetime
import time
import wikipedia
import webbrowser
import pywhatkit as pw
import os
import pyautogui
import random
import cv2
import requests

engine= pyttsx3.init('sapi5') # sapi5 = text to speech engine
voices= engine.getProperty('voices') # extract list of available voices in sapi5
engine.setProperty('voice',voices[1].id) # voice[0]= set 0th voice in the list of voices in sapi5
engine.setProperty('rate',170) # adjust speech rate

def speak(audio): # for speaking text
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!')
    elif hour>=12 and hour<18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening')

def takeCommand(): # to listen to user 
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("'Listening.....")
        r.pause_threshold=1 # Wait for a pause to finish before recognizing
        audio= r.listen(source) # capture audio

    try:
        print("Recognizing....")
        query= r.recognize_google(audio, language= 'en-in') # google API for speech recognition
        print(f'User said {query}\n')
    
    except Exception as e:
        print("Say that again plz....")
        return 'None'
    return query

if __name__=='__main__':
    wishMe()
    while True:
        speak("How can I assist you today?")
        command = takeCommand().lower()

        if 'hello' in command:
            speak("Hello! How can I help you?")
            print("Hello! How can I help you?")

        elif 'Who are you' in command:  #1
            speak("I am a desktop assistant ")
            print("I am a desktop assistant ")
        
        elif 'Who  created you' in command:  #2
            speak("I was created by the owner of this laptop")
            print("I was created by the owner of this laptop")    
        
        elif 'what is ' in command:  #3
            speak("Searching Wikipedia...")
            command= command.replace('what is ','')
            results= wikipedia.summary(command, sentences= 2)
            speak('According to Wikipedia....\n')
            print(results)
            speak(results)

        elif 'who is ' in command:  #4
            speak("Searching Wikipedia...")
            command= command.replace('who is ','')
            results= wikipedia.summary(command, sentences= 2)
            speak('According to Wikipedia....\n')
            print(results)
            speak(results)

        elif 'just open google' in command:  #5
            webbrowser.open('google.com')

        elif 'open google' in command:  #6
            speak("What would you like to search")
            cmd= takeCommand().lower()
            webbrowser.open(f"{cmd}")
            results= wikipedia.summary(cmd, sentences=1)
            speak(results)

        elif 'just open youtube' in command:  #7
            webbrowser.open('youtube.com')

        elif 'open youtube' in command:  #8
            speak("What would you like to search")
            cmd= takeCommand().lower()
            pw.playonyt(f'{cmd}')

        elif 'search on youtube' in command:  #9
            command= command.replace('search on youtube','')
            webbrowser.open(f"www.youtube.com/results?search_query={command}")

        elif 'close browser' in command:  #10
            os.system('taskkill /f /im msedge.exe') # kill a running process in edge browser

        elif 'type' in command:  #11
            command= command.replace('type','')
            pyautogui.typewrite(f"{command}",0.1)

        elif 'open notepad' in command:  #12
            os.startfile("C:/Windows/System32/notepad.exe")

        elif 'close notepad' in command: #13
            os.system('taskkill /f /im notepad.exe')

        elif 'play random movie' in command:  #14
            location= 'D:/movies'
            movies= os.listdir(location)
            os.startfile(os.path.join(location,random.choice(movies)))

        elif 'close movie' in command:  #15
            os.system('taskkill /f /im vlc.exe')
        
        elif 'play fight club' in command:  #16
            location= 'D:/movies/Fight Club'
            os.startfile(location)

        elif 'tell me the time' in command:  #17
            curr_time= datetime.datetime.now().strftime('%D:%M')
            speak(f'Current time of your location is {curr_time}')

        elif 'shutdown the system' in command:  #18
            os.system('shotdown /s /t 5')

        elif 'subscribe' in command:  # 19
            pyautogui.hotkey('win') # press the windows key
            time.sleep(1)
            pyautogui.typewrite('chrome',0.1) # type chrome in windows search bar 
            time.sleep(1)
            pyautogui.press('enter') # press enter in windows search bar 
            time.sleep(2)
            pyautogui.typewrite('youtube.com',0.1) # write in chrome browser
            time.sleep(1)
            pyautogui.press('enter') # click enter in the browser
            time.sleep(2)
            pyautogui.moveTo(498, 169, duration=1) # move to youtubes search bar coordinates
            pyautogui.click(x=498, y=169, clicks=1, interval=0, button='left') # click the coordinates
            pyautogui.typewrite('ashish chanchlani vines',0.1) # type in the search bar
            time.sleep(1)
            pyautogui.press('enter') # press enter
            time.sleep(2)
            pyautogui.moveTo(1781, 855, duration=1) # move to subscribe button 
            pyautogui.click(x=1781, y=855, clicks=1, interval=0, button='left') # click that botton
            speak('subscribed')

        elif 'open camera' in command:  # 20
            cap = cv2.VideoCapture(0) # open the webcam
            # Check if the camera is opened successfully
            if not cap.isOpened():
                print("Error: Could not open webcam.")
                exit()
            while True:
                ret, img = cap.read()  # Capture a frame
                if not ret:
                    print("Error: Failed to grab frame.")
                    break  # Exit the loop if frame capture fails
                cv2.imshow('Webcam', img)  # Display the captured frame
                k = cv2.waitKey(50)
                if k == 27:  # Check for the 'Esc' key
                    break
            cap.release()
            cv2.destroyAllWindows() # close all open cv windows
            
        elif 'take screenshot' in command:  # 21
            speak('name the file for this screenshot')
            name= takeCommand().lower()
            time.sleep(2)
            img= pyautogui.screenshot()
            img.save(f'{name}.png')
            speak('screenshot taken')

        elif 'tell me my ip address' in command:  #22
            speak('checking')
            try:
                adress= requests.get('https://api.ipify.org').text
                print(adress)
                speak('Your ip adress is')
                speak(adress)
            except Exception as e:
                speak('network is week right now. Try again later.')

        elif 'volume up' in command:  #23
            for i in range(0,11):
                pyautogui.press('volumeup')

        elif 'volume down' in command:  #24
            for i in range(0,11):
                pyautogui.press('volumedown')

        elif 'exit' in command:
            speak("Goodbye!")
            break
        
        else:
            speak("Sorry, I didn't understand that command.")
            