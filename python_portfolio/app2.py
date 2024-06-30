import pyautogui
import pyperclip
from time import sleep

def type_phrase(phrase):
    pyperclip.copy(phrase)
    pyautogui.hotkey('ctrl','v')

pyautogui.moveTo(717,1079,duration=1)
pyautogui.leftClick(x =717, y=1079, duration=2)
pyautogui.leftClick(x =717, y=340, duration=2)
pyautogui.typewrite('note')
pyautogui.leftClick(x =717, y=500, duration=2)
sleep(3)
pyautogui.leftClick(x =717, y=500, duration=1)
type_phrase('こんにちは世界')