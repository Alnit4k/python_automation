import pyautogui
import keyboard
import win32api
import win32con
from time import sleep


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


pyautogui.click(888,579) 

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(1021 ,700,(0,0,0)):
        click(1021,700)
    if pyautogui.pixelMatchesColor(923,700,(0,0,0)):
        click(923,700)
    if pyautogui.pixelMatchesColor(849,700,(0,0,0)):
        click(849,700)
    if pyautogui.pixelMatchesColor(758,700,(0,0,0)):
        click(758,700)
   
