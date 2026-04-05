import pyautogui
import threading
import time

stop_flag = False

def start_click(interval):
    global stop_flag
    stop_flag = False
    while not stop_flag:
        pyautogui.click()
        time.sleep(interval)

def stop_click():
    global stop_flag
    stop_flag = True