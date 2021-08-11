import pyautogui
import time

pyautogui.position() #이 코드는 콘솔창에서 실행하는 것이 편리하다.

pyautogui.moveTo(100,100,2) # x좌표, y좌표, 이동시간

pyautogui.click()

pyautogui.click(clicks=2, interval=2)

pyautogui.doubleClick()

time.sleep(1)

pyautogui.typewrite('hello')

pyautogui.typewrite(['enter'])
