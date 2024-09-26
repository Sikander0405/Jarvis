import pyautogui
import time
import webbrowser

# while(True):
#     a=pyautogui.position()
#     print(a)
#     # search panel = 975 224
#     # song =560 572

webbrowser.open("https://www.youtube.co.in/")
time.sleep(6)
pyautogui.moveTo(975,224)
pyautogui.click()
pyautogui.write("softly",interval=0.01)
# pyautogui.hotkey('crtl','v')n
time.sleep(1)

pyautogui.press('enter')
time.sleep(2)

pyautogui.moveTo(560,572)
pyautogui.click()