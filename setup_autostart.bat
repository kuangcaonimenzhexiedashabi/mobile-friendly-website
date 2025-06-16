@echo off
echo 正在设置开机自启动...

:: 获取当前目录的绝对路径
set "CURRENT_DIR=%~dp0"
set "CURRENT_DIR=%CURRENT_DIR:~0,-1%"

:: 创建快捷方式到启动文件夹
powershell "$WS = New-Object -ComObject WScript.Shell; $SC = $WS.CreateShortcut('%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\ImageClicker.lnk'); $SC.TargetPath = '%CURRENT_DIR%\start_hidden.vbs'; $SC.WorkingDirectory = '%CURRENT_DIR%'; $SC.Save()"

echo 设置完成！
echo 程序将在下次开机时自动启动。
pause 