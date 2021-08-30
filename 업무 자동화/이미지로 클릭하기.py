import pyautogui

num7 = pyautogui.locateCenterOnScreen('7.png') #None이 뜰 경우 콘솔에서 pip install opencv-python
pyautogui.click(num7)

#계산기 에서 1이 있는 좌표를 알아내 캡쳐하는 과정.-> 같은 폴더 내에 저장.
pyautogui.screenshot('1.png', region=(1592, 803,30,30)) # (파일명, region=(x좌표, y좌표, x넓이, y넓이)

num1 = pyautogui.locateCenterOnScreen('1.png')
pyautogui.click(num1)
