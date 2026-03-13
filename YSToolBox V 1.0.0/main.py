import sys
import os
import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    # QT环境变量
os.environ["QT_QPA_PLATFORM"] = "windows"
os.environ["QT_WINDOWS_DPI_AWARENESS"] = "dpiUnaware"
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon  # 导入QIcon用于设置图标
from ui.main_window import MainWindow

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    if is_admin():
        return
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "main.py", None, 0)
    sys.exit(0)

def main():
    run_as_admin()
    app = QApplication(sys.argv)
    icon_path = os.path.join(os.path.dirname(__file__), "res", "logo.ico")
    app.setWindowIcon(QIcon(icon_path))
    window = MainWindow()
    window.setWindowIcon(QIcon(icon_path))
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()