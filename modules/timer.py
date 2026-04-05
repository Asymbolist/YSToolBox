import os

def set_shutdown(minutes):
    sec = minutes * 60
    os.system(f"shutdown /s /t {sec}")

def cancel_shutdown():
    os.system("shutdown /a")