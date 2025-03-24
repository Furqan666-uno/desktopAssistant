import pyttsx3
import speech_recognition as sr
import pyautogui
import time 
import os

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold=1
        audio= r.listen(source)
    try:
        print("Recognizing....")
        command= r.recognize_google(audio, language= 'en-in') # google API for speech recognition
        print(f'User said {command}\n')
    
    except Exception as e:
        print("Say that again plz....")
        return 'None'
    return command

if __name__=="__main__":
    while True:
        speak('how can i assist you today')
        command= takeCommand().lower()

        if 'open chrome' in command:
            pyautogui.hotkey('win','2')

        # if 'miximize window' in command:
        #     speak('maximizing window')
        #     try:
        #         pyautogui.keyDown('win')  # Press the Windows key
        #         pyautogui.press('up')  # Press the Up arrow key once
        #         pyautogui.keyUp('win')  # Release the Windows key
        #     except Exception as e:
        #         speak('window is already maximized')

        elif 'google search' in command:
            time.sleep(1)
            command= command.replace('google search','')
            pyautogui.hotkey('alt','d')
            pyautogui.typewrite(f'{command}',0.1)
            time.sleep(1)
            pyautogui.press('enter')

        elif 'open new window' in command:
            pyautogui.hotkey('ctrl','n')

        elif 'open new tab' in command:
            pyautogui.hotkey('ctrl','t')

        elif 'move to next tab' in command:
            pyautogui.hotkey('ctrl','tab')
        
        elif 'move to previous tab' in command:
            pyautogui.hotkey('ctrl','shift','tab')

        elif 'open incognito window' in command:
            pyautogui.hotkey('ctrl','shift','n')

        elif 'close chrome' in command:
            os.system('taskkill /f /im chrome.exe')

        elif 'open youtube' in command:
            pyautogui.hotkey('win')
            time.sleep(1)
            pyautogui.typewrite('chrome',0.1)
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.hotkey('alt','d')
            pyautogui.typewrite('youtube.com',0.1)
            time.sleep(1)
            pyautogui.press('enter')
            
        elif 'youtube search' in command:
            command= command.replace('youtube search','')
            pyautogui.hotkey('/')
            pyautogui.typewrite(f'{command}',0.1)
            time.sleep(1)
            pyautogui.press('enter')

        elif 'see youtube shorts' in command:
            pyautogui.moveTo(59, 376, duration=1)
            pyautogui.click(x=59, y=376, clicks=1, interval=0, button='left')

        elif 'play video' in command:
            img = pyautogui.locateCenterOnScreen('Screenshot 2024-11-30 201010.png')
            if img:
                print("Image found at:", img)
            else:
                print("Image not found.")

        elif 'exit' in command:
            speak('goodbye')
            break

        else:
            speak('sorry, i dont understand that')
