import tkinter  # 导入tkinter总包
from tkinter import messagebox  # 导入弹窗组件包
import logic


class UI(object):
    """A级窗口，主窗口"""

    def __init__(self):
        """初始化主窗口UI"""
        # 函数初始化
        self.time_label = None  # 时间标签
        # 工具初始化
        self.time = logic.Time()
        self.pop_up = PopUp()
        # 程序文件类初始化
        self.file = logic.File()  # 文件操作
        self.log = logic.Log()  # 日志
        self.database = logic.Database()  # 数据库
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

    def __auto_update_time(self):
        """时间标签更新"""
        now_time = self.time.time()
        self.time_label.config(text=now_time)
        self.window_main.after(1000, self.__auto_update_time)  # 主窗口每一秒执行一次

    def __auto_update_schedule(self, today_schedule_frame):
        """每3000毫秒执行一次更新日程"""
        self.__update_schedule(today_schedule_frame)
        self.window_main.after(3000, lambda: self.__auto_update_schedule(today_schedule_frame))

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

    def __update_schedule(self, today_schedule_frame):
        """刷新日程"""
        # 清空日程列表
        for i in today_schedule_frame.winfo_children():
            i.destroy()
        # 重新绘制日程列表
        data = self.database.select_schedule()  # 获取日程
        init_height = 0.1
        if not data:
            tkinter.Label(today_schedule_frame, text="暂无数据", font=("Arial", 11)).place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.15)
        else:
            tkinter.Label(today_schedule_frame, text="日程信息", font=("Arial", 12), background="#FFFFFF").place(relx=0.25, rely=0.04, relwidth=0.5, relheight=0.15)
            for i in data:
                init_height += 0.1
                tkinter.Checkbutton(today_schedule_frame, text=i, font=("Arial", 11)).place(relx=0.05, rely=init_height, relwidth=0.9, relheight=0.15)

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
        self.__auto_update_time()  # 更新时间标签
        # 查询日程

        # 新建日程

        # 删除日程

        # 更改日程

        # 今日日程
        today_schedule_frame = tkinter.Frame(self.home_frame, background="#FFFFFF")
        today_schedule_frame.place(relx=0.25, rely=0.25, relwidth=0.7, relheight=0.6)  # 今日日程框架
        # 日程信息显示
        self.__update_schedule(today_schedule_frame)
        # 刷新按钮
        update_button = tkinter.Button(self.home_frame, text="刷新", command=lambda: self.__update_schedule(today_schedule_frame))
        update_button.place(relx=0.85, rely=0.28, relwidth=0.06, relheight=0.06)
        # 自动更新日程
        self.__auto_update_schedule(today_schedule_frame)
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
        # 数据库初始化
        self.database = logic.Database()

    def __init_ui(self, window_main):
        """ui初始化"""
        self.window_b = tkinter.Toplevel(window_main)  # 创建B级窗口
        self.window_b.title('SMT Tool @2021-B级窗口')  # 设置标题
        self.window_b.iconbitmap(r"./resources/images/icon.ico")  # 程序窗口图标
        self.local_window_size = self.window_b.maxsize()  # 获取主机显示器大小
        self.window_b.geometry(
            "{}x{}+{}+{}".format(int(self.local_window_size[0] / 3), int(self.local_window_size[1] / 3),
                                 int(self.local_window_size[0] / 3), int(self.local_window_size[1] / 3)))  # 按比例缩放程序大小
        self.window_b.configure(background="#00BFFF")  # 设置背景色
        self.window_b.resizable(False, False)  # 禁止自由缩放窗口大小
        self.window_b.transient(window_main)  # 使得子窗口始终在父窗口之上
        self.window_b.grab_set()  # 模态对话框，锁定与父窗口交互
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
        """窗口关闭时执行"""
        self.check_window_B = False  # 窗口设为为False-未占用
        self.window_b.grab_release()  # 释放锁定
        self.window_b.destroy()

    def __schedule_save(self, schedule, year, month, day, hour, minute, second):
        """传入日程以及年月日时分秒数据，保存到数据库中"""
        if schedule is None:  # 空日程判断
            pop_up.information("日程不可为空！")
        else:  # 时间格式判断
            if year.isdigit() and month.isdigit() and day.isdigit() and hour.isdigit() and minute.isdigit() and second.isdigit():
                enter_save = self.pop_up.ask("确认保存吗？")
                if enter_save is True:
                    time = year + "-" + month + "-" + day + " " + hour + ":" + minute + ":" + second
                    run = self.database.insert_data(schedule, self.time.conversion(time))
                    if run == "Insert data success!":
                        self.pop_up.information("数据保存成功")
                    else:
                        self.pop_up.error("数据保存失败:{}".format(run))
                    self.__close()
                else:
                    pass
            else:
                self.pop_up.information("格式错误，请检查输入！")

    def new_schedule(self, window_main):
        """新建日程窗口"""
        if self.__window_check() is False:  # B级窗口占用检测
            self.__init_ui(window_main=window_main)  # 初始化B级窗口
            # 窗口设为为Ture-占用
            self.check_window_B = True
            # 日程标签
            schedule_label = tkinter.Label(self.window_b, text="日程信息", font=("Arial", 13))
            schedule_label.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.1)
            # 输入框
            schedule_enter = tkinter.Entry(self.window_b, font=("Arial", 11))
            schedule_enter.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.15)
            # 时间标签
            time_label = tkinter.Label(self.window_b, text="时间范围", font=("Arial", 13))
            time_label.place(relx=0.1, rely=0.35, relwidth=0.2, relheight=0.1)
            # 时间选择框架
            time_choose_frame = tkinter.Frame(self.window_b, background="#00BFFF")
            time_choose_frame.place(relx=0.1, rely=0.45, relwidth=0.8, relheight=0.3)
            # 变量接收
            year = tkinter.StringVar()
            month = tkinter.StringVar()
            day = tkinter.StringVar()
            hour = tkinter.StringVar()
            minute = tkinter.StringVar()
            second = tkinter.StringVar()
            # 时间标签
            time_choose_year_label = tkinter.Label(time_choose_frame, text="年:", font=("Arial", 13))  # 年标签
            time_choose_year_label.place(relx=0.03, rely=0.3, relwidth=0.06, relheight=0.23)
            time_choose_year_enter = tkinter.Entry(time_choose_frame, font=("Arial", 13), textvariable=year)  # 年输入框
            time_choose_year_enter.place(relx=0.09, rely=0.3, relwidth=0.11, relheight=0.23)
            time_choose_month_label = tkinter.Label(time_choose_frame, text="月:", font=("Arial", 13))  # 月标签
            time_choose_month_label.place(relx=0.20, rely=0.3, relwidth=0.06, relheight=0.23)
            time_choose_month_enter = tkinter.Entry(time_choose_frame, font=("Arial", 13), textvariable=month)  # 月输入框
            time_choose_month_enter.place(relx=0.26, rely=0.3, relwidth=0.09, relheight=0.23)
            time_choose_day_label = tkinter.Label(time_choose_frame, text="日:", font=("Arial", 13))  # 日标签
            time_choose_day_label.place(relx=0.35, rely=0.3, relwidth=0.06, relheight=0.23)
            time_choose_day_enter = tkinter.Entry(time_choose_frame, font=("Arial", 13), textvariable=day)  # 日输入框
            time_choose_day_enter.place(relx=0.41, rely=0.3, relwidth=0.09, relheight=0.23)
            time_choose_hour_label = tkinter.Label(time_choose_frame, text="时:", font=("Arial", 13))  # 时标签
            time_choose_hour_label.place(relx=0.50, rely=0.3, relwidth=0.06, relheight=0.23)
            time_choose_hour_enter = tkinter.Entry(time_choose_frame, font=("Arial", 13), textvariable=hour)  # 时输入框
            time_choose_hour_enter.place(relx=0.56, rely=0.3, relwidth=0.09, relheight=0.23)
            time_choose_minute_label = tkinter.Label(time_choose_frame, text="分:", font=("Arial", 13))  # 分标签
            time_choose_minute_label.place(relx=0.65, rely=0.3, relwidth=0.06, relheight=0.23)
            time_choose_minute_enter = tkinter.Entry(time_choose_frame, font=("Arial", 13), textvariable=minute)  # 分输入框
            time_choose_minute_enter.place(relx=0.71, rely=0.3, relwidth=0.09, relheight=0.23)
            time_choose_second_label = tkinter.Label(time_choose_frame, text="秒:", font=("Arial", 13))  # 秒标签
            time_choose_second_label.place(relx=0.8, rely=0.3, relwidth=0.06, relheight=0.23)
            time_choose_second_enter = tkinter.Entry(time_choose_frame, font=("Arial", 13), textvariable=second)  # 分输入框
            time_choose_second_enter.place(relx=0.86, rely=0.3, relwidth=0.09, relheight=0.23)
            # 保存按钮
            save_button = tkinter.Button(self.window_b, text="保存", command=lambda: self.__schedule_save(schedule_enter.get(), year.get(), month.get(), day.get(), hour.get(), minute.get(), second.get()))
            save_button.place(relx=0.75, rely=0.8, relwidth=0.17, relheight=0.12)

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
    pop_up.information("当前文件并不是程序主文件，请正确打开此程序！")

