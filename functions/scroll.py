import pyautogui
import time
import obsws_python as obs
import os as os
from subprocess import call
from functions.obs import OBSWebsocketsManager



def instaAuto(numberOfScrolls):
    pyautogui.sleep(3)
    for i in range(numberOfScrolls):
        pyautogui.scroll(-1)
        pyautogui.sleep(7)



def record():
    obswebsocketsmanager = OBSWebsocketsManager()
    time.sleep(5)

    obswebsocketsmanager.startRecord()
    print("record started")

    time.sleep(7)

    instaAuto(30)

    obswebsocketsmanager.stopRecord()

