import os
import shutil

def force_delete(path):
    if not path or not os.path.exists(path):
        return "路径不存在"
    try:
        if os.path.isfile(path):
            os.remove(path)
        else:
            shutil.rmtree(path)
        return "删除成功"
    except:
        return "删除失败，请重试"