# YSToolBox  V 1.0.0
Windows系统优化工具箱

## 项目介绍
YSToolBox 是一款基于 PyQt6 开发的 Windows 系统管理工具，集成一键清理、系统信息、快捷操作、定时任务、强制删除等常用功能，适合 Windows 用户使用。

## 功能介绍
- 一键清理：回收站、临时文件、系统缓存、日志文件等
- 系统信息：查看 CPU、内存、系统版本、磁盘等硬件信息
- 快捷工具：一键打开任务管理器、CMD、控制面板、设备管理器
- 结束无响应程序：一键杀死所有卡死进程
- 定时任务：定时关机、取消定时
- 强制删除：强制删除被占用、无法删除的文件/文件夹
- 鼠标连点：全局自动连点（F3 开始 / F4 停止）
- 快捷箭头：一键去除桌面快捷方式小箭头
- 开机启动项：查看系统开机自启程序
- 时间校准：同步网络标准时间

## 运行环境
### 系统环境要求
- 操作系统：Windows 10 / Windows 11（64 位）
- 运行权限：必须以管理员身份运行
- Python 版本：3.8 及以上
- 依赖库：PyQt6

### 最低硬件配置
- CPU：1 GHz 及以上 32/64 位处理器
- 内存：2 GB 及以上
- 硬盘：至少 100 MB 可用空间
- 显卡：支持基础 Windows 桌面显示

## 使用方法
- 打开项目文件夹，并打开CMD
- 安装依赖：```pip install PyQt6```
- 启动程序：```python main.py```

## 项目结构
```
YSToolBox/
├── main.py
├── ui/
│   ├── main_window.py
│   └── styles.py
├── modules/
│   ├── cleaner.py
│   ├── sysinfo.py
│   ├── shortcut.py
│   ├── killtask.py
│   ├── timer.py
│   ├── delete.py
│   ├── clicker.py
│   ├── arrow.py
│   ├── startup.py
│   └── synctime.py
└── res/
    └── logo.ico
```


## 注意事项
- 部分功能涉及系统文件操作，使用前请确保已保存重要数据并备份
- 本工具仅用于个人学习和非商业用途
- 禁止用于非法用途、游戏作弊等违规场景

## 开源协议
**Asymbolist Non-Commercial Share-Alike License v1.0**
- ✅ 允许学习、研究、非商业分发
- ✅ 允许修改源代码
- ❌ 禁止任何形式的商用
- ❌ 禁止去除作者版权信息
- ⚠️ 衍生作品必须使用相同协议开源
- ⚠️ 原项目闭源后，衍生作品必须同步停止公开发布

## 用户社区
### 微信公众号（WeChat Official Account）:开发者云笙Asymbolist
### QQ用户社区:224336421

## 作者
### 云笙Asymbolist  
GitHub：https://github.com/Asymbolist
