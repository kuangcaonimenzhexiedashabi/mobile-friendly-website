# Excel工作表实时同步工具

这个工具可以从OneDrive共享的Excel工作簿中提取指定的工作表，并实现实时同步，同时保留所有公式和格式。

## 功能特点

- ✅ 从OneDrive Excel文件中提取指定工作表
- ✅ 保留所有公式（包括VLOOKUP等函数）
- ✅ 保留格式、列宽、行高
- ✅ 实时监控源文件变化并自动同步
- ✅ 不影响原表的多人协作编辑
- ✅ 详细的日志记录
- ✅ 可配置的设置

## 系统要求

- Windows 10/11
- Python 3.7+
- Microsoft Excel（已安装）
- 网络连接（访问OneDrive）

## 安装步骤

1. **安装Python依赖**
   ```bash
   pip install -r requirements.txt
   ```

2. **配置设置**
   编辑 `config.py` 文件，修改以下设置：
   
   ```python
   # 修改为您的OneDrive文件路径
   SOURCE_FILE_PATH = r"D:\OneDrive\电商工作表_0520.xlsx"
   
   # 确认工作表名称（必须与源文件完全一致）
   SHEET_NAMES = [
       "tianjin_shenzhen database",
       "2830 warehouse", 
       "booking file"
   ]
   
   # 修改目标文件夹路径
   TARGET_FOLDERS = [
       r"D:\relax\tianjin_shenzhen_database",
       r"D:\relax\2830_warehouse", 
       r"D:\relax\booking_file"
   ]
   ```

## 使用方法

1. **启动同步工具**
   ```bash
   python excel_sync_tool.py
   ```

2. **首次运行**
   - 工具会自动提取所有指定的工作表到目标文件夹
   - 每个工作表将保存为独立的Excel文件

3. **实时监控**
   - 工具会持续监控源文件的变化
   - 当源文件被编辑并保存时，会自动同步更新提取的工作表
   - 按 `Ctrl+C` 停止监控

## 文件结构

```
relax/
├── excel_sync_tool.py    # 主程序
├── config.py             # 配置文件
├── requirements.txt      # 依赖列表
├── README.md            # 说明文档
├── excel_sync.log       # 日志文件
├── tianjin_shenzhen_database/
│   └── tianjin_shenzhen database.xlsx
├── 2830_warehouse/
│   └── 2830 warehouse.xlsx
└── booking_file/
    └── booking file.xlsx
```

## 配置说明

### 主要配置项

- `SOURCE_FILE_PATH`: OneDrive中源Excel文件的完整路径
- `SHEET_NAMES`: 要提取的工作表名称列表
- `TARGET_FOLDERS`: 目标文件夹路径列表

### 同步设置

- `monitor_interval`: 监控间隔（秒）
- `debounce_time`: 防抖时间，避免重复触发
- `wait_after_save`: 保存后等待时间

### 日志设置

- `log_file`: 日志文件名
- `log_level`: 日志级别（DEBUG, INFO, WARNING, ERROR）
- `console_output`: 是否在控制台显示日志

## 注意事项

1. **文件路径**: 确保OneDrive文件路径正确，且文件可访问
2. **工作表名称**: 工作表名称必须与源文件中的名称完全一致（包括大小写和空格）
3. **权限**: 确保有足够的权限访问OneDrive文件和创建目标文件夹
4. **Excel进程**: 工具会启动Excel进程，请确保没有其他程序占用Excel
5. **网络连接**: 确保OneDrive文件已同步到本地

## 故障排除

### 常见问题

1. **"源文件不存在"错误**
   - 检查 `SOURCE_FILE_PATH` 是否正确
   - 确保OneDrive文件已同步到本地

2. **"连接Excel应用程序失败"错误**
   - 确保Microsoft Excel已安装
   - 关闭所有打开的Excel文件
   - 重启计算机后重试

3. **"工作表名称不匹配"错误**
   - 检查 `SHEET_NAMES` 中的名称是否与源文件完全一致
   - 注意大小写和空格

4. **同步不工作**
   - 检查日志文件 `excel_sync.log`
   - 确保源文件确实被修改并保存
   - 检查文件监控权限

### 日志查看

查看 `excel_sync.log` 文件了解详细的运行信息和错误信息。

## 技术支持

如果遇到问题，请检查：
1. 日志文件中的错误信息
2. 配置文件设置是否正确
3. 系统环境是否满足要求

## 更新日志

- v1.0: 初始版本，支持基本的工作表提取和实时同步功能 