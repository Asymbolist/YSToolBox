import subprocess
from utils.logger import Logger

def sync_time():
    try:
        subprocess.Popen("w32tm /resync", shell=True)
        Logger.success("时间校准成功")
        return "系统时间已校准"
    except:
        Logger.error("校时失败")
        return "校时失败"