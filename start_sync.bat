@echo off
chcp 65001 >nul
echo ========================================
echo Excel工作表实时同步工具
echo ========================================
echo.

echo 正在检查Python环境...
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误: 未找到Python，请先安装Python 3.7+
    pause
    exit /b 1
)

echo 正在安装依赖包...
pip install -r requirements.txt

echo.
echo 正在启动同步工具...
echo 按 Ctrl+C 停止监控
echo.

python excel_sync_tool.py

echo.
echo 同步工具已停止
pause 