@echo off
chcp 65001 >nul
echo ========================================
echo Excel同步工具配置向导
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
echo 启动配置向导...
python setup_config.py

echo.
echo 配置完成！
pause 