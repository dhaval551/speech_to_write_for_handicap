import os
from difflib import get_close_matches

SEARCH_DIR = r"C:\JAVA"

def match_command(text,commands_list):

    text = text.lower()
    matches = get_close_matches(text,commands_list,n=1,cutoff = 0.6)
    if matches:
        return matches[0]
    return None


def pro_command(command):

    if command == "open notepad":
        os.system("notepad")
        return True

    elif command == "open cmd":
        os.system(f'start cmd /K "cd /d {SEARCH_DIR}"')
        return True

    elif command == "open visual studio code":
        os.system("code")
        return True
    
    elif command == "open notepad++":
        os.system("notepad++")
        return True
    
    elif command == "open file":
        os.system("explorer")
        return True
    
    elif command == "close file":
        os.system("taskkill /f /im explorer.exe")
        return True
    
    elif command == "close notepad":
        os.system("taskkill /f /im notepad.exe")
        return True
    

    elif command == "close visual studio code":
        os.system("taskkill /f /im code.exe")
        return True

    elif command == "close command prompt":
        os.system("taskkill /f /im cmd.exe")
        return True

    elif command == "close notepade++":
        os.system("taskkill /f /im notepad++.exe")
        return True
   
    elif command == "minimize window":
        os.system("powershell -command \"(New-Object -ComObject Shell.Application).MinimizeAll()\"")
        return True

    elif command == "maximize window":
        os.system("powershell -command \"(New-Object -ComObject Shell.Application).UndoMinimizeAll()\"")
        return True

    elif command == "close all tab":
        os.system("taskkill /f /im chrome.exe")
        return True