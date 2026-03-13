import pyautogui, threading, time
stop_flag = False

def start_click(interval=0.1):
    global stop_flag
    stop_flag = False
    def run():
        while not stop_flag:
            pyautogui.click()
            time.sleep(interval)
    threading.Thread(target=run, daemon=True).start()
    return "狂点模式"

def stop_click():
    global stop_flag
    stop_flag = True
    return "连点已停止"