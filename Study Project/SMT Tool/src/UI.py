import tkinter  # 导入UI总包
from tkinter import messagebox  # 导入弹窗组件包


class UI(object):
    """UI主类"""

    def __init__(self):
        """初始化UI"""
        # ui初始化
        self.window_main = tkinter.Tk()  # 创建窗口
        self.window_main.title('SMT Tool @2021')  # 设置标题
        self.window_main.iconbitmap(r"./resources/images/icon.ico")  # 程序窗口图标
        self.local_window_size = self.window_main.maxsize()  # 获取主机显示器大小
        self.window_main.geometry("{}x{}+{}+{}".format(int(self.local_window_size[0] / 2), int(self.local_window_size[1] / 2), int(self.local_window_size[0] / 4), int(self.local_window_size[1] / 4)))  # 按比例缩放程序大小
        self.window_main.resizable(False, False)  # 禁止自由缩放窗口大小
        self.frame = tkinter.Frame(self.window_main)  # 创建主框架组件,显示到程序窗口
        self.frame.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)  # 组件上方起点为顶部，左右两边都填充到边界，并且全部填充
        # 初始化所有界面
        self.home_frame = self.home()
        self.about_frame = self.about()
        # 显示主页
        self.show_frame(self.home_frame)

    def show_frame(self, page):
        """显示(置顶)页面"""
        for i in [self.home_frame, self.about_frame]:
            i.pack_forget()  # 隐藏所有界面
        page.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)  # 显示目标页面

    def menu(self):
        """菜单栏"""
        menu_main = tkinter.Menu(self.window_main, tearoff=0)  # 菜单栏
        menu_setting = tkinter.Menu(menu_main, tearoff=0)  # 一级菜单栏:设置
        menu_new = tkinter.Menu(menu_main, tearoff=0)  # 一级菜单栏:新建

        # 一级菜单
        menu_main.add_cascade(label="设置", menu=menu_setting)
        menu_main.add_cascade(label="新建", menu=menu_new)

        # 设置:二级菜单
        menu_setting.add_cascade(label="主题", command="")

        # 新建:二级菜单
        menu_new.add_cascade(label="新建日常", command="")

        self.window_main.config(menu=menu_main)  # 加载菜单栏

    def home(self):
        """主页"""
        self.home_frame = tkinter.Frame(self.frame, background="#00BFFF")  # 将此主页显示到主框架
        button = tkinter.Button(self.home_frame, text="test", command=lambda: self.show_frame(self.about_frame))
        button.place(x=100, y=100)
        return self.home_frame

    def about(self):
        self.about_frame = tkinter.Frame(self.frame, background="#00BFFF")
        label = tkinter.Label(self.about_frame, text="SMT Tool @2021")
        label.place(x=100, y=100)
        return self.about_frame

    def main(self):
        """主UI界面，负责管理各个页面"""
        self.menu()  # 展示菜单栏
        self.window_main.mainloop()  # 程序主窗口循环



