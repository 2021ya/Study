import tkinter  # 导入tkinter总包
from tkinter import messagebox  # 导入弹窗组件包
import logic


class UI(object):
    """A级窗口，主窗口"""

    def __init__(self):
        """初始化主窗口UI"""
        # 时间初始化
        self.time_label = None
        # 工具初始化
        self.time = logic.Time()
        self.pop_up = PopUp()
        # ui初始化
        self.window_main = tkinter.Tk()  # 创建窗口
        self.window_main.title('SMT Tool @2021')  # 设置标题
        self.window_main.iconbitmap(r"./resources/images/icon.ico")  # 程序窗口图标
        self.local_window_size = self.window_main.maxsize()  # 获取主机显示器大小
        self.window_main.geometry("{}x{}+{}+{}".format(int(self.local_window_size[0] / 2), int(self.local_window_size[1] / 2),
                                                       int(self.local_window_size[0] / 4), int(self.local_window_size[1] / 4)))  # 按比例缩放程序大小
        self.window_main.resizable(False, False)  # 禁止自由缩放窗口大小
        self.main_frame = tkinter.Frame(self.window_main)  # 创建主框架组件,显示到程序窗口
        self.main_frame.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)  # 组件上方起点为顶部，左右两边都填充到边界，并且全部填充
        # 初始化所有界面
        self.home_frame = self.home()  # 主页
        self.schedule_frame = self.schedule()  # 日程
        self.setting_frame = self.setting()  # 设置
        self.about_frame = self.about()  # 关于
        # 打开软件时显示主页
        self.__show_frame(self.home_frame)
        # B级窗口初始化
        self.B_window = UIB()
        # 数据库初始化
        self.database = logic.Database()

    def update_time(self):
        """时间标签更新"""
        now_time = self.time.time()
        self.time_label.config(text=now_time)
        self.window_main.after(1000, self.update_time)  # 主窗口每一秒执行一次

    def __show_frame(self, page):
        """显示页面与侧边栏"""
        for i in [self.home_frame, self.schedule_frame, self.setting_frame, self.about_frame]:
            i.pack_forget()  # 隐藏所有界面
        page.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)  # 显示目标页面

        # 侧边栏
        sidebar_frame = tkinter.Frame(self.window_main, background="#009ACD")
        # logo
        logo = tkinter.Label(sidebar_frame, text="SMT Tool @2021", background="#009ACD", font=("Arial", 11))
        logo.place(relx=0.095, rely=0.02, relwidth=0.8, relheight=0.1)
        # 主页按钮
        home = tkinter.Button(sidebar_frame, text="主页", background="#009ACD", font=("Arial", 12), command=lambda: self.__show_frame(self.home_frame))
        home.place(relx=0, rely=0.14, relwidth=1, relheight=0.1)
        # 日程按钮
        schedule = tkinter.Button(sidebar_frame, text="日程", background="#009ACD", font=("Arial", 12), command=lambda: self.__show_frame(self.schedule_frame))
        schedule.place(relx=0, rely=0.26, relwidth=1, relheight=0.1)
        # 设置按钮
        setting = tkinter.Button(sidebar_frame, text="设置", background="#009ACD", font=("Arial", 12), command=lambda: self.__show_frame(self.setting_frame))
        setting.place(relx=0, rely=0.38, relwidth=1, relheight=0.1)
        # 关于按钮
        about = tkinter.Button(sidebar_frame, text="关于", background="#009ACD", font=("Arial", 12), command=lambda: self.__show_frame(self.about_frame))
        about.place(relx=0, rely=0.5, relwidth=1, relheight=0.1)

        sidebar_frame.place(relx=0, rely=0, relwidth=0.2, relheight=1)

    def menu(self):
        """菜单栏"""
        menu_main = tkinter.Menu(self.window_main, tearoff=0)  # 菜单栏
        menu_page = tkinter.Menu(menu_main, tearoff=0)   # 一级菜单栏:页面
        menu_new = tkinter.Menu(menu_main, tearoff=0)  # 一级菜单栏:新建
        menu_setting = tkinter.Menu(menu_main, tearoff=0)  # 一级菜单栏:设置
        menu_about = tkinter.Menu(menu_main, tearoff=0)  # 一级菜单栏:关于

        # 一级菜单
        menu_main.add_cascade(label="页面", menu=menu_page)
        menu_main.add_cascade(label="新建", menu=menu_new)
        menu_main.add_cascade(label="设置", menu=menu_setting)
        # 若不想有下拉菜单，直接使用.add_command就可以直接执行命令
        menu_main.add_command(label="关于", command=lambda: self.__show_frame(self.about_frame))

        # 页面:二级菜单
        menu_page.add_cascade(label="主页", command=lambda: self.__show_frame(self.home_frame))
        menu_page.add_cascade(label="日程", command=lambda: self.__show_frame(self.schedule_frame))
        menu_page.add_cascade(label="设置", command=lambda: self.__show_frame(self.setting_frame))
        menu_page.add_cascade(label="关于", command=lambda: self.__show_frame(self.about_frame))

        # 新建:二级菜单
        menu_new.add_cascade(label="新建日程", command=lambda: self.B_window.new_schedule(self.window_main))

        # 设置:二级菜单
        menu_setting.add_cascade(label="主题", command=lambda: self.pop_up.information("em...\n还没写，要不你先看看别的？"))

        # 关于:二级菜单
        pass

        self.window_main.config(menu=menu_main)  # 加载菜单栏

    """
    界面原理：创建一个frame页面框架，将此框架放到窗口主框架上，然后再此页面框架中添加元素，最后返回此页面，通过调用show_frame()函数来显示需要的页面
            每个界面的第一行目的是为了创建框架，同时也是为了给初始化界面的变量赋值，而每个界面函数都会返回此界面，如果需要展示返回的界面，那么就需要调用展示函数
    """

    def home(self):
        """主页"""
        self.home_frame = tkinter.Frame(self.main_frame, background="#00BFFF")  # 将此主页显示到主框架

        # 时间显示
        self.time_label = tkinter.Label(self.home_frame, text=self.time.time(), font=("Arial", 11))  # 创建一个时间标签
        self.time_label.place(relx=0.3, rely=0.02, relwidth=0.6, relheight=0.1)
        self.update_time()  # 更新时间标签

        # 今日日程
        today_schedule_frame = tkinter.Frame(self.home_frame, background="#FFFFFF")
        today_schedule_frame.place(relx=0.25, rely=0.25, relwidth=0.7, relheight=0.6)  # 今日日程框架

        data = self.database.select_recent_12h()  # 获取上下12小时的日程
        init_height = 0.1
        if data is None:
            tkinter.Label(today_schedule_frame, text="暂无数据").place(relx=0.2, rely=init_height, relwidth=0.6, relheight=0.1)
        else:
            for i in data:
                init_height += 0.1
                tkinter.Checkbutton(today_schedule_frame, text=i).place(relx=0.2, rely=init_height, relwidth=0.6, relheight=0.1)
        return self.home_frame

    def schedule(self):
        """日程"""
        self.schedule_frame = tkinter.Frame(self.main_frame, background="#00BFFF")

        # 测试代码
        label = tkinter.Label(self.schedule_frame, text="这是日程界面", font=("Arial", 11))
        label.place(relx=0.35, rely=0.4, relwidth=0.5, relheight=0.1)

        return self.schedule_frame

    def setting(self):
        """设置"""
        self.setting_frame = tkinter.Frame(self.main_frame, background="#00BFFF")

        # 设置保存按钮
        save_button = tkinter.Button(self.setting_frame, text="保存设置", font=("Arial", 10), command=lambda: self.pop_up.information("em...\n还没写，要不你先看看别的？"))
        save_button.place(relx=0.85, rely=0.85, relwidth=0.1, relheight=0.085)

        # 测试代码
        label = tkinter.Label(self.setting_frame, text="这是设置界面", font=("Arial", 11))
        label.place(relx=0.35, rely=0.4, relwidth=0.5, relheight=0.1)

        return self.setting_frame

    def about(self):
        """关于"""
        self.about_frame = tkinter.Frame(self.main_frame, background="#00BFFF")

        # 测试代码
        label = tkinter.Label(self.about_frame, text="这是关于界面", font=("Arial", 11))
        label.place(relx=0.35, rely=0.4, relwidth=0.5, relheight=0.1)

        return self.about_frame

    def main(self):
        """负责运行UI类"""
        self.menu()  # 展示菜单栏
        self.window_main.mainloop()  # 程序主窗口循环


class UIB(object):
    """B级窗口，二级窗口"""
    def __init__(self):
        # 窗口检测-只允许一个B级窗口出现
        self.check_window_B = False
        # 时间初始化
        self.time_label = None
        # 工具初始化
        self.time = logic.Time()
        self.pop_up = PopUp()
        # ui初始化默认设置
        self.window_b = None
        self.local_window_size = None

    def __init_ui(self, window_main):
        # ui初始化
        self.window_b = tkinter.Toplevel(window_main)  # 创建B级窗口
        self.window_b.title('SMT Tool @2021-B级窗口')  # 设置标题
        self.window_b.iconbitmap(r"./resources/images/icon.ico")  # 程序窗口图标
        self.local_window_size = self.window_b.maxsize()  # 获取主机显示器大小
        self.window_b.geometry(
            "{}x{}+{}+{}".format(int(self.local_window_size[0] / 3), int(self.local_window_size[1] / 3),
                                 int(self.local_window_size[0] / 4), int(self.local_window_size[1] / 4)))  # 按比例缩放程序大小
        self.window_b.resizable(False, False)  # 禁止自由缩放窗口大小
        self.window_b.attributes("-topmost", True)  # 置顶B级窗口
        # 自定义退出
        self.window_b.protocol("WM_DELETE_WINDOW", self.__close)

    def __window_check(self):
        """窗口检查，只允许一个B级窗口出现"""
        if self.check_window_B is True:
            self.pop_up.warning("已存在一个B级窗口，请先关闭当前B级窗口后再执行此操作！")
            return True
        else:
            return False

    def __close(self):
        self.check_window_B = False  # 窗口设为为False-未占用
        self.window_b.destroy()

    def new_schedule(self, window_main):
        """新建日程窗口"""
        if self.__window_check() is False:  # B级窗口占用检测
            self.__init_ui(window_main=window_main)  # 初始化B级窗口
            # 窗口设为为Ture-占用
            self.check_window_B = True
            # 测试代码
            label = tkinter.Label(self.window_b, text="这是B级窗口界面", font=("Arial", 11))
            label.place(relx=0.35, rely=0.4, relwidth=0.5, relheight=0.1)
        elif self.check_window_B is True:
            return


class PopUp(object):
    """弹窗类"""

    def __init__(self):
        pass

    @staticmethod
    def information(text):
        """信息"""
        messagebox.showinfo(title="Information", message=text)

    @staticmethod
    def warning(text):
        """警告"""
        messagebox.showwarning(title="Warning", message=text)

    @staticmethod
    def error(text):
        """错误"""
        messagebox.showerror(title="Error", message=text)

    @staticmethod
    def ask(text):
        """yes/no"""
        value = messagebox.askyesno(title="Choose", message=text)
        if value:
            return True
        elif not value:
            return False


if __name__ == '__main__':
    pop_up = PopUp()
    pop_up.information("当前文件并不是程序主文件，此文件为程序UI文件，请正确打开此程序！")

