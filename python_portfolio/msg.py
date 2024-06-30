import pyautogui
import webbrowser
from time import sleep

telefones = [557592497047, 557184077624, 553182397674]

for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(2)
    pyautogui.click(946,367, duration=1)
    sleep(3)
    pyautogui.press('tab', presses=2, interval=1)
    sleep(3)
    pyautogui.press('enter')
    sleep(20)
    pyautogui.typewrite('tu e gai mano?')
    sleep(5)
    pyautogui.press('enter')
    sleep(300)
