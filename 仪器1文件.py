from tkinter import *

主窗体 = Tk()
# --------

状态 = StringVar(主窗体)
状态.set("开")
数据 = IntVar(主窗体)
数据.set(0)

# --------


def 切换():
    if 状态.get() == "关":
        状态.set("开")
        # https://www.cnblogs.com/hhh5460/p/5284835.html
        滑动条['state'] = DISABLED
        滑动条文本['state'] = DISABLED
    else:
        状态.set("关")
        滑动条['state'] = NORMAL
        滑动条文本['state'] = NORMAL


# --------------

主窗体.wm_title("仪器1")
主窗体.wm_geometry("300x400")
实验名 = Label(主窗体, text="仪器1", font="微软雅黑 30")
实验名.grid_configure(row=1, column=1)
# -----------
开关框 = LabelFrame(主窗体)
开关框.grid_configure(row=2, column=1)
开关 = Label(开关框, text="开关", font="微软雅黑 15")
开关.grid_configure(row=1, column=1)
开关按钮 = Button(开关框, text=状态.get(), textvariable=状态,
              command=切换, font="微软雅黑 15")
# https://www.pythonf.cn/read/84665
开关按钮.grid_configure(row=2, column=1, padx=30, pady=30)
# ----------------
滑动条框 = LabelFrame(主窗体)
滑动条框.grid_configure(row=3, column=1)


def 滑动条数据(var):
    数据.set(滑动条.get())


滑动条 = Scale(滑动条框, from_=0, to=180, showvalue=True,
            orient=HORIZONTAL, length=300, command=滑动条数据, state=DISABLED)
滑动条.grid_configure(column=1, row=2)

滑动条文本 = Label(滑动条框, text="滑动条的值=", textvariable=数据,
              font="微软雅黑 10", state=DISABLED)
滑动条文本.grid_configure(row=1, column=1)

主窗体.mainloop()

'''
设计
--------------------------------
|            仪器1             |
|                              |
|     开关                     |
|    button                    |
|        滑动条文本            |
|            slide             |
--------------------------------

'''
