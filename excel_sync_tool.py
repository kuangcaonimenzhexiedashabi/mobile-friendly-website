import os
import shutil
import time
import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import win32com.client
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging
from datetime import datetime
from config import *

# 配置日志
log_level = getattr(logging, LOG_SETTINGS["log_level"])
logging.basicConfig(
    level=log_level,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_SETTINGS["log_file"], encoding='utf-8'),
    ]
)

if LOG_SETTINGS["console_output"]:
    logging.getLogger().addHandler(logging.StreamHandler())

class ExcelSyncHandler(FileSystemEventHandler):
    def __init__(self, source_file, target_folders, sheet_names):
        self.source_file = source_file
        self.target_folders = target_folders
        self.sheet_names = sheet_names
        self.last_modified = 0
        self.extractor = ExcelSheetExtractor(source_file)
        
    def on_modified(self, event):
        if event.is_file and event.src_path == self.source_file:
            current_time = time.time()
            # 避免重复触发
            if current_time - self.last_modified > SYNC_SETTINGS["debounce_time"]:
                self.last_modified = current_time
                logging.info(f"检测到源文件变化: {event.src_path}")
                time.sleep(SYNC_SETTINGS["wait_after_save"])  # 等待文件完全保存
                self.sync_sheets()
    
    def sync_sheets(self):
        try:
            logging.info("开始同步工作表...")
            self.extractor.extract_all_sheets(self.sheet_names, self.target_folders)
            logging.info("同步完成")
        except Exception as e:
            logging.error(f"同步过程中出现错误: {str(e)}")

class ExcelSheetExtractor:
    def __init__(self, source_file_path):
        self.source_file_path = source_file_path
        self.excel_app = None
        
    def connect_to_excel(self):
        """连接到Excel应用程序"""
        try:
            self.excel_app = win32com.client.Dispatch("Excel.Application")
            self.excel_app.Visible = EXCEL_SETTINGS["visible"]
            self.excel_app.DisplayAlerts = EXCEL_SETTINGS["display_alerts"]
            self.excel_app.EnableEvents = EXCEL_SETTINGS["enable_events"]
            logging.info("成功连接到Excel应用程序")
        except Exception as e:
            logging.error(f"连接Excel应用程序失败: {str(e)}")
            raise
    
    def disconnect_from_excel(self):
        """断开Excel应用程序连接"""
        if self.excel_app:
            try:
                self.excel_app.Quit()
                self.excel_app = None
                logging.info("已断开Excel应用程序连接")
            except Exception as e:
                logging.error(f"断开Excel连接时出错: {str(e)}")
    
    def extract_sheet_with_formulas(self, sheet_name, target_file_path):
        """提取工作表并保留所有公式"""
        try:
            # 打开源工作簿
            workbook = self.excel_app.Workbooks.Open(self.source_file_path)
            worksheet = workbook.Worksheets(sheet_name)
            
            # 创建新的工作簿
            new_workbook = self.excel_app.Workbooks.Add()
            new_worksheet = new_workbook.Worksheets(1)
            new_worksheet.Name = sheet_name
            
            # 复制整个工作表内容（包括公式）
            used_range = worksheet.UsedRange
            used_range.Copy()
            new_worksheet.Range("A1").PasteSpecial(Paste=-4163)  # xlPasteAll
            
            # 复制列宽
            for col in range(1, used_range.Columns.Count + 1):
                source_col_width = worksheet.Columns(col).ColumnWidth
                new_worksheet.Columns(col).ColumnWidth = source_col_width
            
            # 复制行高
            for row in range(1, used_range.Rows.Count + 1):
                source_row_height = worksheet.Rows(row).RowHeight
                new_worksheet.Rows(row).RowHeight = source_row_height
            
            # 保存新工作簿
            new_workbook.SaveAs(target_file_path)
            new_workbook.Close()
            workbook.Close()
            
            logging.info(f"成功提取工作表 '{sheet_name}' 到 {target_file_path}")
            
        except Exception as e:
            logging.error(f"提取工作表 '{sheet_name}' 时出错: {str(e)}")
            raise
    
    def extract_all_sheets(self, sheet_names, target_folders):
        """提取所有指定的工作表"""
        try:
            self.connect_to_excel()
            
            for sheet_name, target_folder in zip(sheet_names, target_folders):
                # 确保目标文件夹存在
                os.makedirs(target_folder, exist_ok=True)
                
                # 构建目标文件路径
                target_file_path = os.path.join(target_folder, f"{sheet_name}.xlsx")
                
                # 提取工作表
                self.extract_sheet_with_formulas(sheet_name, target_file_path)
                
        finally:
            self.disconnect_from_excel()

def setup_file_monitoring(source_file, target_folders, sheet_names):
    """设置文件监控"""
    event_handler = ExcelSyncHandler(source_file, target_folders, sheet_names)
    observer = Observer()
    observer.schedule(event_handler, os.path.dirname(source_file), recursive=False)
    observer.start()
    
    logging.info(f"开始监控文件: {source_file}")
    return observer

def main():
    # 验证配置
    if not os.path.exists(SOURCE_FILE_PATH):
        logging.error(f"源文件不存在: {SOURCE_FILE_PATH}")
        logging.error("请在config.py中修改SOURCE_FILE_PATH为正确的文件路径")
        return
    
    if len(SHEET_NAMES) != len(TARGET_FOLDERS):
        logging.error("工作表名称和目标文件夹数量不匹配")
        return
    
    # 创建提取器实例
    extractor = ExcelSheetExtractor(SOURCE_FILE_PATH)
    
    # 首次提取所有工作表
    logging.info("开始首次提取工作表...")
    extractor.extract_all_sheets(SHEET_NAMES, TARGET_FOLDERS)
    
    # 设置文件监控
    observer = setup_file_monitoring(SOURCE_FILE_PATH, TARGET_FOLDERS, SHEET_NAMES)
    
    try:
        logging.info("监控已启动，按 Ctrl+C 停止...")
        while True:
            time.sleep(SYNC_SETTINGS["monitor_interval"])
    except KeyboardInterrupt:
        logging.info("正在停止监控...")
        observer.stop()
        observer.join()
        logging.info("监控已停止")

if __name__ == "__main__":
    main() 