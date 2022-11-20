from pynput import keyboard
import pyautogui, subprocess as sp
COMBINATIONS = [{keyboard.Key.f1},
                {keyboard.Key.f2},
                {keyboard.Key.f3},
                {keyboard.Key.f4},
                {keyboard.Key.f5},
                {keyboard.Key.f6},
                {keyboard.Key.f7},
                {keyboard.Key.f8},
                {keyboard.Key.f9},
                {keyboard.Key.f10}
                #{keyboard.KeyCode(char='a')}
                ]
current = set()
def dst():
    pyautogui.press("t")
    pyautogui.typewrite("Get Dusted! ")
    pyautogui.typewrite("Hard Dunked! ")
    pyautogui.press("enter")
def was():
    pyautogui.press("t")
    pyautogui.typewrite("What a Save Bot! ")
    pyautogui.typewrite("Uninstall Noob! ")
    pyautogui.press("enter")
def non():
    pyautogui.press("t")
    pyautogui.typewrite("Nice one Kid! ")
    pyautogui.typewrite("WP idiot! ")
    pyautogui.press("enter")
def gp():
    pyautogui.press("t")
    pyautogui.typewrite("Great Pass Biggot! ")
    pyautogui.typewrite("Ty for free Ball! ")
    pyautogui.press("enter")
def stfu():
    pyautogui.press("t")
    pyautogui.typewrite("Idiot! ")
    pyautogui.typewrite("Shut yo Stupid 4$$! ")
    pyautogui.press("enter")
def ban():
    pyautogui.press("t")
    pyautogui.typewrite("Go Keys! ")
    pyautogui.typewrite("Idiot Cret1n! ")
    pyautogui.typewrite("Beech A$$ Frag! ")
    pyautogui.press("enter")
def fl():
    pyautogui.press("t")
    pyautogui.typewrite("Bg Too EZ! ")
    pyautogui.typewrite("Legit Playing Bots! ")
    pyautogui.typewrite("Ty For Freelo! ")
    pyautogui.press("enter")
def bt():
    pyautogui.press("t")
    pyautogui.typewrite("Dogsh1t Team! ")
    pyautogui.typewrite("Worse than bots! ")
    pyautogui.typewrite("Worst Team Ever! ")
    pyautogui.press("enter")
    
def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if current == {keyboard.Key.f1}:dst()
        elif current == {keyboard.Key.f2}:was()
        elif current == {keyboard.Key.f3}:non()
        elif current == {keyboard.Key.f4}:gp()
        elif current == {keyboard.Key.f5}:stfu()
        elif current == {keyboard.Key.f6}:ban()
        elif current == {keyboard.Key.f7}:fl()
        elif current == {keyboard.Key.f8}:bt()
        elif current == {keyboard.Key.f9}:sp.call('calc.exe')
def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:listener.join()
