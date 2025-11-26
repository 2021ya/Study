import time
import tkinter  # 导入UI总包
from tkinter import messagebox  # 导入弹窗组件包
import logic


class Main(object):
    """程序主类"""

    def __init__(self):
        """初始化程序"""
        # 目录初始化
        self.file = logic.File()
        self.log = logic.Log()
        # ui初始化
        self.window_main = tkinter.Tk()
        self.window_main.title('SMT Tool @2021')
        self.window_main.iconbitmap(r"./resources/images/icon.ico")
        self.local_window_size = self.window_main.maxsize()
        self.window_main.configure(background="#00BFFF")
        self.window_main.geometry("{}x{}+{}+{}".format(int(self.local_window_size[0] / 2), int(self.local_window_size[1] / 2), int(self.local_window_size[0] / 4), int(self.local_window_size[1] / 4)))
        self.window_main.resizable(False, False)

    def main(self):
        """主程序界面UI"""
        menu_main = tkinter.Menu(self.window_main, tearoff=0)  # 主菜单栏
        menu_setting = tkinter.Menu(menu_main, tearoff=0)  # 设置:二级菜单栏
        menu_new = tkinter.Menu(menu_main, tearoff=0)  # 新建:二级菜单栏

        # 一级菜单
        menu_main.add_cascade(label="设置", menu=menu_setting)
        menu_main.add_cascade(label="新建", menu=menu_new)

        # 设置:二级菜单
        menu_setting.add_cascade(label="主题", command="")

        # 新建:二级菜单
        menu_new.add_cascade(label="新建日常", command="")

        self.window_main.config(menu=menu_main)
        self.window_main.mainloop()


if __name__ == '__main__':
    run = Main()
    run.main()
