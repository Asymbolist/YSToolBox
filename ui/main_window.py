from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from ui.styles import GLASS_STYLE
from modules import cleaner, sysinfo, shortcut, killtask, timer, delete, clicker, arrow, startup, synctime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YSToolBox 1.0.0")
        self.setFixedSize(920, 680)
        self.setStyleSheet(GLASS_STYLE)
        self.init_ui()

    def init_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QHBoxLayout(central)
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)

        nav = QWidget()
        nav.setFixedWidth(180)
        nav_layout = QVBoxLayout(nav)
        nav_layout.setContentsMargins(20,26,20,20)
        nav_layout.setSpacing(10)

        title = QLabel("YSToolBox")
        title.setStyleSheet("font-size:18px; font-weight:600; color:white;")
        nav_layout.addWidget(title)
        nav_layout.addSpacing(10)

        self.menu = QListWidget()
        self.menu.addItems([
            "一键清理", "系统信息", "快捷工具", "结束无响应程序",
            "定时任务", "强制删除", "鼠标连点", "快捷箭头",
            "开机启动项", "时间校准"
        ])
        self.menu.currentRowChanged.connect(self.switch_page)
        nav_layout.addWidget(self.menu)

    # 内容区
        self.stack = QStackedWidget()
        self.stack.addWidget(self.page_cleaner())
        self.stack.addWidget(self.page_sysinfo())
        self.stack.addWidget(self.page_shortcut())
        self.stack.addWidget(self.page_kill())
        self.stack.addWidget(self.page_timer())
        self.stack.addWidget(self.page_delete())
        self.stack.addWidget(self.page_click())
        self.stack.addWidget(self.page_arrow())
        self.stack.addWidget(self.page_startup())
        self.stack.addWidget(self.page_sync())

    # 日志
        self.log = QTextEdit()
        self.log.setReadOnly(True)
        self.log.setMaximumHeight(130)
        self.log.setPlaceholderText("日志")

        right = QVBoxLayout()
        right.addWidget(self.stack)
        right.addWidget(self.log)

        right_widget = QWidget()
        right_widget.setLayout(right)

        main_layout.addWidget(nav)
        main_layout.addWidget(right_widget)

    # 一键清理·modules/cleaner.py
    def page_cleaner(self):
        w = QWidget()
        l = QVBoxLayout(w)
        l.setContentsMargins(40,40,40,40)
        info = QLabel("""
⚠️一键清理现仅支持的清理内容：
1. 回收站文件
2. Prefetch 文件
3. Logfiles 文件
4. Temp 文件
5. Download 文件
6. 系统缓存与日志文件
        """)
        info.setStyleSheet("font-size:14px; color:#ccc;")
        btn = QPushButton("一键清理")
        btn.clicked.connect(self.do_clean)
        l.addWidget(info)
        l.addWidget(btn)
        l.addStretch()
        return w

    # 系统信息·modules/sysinfo.py
    def page_sysinfo(self):
        w = QWidget()
        l = QVBoxLayout(w)
        btn = QPushButton("获取系统信息")
        btn.clicked.connect(self.do_sysinfo)
        self.info_text = QLabel()
        self.info_text.setStyleSheet("color:#eee; font-size:13px;")
        l.addWidget(btn)
        l.addWidget(self.info_text)
        l.addStretch()
        return w

    # 快捷工具·modules/shortcut.py
    def page_shortcut(self):
        w = QWidget()
        g = QGridLayout(w)
        g.addWidget(QPushButton("任务管理器", clicked=shortcut.open_taskmgr),0,0)
        g.addWidget(QPushButton("CMD", clicked=shortcut.open_cmd),0,1)
        g.addWidget(QPushButton("控制面板", clicked=shortcut.open_control),1,0)
        g.addWidget(QPushButton("设备管理器", clicked=shortcut.open_devmgmt),1,1)
        return w

    # 结束无响应进程·modules/killtask.py
    def page_kill(self):
        w = QWidget()
        l = QVBoxLayout(w)
        btn = QPushButton("结束所有无响应进程")
        btn.clicked.connect(self.do_kill)
        l.addWidget(btn)
        l.addStretch()
        return w

    # 定时任务·modules/timer.py
    def page_timer(self):
        w = QWidget()
        l = QVBoxLayout(w)
        self.time_input = QLineEdit()
        self.time_input.setPlaceholderText("输入分钟数")
        l.addWidget(self.time_input)
        l.addWidget(QPushButton("设置定时关机", clicked=self.do_timer))
        l.addWidget(QPushButton("取消定时", clicked=timer.cancel_shutdown))
        return w

    # 强制删除·modules/delete.py
    def page_delete(self):
        w = QWidget()
        l = QVBoxLayout(w)
        self.del_input = QLineEdit()
        self.del_input.setPlaceholderText("复制文件路径到此处")
        l.addWidget(self.del_input)
        l.addWidget(QPushButton("强制删除", clicked=self.do_delete))
        return w

    # 鼠标连点·modules/clicker.py
    def page_click(self):
        w = QWidget()
        l = QVBoxLayout(w)
        l.addWidget(QPushButton("开始连点（F3）", clicked=clicker.start_click))
        l.addWidget(QPushButton("停止连点（F4）", clicked=clicker.stop_click))
        return w

    # 快捷箭头·modules/arrow.py
    def page_arrow(self):
        w = QWidget()
        l = QVBoxLayout(w)
        l.addWidget(QPushButton("去除快捷箭头并重启资源管理器", clicked=self.do_arrow))
        return w

    # 开机启动项·modules/startup.py
    def page_startup(self):
        w = QWidget()
        l = QVBoxLayout(w)
        l.addWidget(QPushButton("查看开机启动项", clicked=startup.show_startup_window))
        return w

    # 时间校准·modules/synctime.py
    def page_sync(self):
        w = QWidget()
        l = QVBoxLayout(w)
        l.addWidget(QPushButton("网络校准时间", clicked=self.do_sync))
        return w

    def do_clean(self):
        msg = cleaner.run_all_clean()
        self.log.append(msg)

    def do_sysinfo(self):
        info = sysinfo.get_full_info()
        self.info_text.setText(info)

    def do_kill(self):
        cnt = killtask.kill_all_not_responding()
        self.log.append(f"已结束 {cnt} 个无响应进程")

    def do_timer(self):
        try:
            m = int(self.time_input.text())
            timer.set_shutdown(m)
            self.log.append(f"已设置 {m} 分钟后关机")
        except:
            self.log.append("请输入数字")

    def do_delete(self):
        p = self.del_input.text().strip('"')
        res = delete.force_delete(p)
        self.log.append(res)

    def do_arrow(self):
        arrow.remove_arrow()
        self.log.append("已去除箭头，资源管理器已重启")

    def do_sync(self):
        ok = synctime.sync_time()
        self.log.append("时间校准完成" if ok else "校准失败")

    def switch_page(self, i):
        self.stack.setCurrentIndex(i)