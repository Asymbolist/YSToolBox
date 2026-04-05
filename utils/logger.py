import datetime
import os

class Logger:
    LOG_FILE = "ystoolbox.log"

    @staticmethod
    def log(level, msg):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        text = f"[{now}] [{level}] {msg}"
        print(text)
        try:
            with open(Logger.LOG_FILE, "a", encoding="utf-8") as f:
                f.write(text + "\n")
        except:
            pass

    @staticmethod
    def info(msg):
        Logger.log("INFO", msg)

    @staticmethod
    def success(msg):
        Logger.log("SUCCESS", msg)

    @staticmethod
    def error(msg):
        Logger.log("ERROR", f"{msg} → 我真服了！")