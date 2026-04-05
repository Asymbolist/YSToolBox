import os
from utils.logger import Logger

def force_delete(path):
    if not os.path.exists(path):
        return "文件不存在"
    try:
        os.system(f'del /f /s /q "{path}"')
        os.system(f'rd /s /q "{path}"')
        Logger.success(f"强制删除: {path}")
        return f"已强制删除: {path}"
    except:
        Logger.error("强制删除失败，请重试")
        return "删除失败"