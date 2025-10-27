
import pyautogui

Key = {

    "press enter": lambda: pyautogui.press("enter",interval=0.5),
    "press centre": lambda: pyautogui.write(".",interval=0.5),
    "press tab button": lambda: pyautogui.press("tab",interval=0.5),
    "press alter": lambda: pyautogui.press("alt",interval=0.5),
    "press shift": lambda: pyautogui.press("shift",interval=0.5),
    "press backspace": lambda: pyautogui.press("backspace",interval=0.5),
    "press page up": lambda: pyautogui.press("pageup",interval=0.5),
    "press page down": lambda: pyautogui.press("pagedown",interval=0.5),
    "press home": lambda: pyautogui.press("home",interval=0.5),
    "press space": lambda: pyautogui.press("space",interval=0.5),
    "press end": lambda: pyautogui.press("end",interval=0.5),
    "press 1": lambda: pyautogui.press("1",interval=0.5),
    "press 2": lambda: pyautogui.press("2",interval=0.5),
    "press 3": lambda: pyautogui.press("3",interval=0.5),
    "press 4": lambda: pyautogui.press("4",interval=0.5),
    "press 5": lambda: pyautogui.press("5",interval=0.5),
    "press 6": lambda: pyautogui.press("6",interval=0.5),
    "press 7": lambda: pyautogui.press("7",interval=0.5),
    "press 8": lambda: pyautogui.press("8",interval=0.5),
    "press 9": lambda: pyautogui.press("9",interval=0.5),
    "press 0": lambda: pyautogui.press("0",interval=0.5),
    "control save": lambda: pyautogui.hotkey("ctrl", "s",interval=0.5),
    "control z": lambda: pyautogui.hotkey("ctrl", "z",interval=0.5),
    "control a": lambda: pyautogui.hotkey("ctrl", "a",interval=0.5),
    "control o": lambda: pyautogui.hotkey("ctrl", "o",interval=0.5),
    "control new": lambda: pyautogui.hotkey("ctrl", "n",interval=0.5),
    "control run": lambda: pyautogui.hotkey("ctrl", "p",interval=0.5),

}
