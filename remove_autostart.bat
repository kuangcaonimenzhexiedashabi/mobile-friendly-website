@echo off
echo 正在移除开机自启动...

:: 删除启动文件夹中的快捷方式
del "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\ImageClicker.lnk"

echo 移除完成！
echo 程序将不再开机自动启动。
pause 