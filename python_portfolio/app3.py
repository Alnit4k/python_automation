import pyautogui

captcha = pyautogui.locateOnScreen('play.png')


print(captcha)
pyautogui.click(captcha[0],captcha[1],duration=5)   