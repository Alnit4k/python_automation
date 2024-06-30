import webbrowser   
import pyautogui
from time import sleep

pyautogui.moveTo(x=1690, y=190)
sleep(1)
webbrowser.open('https://cursoautomacao.netlify.app')
sleep(3)
pyautogui.scroll(-820)
sleep(1)
pyautogui.leftClick()
sleep(2)
pyautogui.typewrite("Misael Brito")
pyautogui.press('tab')
pyautogui.press('enter', presses=2, interval=0.50)
sleep(1)
pyautogui.scroll(-800)
sleep(1)
pyautogui.moveTo(x=475, y=175, duration=1)
pyautogui.click()
sleep(2)
pyautogui.press('enter')


for i in range (5):
    sleep(1)    
    pyautogui.press('tab', presses=2, interval=2)
    sleep(2)
    pyautogui.press('enter', presses=2, interval=2)
    sleep(2)



pyautogui.moveTo(x=1690, y=190, duration=1)
pyautogui.scroll(800)
pyautogui.click()
pyautogui.typewrite("sayonara")
pyautogui.press('tab')
pyautogui.press('enter')