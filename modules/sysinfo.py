import platform
import psutil
import hashlib
import uuid
import os

def get_full_info():
    try:
    # 系统
        os_name = platform.system() + " " + platform.release()
        os_ver = platform.version()
        host = platform.node()

    # CPU
        cpu = platform.processor()
        cores = psutil.cpu_count(logical=True)

    # 内存
        mem = psutil.virtual_memory()
        mem_total = f"{mem.total / (1024**3):.1f} GB"
        mem_used = f"{mem.used / (1024**3):.1f} GB"

    # 硬盘
        disk = psutil.disk_usage("C:")
        disk_total = f"{disk.total / (1024**3):.1f} GB"

    # MAC和机器码
        mac = get_mac()
        mid = hashlib.md5(mac.encode()).hexdigest().upper()

        info = (
            f"操作系统：{os_name}\n"
            f"系统版本：{os_ver}\n"
            f"计算机名称：{host}\n\n"
            f"CPU：{cpu}\n"
            f"CPU线程：{cores}\n"
            f"内存：{mem_used} / {mem_total}\n"
            f"C盘总容量：{disk_total}\n\n"
            f"MAC地址：{mac}\n"
            f"机器码：{mid}"
        )
        return info
    except:
        return "获取信息失败，请重试！"

def get_mac():
    try:
        return ":".join(["{:02x}".format((uuid.getnode() >> i) & 0xff) for i in range(0, 8 * 6, 8)][::-1])
    except:
        return "获取失败，请重试！"