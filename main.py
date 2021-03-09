import time
from datetime import datetime
from pynput.keyboard import Controller, Key
from data import lst1

import webbrowser
import pyautogui
keyboard = Controller()

isStarted = False
today=datetime.today()
today=today.strftime("%A")
def zoomauto():
    isStarted = False
    today=datetime.today()
    today=today.strftime("%A")
    if(today=="Monday"):
        print("Monday")
        for i in lst1:
            while True:
                if isStarted == False:
                    if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]):
                        webbrowser.open(i[0])
                        time.sleep(10)
                        join_btn = pyautogui.locateCenterOnScreen('join_btn.jpg')
                        pyautogui.moveTo(join_btn)
                        pyautogui.click()
                        isStarted = True
                elif isStarted == True:
                    if datetime.now().hour == int(i[2].split(':')[0]) and datetime.now().minute == int(i[2].split(':')[1]):
                        keyboard.press(Key.alt)
                        keyboard.press('q')
                        keyboard.release(Key.alt)
                        keyboard.release('q')
                        time.sleep(1)
                        keyboard.press(Key.enter)
                        isStarted = False
                        break
    if(today=="Tuesday"):
        print("Tuesday")
        for i in lst2:
            while True:
                if isStarted == False:
                    if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]):
                        webbrowser.open(i[0])
                        isStarted = True
                elif isStarted == True:
                    if datetime.now().hour == int(i[2].split(':')[0]) and datetime.now().minute == int(i[2].split(':')[1]):
                        keyboard.press(Key.alt)
                        keyboard.press('q')
                        keyboard.release(Key.alt)
                        keyboard.release('q')
                        time.sleep(1)
                        keyboard.press(Key.enter)
                        isStarted = False
                        break
    if(today=="Wednesday"):
        print("Wednesday")
        for i in lst3:
            while True:
                if isStarted == False:
                    if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]):
                        webbrowser.open(i[0])
                        isStarted = True
                elif isStarted == True:
                    if datetime.now().hour == int(i[2].split(':')[0]) and datetime.now().minute == int(i[2].split(':')[1]):
                        keyboard.press(Key.alt)
                        keyboard.press('q')
                        keyboard.release(Key.alt)
                        keyboard.release('q')
                        time.sleep(1)
                        keyboard.press(Key.enter)
                        isStarted = False
                        break
    if(today=="Thursday"):
        print("Thursday")
        for i in lst4:
            while True:
                if isStarted == False:
                    if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]):
                        webbrowser.open(i[0])
                        isStarted = True
                elif isStarted == True:
                    if datetime.now().hour == int(i[2].split(':')[0]) and datetime.now().minute == int(i[2].split(':')[1]):
                        keyboard.press(Key.alt)
                        keyboard.press('q')
                        keyboard.release(Key.alt)
                        keyboard.release('q')
                        time.sleep(1)
                        keyboard.press(Key.enter)
                        isStarted = False
                        break
    if(today=="Sunday"):
        print("Sunday")
        for i in lst1:
            while True:
                if isStarted == False:
                    if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]):
                        webbrowser.open(i[0])
                        time.sleep(20)
                        join_btn = pyautogui.locateCenterOnScreen('D:\\python\\zoom makathon\\join_btn.jpg')
                        pyautogui.moveTo(join_btn)
                        pyautogui.click()
                        isStarted = True
                elif isStarted == True:
                    if datetime.now().hour == int(i[2].split(':')[0]) and datetime.now().minute == int(i[2].split(':')[1]):
                        keyboard.press(Key.alt)
                        keyboard.press(Key.f4)
                        keyboard.release(Key.alt)
                        keyboard.release(Key.f4)
                        time.sleep(1)
                        keyboard.press(Key.enter)
                        isStarted = False
                        break