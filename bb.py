import pyautogui

r = open('numbers.txt', 'r')
o = r.read()
l1 = []

l1.append(o)

print(l1)



# Klavye ile mesaj yazın ve Enter tuşuna basın



def bastir():
    for k in l1:
        pyautogui.typewrite("@")
        pyautogui.typewrite("+")
        pyautogui.typewrite(k)
        pyautogui.press('enter')






