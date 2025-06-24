# Excel同步工具配置文件
# 请根据您的实际情况修改以下配置

# OneDrive中源Excel文件的完整路径
# 请将路径替换为您实际的OneDrive文件路径
SOURCE_FILE_PATH = r"D:\OneDrive\电商工作表_0520.xlsx"

# 要提取的工作表名称（必须与源文件中的工作表名称完全一致）
SHEET_NAMES = [
    "tianjin_shenzhen database",
    "2830 warehouse", 
    "booking file"
]

# 目标文件夹路径（提取的工作表将保存到这些文件夹中）
TARGET_FOLDERS = [
    r"D:\relax\tianjin_shenzhen_database",
    r"D:\relax\2830_warehouse", 
    r"D:\relax\booking_file"
]

# 同步设置
SYNC_SETTINGS = {
    "monitor_interval": 1,  # 监控间隔（秒）
    "debounce_time": 2,     # 防抖时间（秒）
    "wait_after_save": 1,   # 保存后等待时间（秒）
}

# 日志设置
LOG_SETTINGS = {
    "log_file": "excel_sync.log",
    "log_level": "INFO",  # DEBUG, INFO, WARNING, ERROR
    "console_output": True,
}

# Excel应用程序设置
EXCEL_SETTINGS = {
    "visible": False,        # Excel应用程序是否可见
    "display_alerts": False, # 是否显示Excel警告
    "enable_events": True,   # 是否启用Excel事件
} 