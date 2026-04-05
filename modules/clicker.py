import threading
import time
import keyboard
import mouse

_running = False

def _click_loop():
    while _running:
        mouse.click()
        time.sleep(0.1)

def start_click():
    global _running
    _running = True
    threading.Thread(target=_click_loop, daemon=True).start()

def stop_click():
    global _running
    _running = False

keyboard.add_hotkey("F3", start_click)
keyboard.add_hotkey("F4", stop_click)