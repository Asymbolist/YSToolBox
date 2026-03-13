from PyQt6.QtWidgets import QDialog, QVBoxLayout, QTextEdit
import winreg

def get_startup_list():
    items = []
    paths = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce"
    ]
    for path in paths:
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path)
            i = 0
            while True:
                try:
                    name, val, typ = winreg.EnumValue(key, i)
                    items.append(f"{name} → {val}")
                    i += 1
                except:
                    break
            winreg.CloseKey(key)
        except:
            pass
    return items

def show_startup_window():
    dlg = QDialog()
    dlg.setWindowTitle("开机启动项")
    dlg.setFixedSize(600,400)
    lay = QVBoxLayout(dlg)
    text = QTextEdit()
    text.setReadOnly(True)
    lines = get_startup_list()
    text.setText("\n".join(lines) if lines else "无启动项")
    lay.addWidget(text)
    dlg.exec()