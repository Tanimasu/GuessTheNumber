import tkinter as tk
import random
from tkinter import messagebox

# 生成随机数字
target_number = random.randint(0, 1024)


def check_guess():
    user_guess = entry_guess.get()

    try:
        user_guess = int(user_guess)
    except ValueError:
        messagebox.showerror("戳啦", "请输入一个有效的数字！")
        return

    if user_guess < target_number:
        messagebox.showinfo("提示", "猜小了！")
    elif user_guess > target_number:
        messagebox.showinfo("提示", "猜大了！")
    else:
        messagebox.showinfo("提示", "恭喜你，猜对了！")
        window.destroy()  # 关闭窗口


# 创建主窗口
window = tk.Tk()
window.title("猜数字游戏")

# 创建标签和输入框
label_prompt = tk.Label(window, text="请输入一个0~1024的数字：")
label_prompt.pack()
entry_guess = tk.Entry(window)
entry_guess.pack()

# 创建按钮
button_check = tk.Button(window, text="猜", command=check_guess)
button_check.pack()

# 运行主循环
window.mainloop()
