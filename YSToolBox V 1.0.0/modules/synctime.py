import os

def sync_time():
    try:
        os.system("w32tm /resync")
        return True
    except:
        try:
            os.system("net time /set /yes")
            return True
        except:
            return False