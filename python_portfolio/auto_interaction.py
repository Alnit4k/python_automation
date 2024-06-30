import webbrowser
import pyautogui
from time import sleep

webbrowser.open('https://www.facebook.com/')
sleep(5)
pyautogui.press('tab',presses=2, interval=1)
pyautogui.typewrite('nike',interval=0.5)
pyautogui.press('enter')
pyautogui.moveTo(x=900, y=200, duration=1)
sleep(3)
pyautogui.click()
pyautogui.moveTo(x=444, y=586)
sleep(1)
pyautogui.scroll(-2000)
sleep(1)
pyautogui.click()
im1= pyautogui.screenshot(region=(1580,315,100,40))
im1.save('screenshot.png')
curta = pyautogui.locateCenterOnScreen("screenshot.png")
sleep(1)
pyautogui.moveTo(curta)
sleep(1)
pyautogui.click()