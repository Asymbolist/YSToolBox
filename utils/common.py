import os

def get_downloads():
    return os.path.join(os.path.expanduser("~"), "Downloads")

def get_temp():
    return os.environ.get("TEMP", "")