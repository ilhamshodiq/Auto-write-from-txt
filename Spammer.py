import pyautogui
filenya = open("test.txt")
for word in filenya :
    pyautogui.typewrite(word)
    pyautogui.press("enter")
