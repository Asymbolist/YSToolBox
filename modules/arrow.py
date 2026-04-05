import os
import winreg

def remove_arrow():
    try:
        key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, "lnkfile")
        winreg.DeleteValue(key, "IsShortcut")
        winreg.CloseKey(key)
    except:
        pass

    try:
        key2 = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, "piffile")
        winreg.DeleteValue(key2, "IsShortcut")
        winreg.CloseKey(key2)
    except:
        pass

    os.system("taskkill /f /im explorer.exe && start explorer.exe")