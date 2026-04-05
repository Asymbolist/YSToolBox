import os
import shutil

def run_all_clean():
    log = []
    try:
        os.system("rd /s /q %systemdrive%\\$Recycle.bin")
        log.append("清空回收站")
    except: pass

    try:
        os.system("del /q /f /s C:\\Windows\\Prefetch\\*")
        log.append("清空Prefetch")
    except: pass

    try:
        os.system("del /q /f /s C:\\Windows\\System32\\LogFiles\\*")
        log.append("清空LogFiles")
    except: pass

    try:
        os.system("del /q /f /s %temp%\\*")
        log.append("清空Temp")
    except: pass

    try:
        down = os.path.join(os.path.expanduser("~"), "Downloads")
        for f in os.listdir(down):
            p = os.path.join(down, f)
            try:
                if os.path.isfile(p):
                    os.remove(p)
                else:
                    shutil.rmtree(p)
            except: pass
        log.append("清空Download")
    except: pass

    try:
        os.system("ipconfig /flushdns")
        os.system("del /q /f /s C:\\Windows\\SoftwareDistribution\\Download\\*")
        log.append("清理系统缓存与日志")
    except: pass

    return "\n".join(log)