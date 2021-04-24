import pyperclip
import os


"""path = r'D:\Coding\hackathon\poison_ivy_pictures'
if not os.path.exists(path):
    os.mkdir(path)

while 1:
    url = pyperclip.waitForNewPaste()"""
import pyautogui, time
time.sleep(1)
for x in range(1,11):
    pyautogui.press('right')
    time.sleep(1)
    pyautogui.click((744, 656),button='right')
    pyautogui.press('v')
    time.sleep(1)
    filename='creeper'+str(x)+'.jpg'
    pyautogui.typewrite(filename)
    time.sleep(1)
    for _ in range(3):
        pyautogui.press('\t')
        time.sleep(0.3)
    pyautogui.press(' ')
    print(filename)
    time.sleep(1)
