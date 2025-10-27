
import speech_recognition as sr
from Brain import fix_phrase
from Command import match_command, pro_command
import pyautogui
from Command_key import Key as key
from Search import search_and_run



SEARCH_DIR = r"C:\Users\java"
def Print_text(text):
    print("you said : ", text)


def Key_Board(text):
    if text.lower().startswith("capital "):
        rest = text[8:].strip()  # "capital " ke baad ka text
        if rest:
            pyautogui.write(rest.capitalize())  # Pehla letter capitalAutomatic
        return
    

    if text.lower().startswith("title "):
        rest = text[6:].strip()
        if rest:
            pyautogui.write(rest.title())  # Har shabd ka pehla letter capital
        return

 
    if text.lower() in key:
        key[text.lower()]()  # execute mapped command
    else:
        pyautogui.write(text,interval=0.1)  # normal typing
    
    

def Speech(language):

    commands = [ "open notepad", "mic off", "stop speech", "how are you","open cmd","open visual studio code", "open notepad++", "open file", "close file","close notepad","close visual studio code","close notepade","minimize window","maximize window","close all tab"]


    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:

        recognizer.adjust_for_ambient_noise(source)

        while True:
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio,language=language)
                text = fix_phrase(text.lower())

                if text.strip():
                     if "stop program" in text or "mic off" in text:
                         print("Stopping...")
                         break

                
                
                matched = match_command(text, commands)
                if matched:
                    pro_command(matched)

                elif text.startswith("open "):
                    query = text.replace("open ", "").strip()
                    search_and_run(query, SEARCH_DIR)

                else:
                    Key_Board(text)
                    print(text)

            except sr.UnknownValueError:
                print("sorry,i did not understand")


Speech(language='en-IN')            

