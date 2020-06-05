import 仪器1文件
import 仪器2文件
import 仪器3文件
from tkinter import *


def 仪器1功能():
    仪器1文件.main()


def 仪器2功能():
    仪器2文件.main()


def 仪器3功能():
    仪器3文件.main()


# ---------------------
主窗体 = Tk()
主窗体.wm_title("虚拟实验")
主窗体.wm_geometry("500x300")
实验名 = Label(主窗体, text="虚拟实验", font="微软雅黑 30")
实验名.grid_configure(row=1, column=2)
# ---------------------------
仪器1 = Label(主窗体, text="仪器1", font="微软雅黑 20")
仪器1.grid_configure(row=2, column=1)
仪器1的地方 = LabelFrame(主窗体)
仪器1的地方.grid_configure(row=3, column=1)
仪器1填充 = Label(仪器1的地方, text="1234\n5678\n91011")
仪器1填充.grid_configure(row=1, column=1)
# ---------------------------
仪器2 = Label(主窗体, text="仪器2", font="微软雅黑 20")
仪器2.grid_configure(row=2, column=2)
仪器2的地方 = LabelFrame(主窗体)
仪器2的地方.grid_configure(row=3, column=2)
仪器2填充 = Label(仪器2的地方, text="1234\n5678\n91011")
仪器2填充.grid_configure(row=1, column=1)
# ---------------------------
仪器3 = Label(主窗体, text="仪器3", font="微软雅黑 20")
仪器3.grid_configure(row=2, column=3)
仪器3的地方 = LabelFrame(主窗体)
仪器3的地方.grid_configure(row=3, column=3)
仪器3填充 = Label(仪器3的地方, text="1234\n5678\n91011")
仪器3填充.grid_configure(row=1, column=1)
# ---------------------------
仪器1按钮 = Button(仪器1的地方, text='点此设置', command=仪器1功能,
               padx=10, pady=10, font="微软雅黑 15")
仪器1按钮.grid_configure(row=2, column=1)
# ---------------------------
仪器2按钮 = Button(仪器2的地方, text='点此设置', command=仪器2功能,
               padx=10, pady=10, font="微软雅黑 15")
仪器2按钮.grid_configure(row=2, column=1)
# ---------------------------
仪器3按钮 = Button(仪器3的地方, text='点此设置', command=仪器3功能,
               padx=10, pady=10, font="微软雅黑 15")
仪器3按钮.grid_configure(row=2, column=1)
# ---------------------------
制作 = Label(主窗体, text="制作：wuyudi")
制作.grid_configure(row=5, column=3)
主窗体.mainloop()


"""
设计：
-----------------------------------------------------
|            实验名                                  |
|     仪器1       仪器2         仪器3                |
|    点击设置    点击设置     点击设置               |
|                                                    |
-----------------------------------------------------
"""
