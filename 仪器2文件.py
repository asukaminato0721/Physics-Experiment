from tkinter import *

def main():
    主窗体 = Tk()
    主窗体.wm_title("仪器2")
    主窗体.wm_geometry("400x300")
    实验名 = Label(主窗体, text="仪器2", font="微软雅黑 20")
    实验名.grid_configure(row=1, column=2)
    #文本 = Label(主窗体, text="不想做了，就这样吧", font="\"Sarasa Mono SC\" 20")
    文本 = Label(主窗体, text="不想做了，就这样吧", font="微软雅黑 20")
    文本.grid_configure(row=2, column=2)
    主窗体.mainloop()
if __name__ == "__main__":
    main()
