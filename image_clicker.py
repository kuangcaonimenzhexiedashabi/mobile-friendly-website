import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
import random
import os
import time
import sys

class PasswordDialog:
    def __init__(self, parent):
        self.result = None
        
        # 创建对话框窗口
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("输入密码")
        self.dialog.geometry("300x150")
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # 设置窗口位置在屏幕中央
        self.dialog.update_idletasks()
        width = self.dialog.winfo_width()
        height = self.dialog.winfo_height()
        x = (self.dialog.winfo_screenwidth() // 2) - (width // 2)
        y = (self.dialog.winfo_screenheight() // 2) - (height // 2)
        self.dialog.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        
        # 创建标签
        label = tk.Label(self.dialog, text="请输入密码：", font=("Arial", 12))
        label.pack(pady=10)
        
        # 创建密码输入框
        self.password_entry = tk.Entry(self.dialog, show="*", font=("Arial", 12))
        self.password_entry.pack(pady=10)
        
        # 创建确定按钮
        ok_button = tk.Button(self.dialog, text="确定", command=self.ok, font=("Arial", 12))
        ok_button.pack(pady=10)
        
        # 绑定回车键
        self.password_entry.bind('<Return>', lambda e: self.ok())
        
        # 设置焦点到输入框
        self.password_entry.focus_set()
        
    def ok(self):
        self.result = self.password_entry.get()
        self.dialog.destroy()

class ImageClicker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("图片点击器")
        
        # 获取屏幕尺寸
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        
        # 设置窗口全屏和置顶
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)
        
        # 禁用窗口关闭按钮
        self.root.protocol("WM_DELETE_WINDOW", lambda: None)
        
        # 创建画布
        self.canvas = tk.Canvas(self.root, width=self.screen_width, height=self.screen_height)
        self.canvas.pack()
        
        # 初始化计数器
        self.click_count = 0
        self.max_clicks = 1000
        
        # 获取当前脚本所在目录（兼容打包和源码运行）
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_path, "badd97c09d10ffb77bea4576c012aa3.jpg")
        self.original_image = Image.open(image_path)
        # 调整图片大小，保持宽高比
        self.image_size = (300, 300)
        self.original_image = self.original_image.resize(self.image_size, Image.Resampling.LANCZOS)
        
        # 创建目标区域
        self.create_target_area()
        
        # 绑定点击事件
        self.canvas.bind('<Button-1>', self.on_click)
        
        # 绑定回车键事件
        self.root.bind('<Return>', self.check_password)
        
    def check_password(self, event=None):
        # 创建密码输入对话框
        dialog = PasswordDialog(self.root)
        self.root.wait_window(dialog.dialog)
        
        if dialog.result == "我错了":
            # 暂时关闭，5秒后重启
            self.root.destroy()
            time.sleep(5)  # 等待5秒
            os.execv(sys.executable, ['python'] + sys.argv)  # 重启程序
        elif dialog.result == "真错了，再也不敢了":
            # 彻底关闭程序
            self.root.quit()
            sys.exit()
        
    def create_target_area(self):
        # 创建图片对象
        self.photo = ImageTk.PhotoImage(self.original_image)
        
        # 随机位置
        self.target_x = random.randint(0, self.screen_width - self.image_size[0])
        self.target_y = random.randint(0, self.screen_height - self.image_size[1])
        
        # 在画布上显示图片
        self.canvas.create_image(self.target_x, self.target_y, image=self.photo, anchor='nw')
        
    def on_click(self, event):
        # 检查点击是否在目标区域内
        if (self.target_x <= event.x <= self.target_x + self.image_size[0] and 
            self.target_y <= event.y <= self.target_y + self.image_size[1]):
            self.click_count += 1
            
            if self.click_count >= self.max_clicks:
                messagebox.showinfo("完成", f"恭喜！您已完成 {self.max_clicks} 次点击！")
                self.root.quit()
            else:
                # 清除画布并创建新的目标区域
                self.canvas.delete("all")
                self.create_target_area()
                
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ImageClicker()
    app.run() 