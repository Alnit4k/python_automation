import pyautogui
import keyboard
from time import sleep

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(789,749,(12,152,33), tolerance=10):
        pyautogui.press('a')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(880,750,(255,0,0), tolerance=10):
        pyautogui.press('s')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(967,744,(244,244,64), tolerance=10):
        pyautogui.press('j')
        sleep(0.05)