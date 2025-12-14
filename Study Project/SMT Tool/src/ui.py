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
        self.version = logic.Version()  # 版本号
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
        # 日程显示界面实例初始化--保存画布和滚动条到实例--若不保存到实例的话只会在此代码段执行的时候存在画布与滚动条，而在其他代码段执行时可能被销毁
        self.canvas = None
        self.scrollbar = None
        self.schedule_canvas = None
        self.schedule_scrollbar = None
        # 初始化所有界面
        self.home_frame = self.home()  # 主页
        self.schedule_frame = self.schedule()  # 日程
        self.setting_frame = self.setting()  # 设置
        self.about_frame = self.about()  # 关于
        # 打开软件时显示主页
        self.__show_frame(self.home_frame)
        # B级窗口初始化
        self.B_window = UIB()

    @classmethod
    def on_mouse_wheel(cls, event, canvas):  # event事件tkinter自己有了，会接收所有操作记录
        """鼠标滚轮事件处理"""
        if event.delta > 0:  # 向上滚动
            canvas.yview_scroll(-1, "units")  # 视图向下移动1单位
        elif event.delta < 0:  # 向下滚动
            canvas.yview_scroll(1, "units")  # 视图向上移动1单位

    @classmethod
    def update_scrollregion(cls, canvas):
        """更新滚动区域"""
        bbox = canvas.bbox("all")
        canvas.configure(scrollregion=bbox)  # 获取画布包所有组件的最小矩形，然后将画图滚动区域调整为此矩形

    def __auto_update_time(self):
        """时间标签更新"""
        now_time = self.time.time()
        self.time_label.config(text=now_time)
        self.window_main.after(1000, self.__auto_update_time)  # 主窗口每一秒执行一次

    def __count_finish(self, label1, label2):
        """更新统计"""
        count = self.database.count_finish()
        label1.config(text="已完成:{}".format(count[0]))
        label2.config(text="未完成:{}".format(count[1]))

    def __auto_update_schedule(self, inner_frame, label1, label2):
        """每3000毫秒执行一次更新日程+统计"""
        self.__update_schedule(inner_frame)
        self.__count_finish(label1, label2)  # 统计更新
        self.window_main.after(3000, lambda: self.__auto_update_schedule(inner_frame, label1, label2))

    def __auto_update_all_schedule(self, canvas, inner_frame):
        """自动更新所有日程界面"""
        self.select_all_schedule(canvas, inner_frame)
        self.window_main.after(3000, lambda: self.__auto_update_all_schedule(canvas, inner_frame))

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

    def __update_schedule_state(self, var, schedule_id):
        """更新日程状态（完成、未完成）"""
        run = self.database.update_schedule_state(var, schedule_id)
        if run == "Update schedule success!":
            self.pop_up.information("日程已更新！")
        else:
            self.pop_up.error("日程更改状态错误![Error:{}]".format(run))

    def __update_schedule(self, inner_frame):
        """传入内容框架，刷新日程"""
        # 清空日程列表
        for i in inner_frame.winfo_children():
            i.destroy()
        # 重新绘制日程列表
        data = self.database.select_schedule()  # 获取日程
        if not data:
            frame = tkinter.Frame(inner_frame)
            tkinter.Label(frame, text="暂无待办日程", font=("Arial", 13)).pack(fill="x")
            frame.pack(fill=tkinter.BOTH, padx=250, pady=30)
        else:
            frame = tkinter.Frame(inner_frame)
            tkinter.Label(frame, text="待办日程:", font=("Arial", 13)).pack(side="left", fill="x")
            frame.pack(fill=tkinter.BOTH, padx=20, pady=30)
            for schedule_data in data:
                schedule_id = schedule_data[0]  # 获取日程id
                var = tkinter.IntVar()
                tkinter.Checkbutton(frame, text=schedule_data, font=("Arial", 11), variable=var, onvalue=1, offvalue=0, command=lambda sid=schedule_id, v=var: self.__update_schedule_state(v.get(), sid)).pack(side="top", padx=10, pady=5, anchor="w")
        # 滚动区域更新
        self.update_scrollregion(self.canvas)

    def __delete_log_data(self):
        """删除日志数据"""
        if self.pop_up.ask("此操作将删除所有日志数据，确定执行吗？"):
            if self.log.delete_log_data() == "Delete log successfully!":
                self.pop_up.information("日志数据删除成功！")
            else:
                self.pop_up.error("日志数据删除失败！[Error:{}]".format(self.log.delete_log_data()))
        else:
            pass

    def __delete_data(self):
        """删除数据"""
        if self.pop_up.ask("你知道你在干什么吗？\n此操作将删除所有数据，你确定？？？"):
            if self.database.delete_data() == "Delete all data successfully!":
                self.pop_up.information("数据删除成功！")
            else:
                self.pop_up.error("数据删除失败！[Error:{}]".format(self.database.delete_data()))
        else:
            pass

    def select_all_schedule(self, canvas, inner_frame):
        """查询所有日程"""
        for i in inner_frame.winfo_children():
            i.destroy()
        data = self.database.select_schedule(all_schedule=True)
        if not data:
            frame = tkinter.Frame(inner_frame)
            tkinter.Label(frame, text="暂无数据", font=("Arial", 13)).pack(fill="x")
            frame.pack(fill=tkinter.BOTH, padx=257, pady=30)

        else:
            frame = tkinter.Frame(inner_frame)
            tkinter.Label(frame, text="所有日程:", font=("Arial", 13)).pack(side="left", fill="x")
            frame.pack(fill=tkinter.BOTH, padx=20, pady=30)
            for schedule_data in data:
                schedule_id = schedule_data[0]
                all_schedule = schedule_data[1]
                finish = schedule_data[2]
                start_time = schedule_data[3]
                str_time = self.time.conversion(c_time=start_time, type_str=False)
                var_finish = tkinter.IntVar(value=finish)
                tkinter.Checkbutton(frame, text=str(schedule_id)+" || "+str_time+" "+all_schedule, font=("Arial", 11), variable=var_finish, onvalue=1, offvalue=0, command=lambda sid=schedule_id, v=var_finish: self.__update_schedule_state(v.get(), sid)).pack(side="top", padx=10, pady=5, anchor="w")
            # 更新滚动区域
            self.update_scrollregion(canvas)

    def menu(self):
        """菜单栏"""
        menu_main = tkinter.Menu(self.window_main, tearoff=0)  # 菜单栏
        menu_page = tkinter.Menu(menu_main, tearoff=0)   # 一级菜单栏:页面
        menu_function = tkinter.Menu(menu_main, tearoff=0)  # 一级菜单栏:新建
        menu_setting = tkinter.Menu(menu_main, tearoff=0)  # 一级菜单栏:设置

        # 一级菜单
        menu_main.add_cascade(label="页面", menu=menu_page)
        menu_main.add_cascade(label="功能", menu=menu_function)
        menu_main.add_cascade(label="设置", menu=menu_setting)
        # 若不想有下拉菜单，直接使用.add_command就可以直接执行命令
        menu_main.add_command(label="关于", command=lambda: self.__show_frame(self.about_frame))

        # 页面:二级菜单
        menu_page.add_cascade(label="主页", command=lambda: self.__show_frame(self.home_frame))
        menu_page.add_cascade(label="日程", command=lambda: self.__show_frame(self.schedule_frame))
        menu_page.add_cascade(label="设置", command=lambda: self.__show_frame(self.setting_frame))
        menu_page.add_cascade(label="关于", command=lambda: self.__show_frame(self.about_frame))

        # 新建:二级菜单
        menu_function.add_cascade(label="新建日程", command=lambda: self.B_window.new_schedule_window(self.window_main))
        menu_function.add_cascade(label="查询日程", command=lambda: self.B_window.select_schedule_window(self.window_main))
        menu_function.add_cascade(label="删除日程", command=lambda: self.B_window.delete_schedule_window(self.window_main))
        menu_function.add_cascade(label="更改日程", command=lambda: self.B_window.update_schedule_window(self.window_main))

        # 设置:二级菜单
        menu_setting.add_cascade(label="清理日志", command=lambda: self.__delete_log_data())
        menu_setting.add_cascade(label="清空数据", command=lambda: self.__delete_data())

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
        # 新建日程
        new_schedule_button = tkinter.Button(self.home_frame, text="新建", command=lambda: self.B_window.new_schedule_window(window_main=self.window_main))
        new_schedule_button.place(relx=0.25, rely=0.18, relwidth=0.1, relheight=0.07)
        # 查询日程
        select_schedule_button = tkinter.Button(self.home_frame, text="查询", command=lambda: self.B_window.select_schedule_window(window_main=self.window_main))
        select_schedule_button.place(relx=0.35, rely=0.18, relwidth=0.1, relheight=0.07)
        # 删除日程
        delete_schedule_button = tkinter.Button(self.home_frame, text="删除", command=lambda: self.B_window.delete_schedule_window(self.window_main))
        delete_schedule_button.place(relx=0.45, rely=0.18, relwidth=0.1, relheight=0.07)
        # 更改日程
        update_schedule_button = tkinter.Button(self.home_frame, text="更改", command=lambda: self.B_window.update_schedule_window(self.window_main))
        update_schedule_button.place(relx=0.55, rely=0.18, relwidth=0.1, relheight=0.07)
        # 统计
        count_completed = tkinter.Label(self.home_frame, text="已完成:{}".format(0))
        count_not_completed = tkinter.Label(self.home_frame, text="未完成:{}".format(0))
        count_completed.place(relx=0.25, rely=0.8505, relwidth=0.2, relheight=0.07)
        count_not_completed.place(relx=0.455, rely=0.8505, relwidth=0.2, relheight=0.07)
        # 更新统计
        self.__count_finish(count_completed, count_not_completed)
        # 今日日程框架
        today_schedule_frame = tkinter.Frame(self.home_frame, background="#FFFFFF")
        today_schedule_frame.place(relx=0.25, rely=0.25, relwidth=0.7, relheight=0.6)
        # 创建画布
        self.canvas = tkinter.Canvas(today_schedule_frame, background="#FFFFFF")
        # 创建滚动条
        self.scrollbar = tkinter.Scrollbar(today_schedule_frame, width=25)
        # 画布与滚动条相互绑定
        self.canvas.configure(yscrollcommand=self.scrollbar.set)  # 当视图移动时，移动滚动条
        self.scrollbar.config(command=self.canvas.yview)  # 当滚动条移动时，移动视图
        # 内容框架
        inner_frame = tkinter.Frame(self.canvas, background="#FFFFFF", width=int(self.local_window_size[0] * 0.7))
        # 画布窗口
        self.canvas.create_window((0, 0), window=inner_frame, anchor=tkinter.NW)  # 第一个是画布窗口坐标起始点为画布的00点，第二个是窗口中放个框架，第三个是组件布局起始点，左上角开始
        # 布局画布与滚动条
        self.canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
        self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        # 日程信息显示
        self.__update_schedule(inner_frame)
        # 刷新按钮
        update_button = tkinter.Button(self.home_frame, text="刷新", command=lambda: self.__update_schedule(inner_frame))
        update_button.place(relx=0.85, rely=0.28, relwidth=0.06, relheight=0.06)
        # 绑定鼠标滚轮事件
        self.canvas.bind("<MouseWheel>", lambda event: self.on_mouse_wheel(event, self.canvas))
        # 提示
        tkinter.Label(self.home_frame, text="tip:若日程过长且要使用滚轮进行上下滑动日程，那么就需要将鼠标放到滚动条上...", foreground="red").place(relx=0.34, rely=0.935)
        # 自动更新日程
        self.__auto_update_schedule(inner_frame, count_completed, count_not_completed)
        return self.home_frame

    def schedule(self):
        """日程"""
        self.schedule_frame = tkinter.Frame(self.main_frame, background="#00BFFF")

        # "全部日程"标签
        label = tkinter.Label(self.schedule_frame, text="所有日程详细信息", font=("Arial", 11))
        label.place(relx=0.35, rely=0.05, relwidth=0.5, relheight=0.1)
        # 新建日程
        new_schedule_button = tkinter.Button(self.schedule_frame, text="新建",
                                             command=lambda: self.B_window.new_schedule_window(
                                                 window_main=self.window_main))
        new_schedule_button.place(relx=0.25, rely=0.19, relwidth=0.1, relheight=0.07)
        # 查询日程
        select_schedule_button = tkinter.Button(self.schedule_frame, text="查询",
                                                command=lambda: self.B_window.select_schedule_window(
                                                    window_main=self.window_main))
        select_schedule_button.place(relx=0.35, rely=0.19, relwidth=0.1, relheight=0.07)
        # 删除日程
        delete_schedule_button = tkinter.Button(self.schedule_frame, text="删除",
                                                command=lambda: self.B_window.delete_schedule_window(self.window_main))
        delete_schedule_button.place(relx=0.45, rely=0.19, relwidth=0.1, relheight=0.07)
        # 更改日程
        update_schedule_button = tkinter.Button(self.schedule_frame, text="更改",
                                                command=lambda: self.B_window.update_schedule_window(self.window_main))
        update_schedule_button.place(relx=0.55, rely=0.19, relwidth=0.1, relheight=0.07)
        # 日程显示框架
        show_schedule_frame = tkinter.Frame(self.schedule_frame, background="#FFFFFF")
        show_schedule_frame.place(relx=0.25, rely=0.26, relwidth=0.7, relheight=0.65)
        # 创建画布
        self.schedule_canvas = tkinter.Canvas(show_schedule_frame, background="#FFFFFF")
        self.schedule_canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
        # 创建滚动条
        self.schedule_scrollbar = tkinter.Scrollbar(show_schedule_frame, width=25)
        self.schedule_scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        # 内容框架
        schedule_inner_frame = tkinter.Frame(self.schedule_canvas, background="#FFFFFF", width=int(self.local_window_size[0] * 0.7))
        # 画布窗口
        self.schedule_canvas.create_window((0, 0), window=schedule_inner_frame, anchor=tkinter.NW)
        # 画布滚动条绑定
        self.schedule_canvas.configure(yscrollcommand=self.schedule_scrollbar.set)
        self.schedule_scrollbar.config(command=self.schedule_canvas.yview)
        # 刷新按钮
        update_button = tkinter.Button(self.schedule_frame, text="刷新", command=lambda: self.select_all_schedule(self.schedule_canvas, schedule_inner_frame))
        update_button.place(relx=0.86, rely=0.2, relwidth=0.06, relheight=0.06)
        # 绑定滚轮
        self.schedule_canvas.bind("<MouseWheel>", lambda event: self.on_mouse_wheel(event, self.schedule_canvas))
        # 显示所有日程
        self.__auto_update_all_schedule(self.schedule_canvas, schedule_inner_frame)

        return self.schedule_frame

    def setting(self):
        """设置"""
        self.setting_frame = tkinter.Frame(self.main_frame, background="#00BFFF")

        # "设置界面"标签
        label = tkinter.Label(self.setting_frame, text="设置界面", font=("Arial", 11))
        label.place(relx=0.35, rely=0.05, relwidth=0.5, relheight=0.1)

        # 程序设置
        tkinter.Label(self.setting_frame, text="程序设置", font=("Arial", 11)).place(relx=0.25, rely=0.2, relwidth=0.1, relheight=0.07)
        program_setting_frame = tkinter.Frame(self.setting_frame, background="#FFFFFF")
        program_setting_frame.place(relx=0.25, rely=0.27, relwidth=0.7, relheight=0.25)
        # 删除数据
        reset_data = tkinter.Button(program_setting_frame, text="清空数据", font=("Arial", 11), command=lambda: self.__delete_data())
        reset_data.place(relx=0.025, rely=0.1, relwidth=0.15, relheight=0.25)
        # 删除日志数据
        reset_log = tkinter.Button(program_setting_frame, text="清空日志", font=("Arial", 11), command=lambda: self.__delete_log_data())
        reset_log.place(relx=0.2, rely=0.1, relwidth=0.15, relheight=0.25)

        return self.setting_frame

    def about(self):
        """关于"""
        self.about_frame = tkinter.Frame(self.main_frame, background="#00BFFF")

        # "关于界面"标签
        label = tkinter.Label(self.about_frame, text="关于界面", font=("Arial", 11))
        label.place(relx=0.35, rely=0.05, relwidth=0.5, relheight=0.1)

        # 内容
        text = ("作者：2021",
                "程序版本：{}".format(self.version.read_version()),
                "完成时间：2025-12-13",
                "Githup学习仓库地址：\"https://github.com/2021ya/Study\"",
                "自学讨论企鹅群：1062127934",
                "目的：python基础、SQLite基础、Tkinter基础和其他基本库等的综合应用",
                "日志文件路径(可定期删除)：\"./data/log/log.txt\"",
                "数据库文件(重置程序可删除)：\"./data/databases/data.db\"")
        list_box = tkinter.Listbox(self.about_frame, font=("黑体", 12))
        list_box.place(relx=0.25, rely=0.2, relwidth=0.7, relheight=0.7)
        for info in text:
            list_box.insert(tkinter.END, info)

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
        # C级窗口初始化
        self.c_window = UIC()

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

    def __schedule_save(self, schedule, year, month, day, hour, minute, second, save_or_update=True, schedule_id=""):
        """传入日程以及年月日时分秒数据，保存到数据库中;传入日程以及年月日时分秒数据、False、日程id，更新数据"""
        if schedule == "":  # 空日程判断
            self.pop_up.information("日程不可为空！")
            return
        if not (year.isdigit() and month.isdigit() and day.isdigit() and hour.isdigit() and minute.isdigit() and second.isdigit()):  # 时间是否为数字判断
            self.pop_up.information("日程时间格式错误！")
            return
        if " " in schedule:  # 日程中是否有空格
            self.pop_up.information("日程中不可包含空格！")
            return
        if save_or_update is False:  # 如果是False，就为更新
            if schedule_id == "":  # 判断日程id是否为空
                self.pop_up.information("日程id未填写！")
                return
            if not schedule_id.isdigit():
                self.pop_up.information("日程id错误，请检查输入！")
                return
        time = year + "-" + month + "-" + day + " " + hour + ":" + minute + ":" + second
        enter_save = self.pop_up.ask("确认保存吗？")
        if enter_save is True:
            try:
                if save_or_update:  # 保存数据
                    run = self.database.insert_data("||：" + schedule, self.time.conversion(time))
                    if run == "Insert data success!":
                        self.pop_up.information("数据保存成功")
                    else:
                        self.pop_up.error("数据保存失败:{}".format(run))
                    self.__close()
                elif not save_or_update:  # 更新数据
                    run = self.database.update_schedule("||：" + schedule, self.time.conversion(time), schedule_id)
                    if run == "Update schedule success!":
                        self.pop_up.information("日程[id={}]更新成功！".format(schedule_id))
                        self.__close()
                    else:
                        self.pop_up.error("日程[id={}]更新失败！[Error:{}]".format(schedule_id, run))
                        self.__close()
            except Exception as e:
                self.pop_up.error("时间戳转换失败，请注意您输入的日期是否合法！[Error:{}]".format(e))
        else:
            pass

    def __select_enter(self, window_b, year, month, day, hour, minute, second, year2, month2, day2, hour2, minute2, second2):
        """合并时间字符串并调用函数展示查询结果"""
        if not (year.isdigit() and month.isdigit() and day.isdigit() and hour.isdigit() and minute.isdigit() and second.isdigit() and year2.isdigit() and month2.isdigit() and day2.isdigit() and hour2.isdigit() and minute2.isdigit() and second2.isdigit()):  # 时间是否为数字判断
            self.pop_up.information("日程时间格式错误！")
            return
        start_time = year + "-" + month + "-" + day + " " + hour + ":" + minute + ":" + second
        end_time = year2 + "-" + month2 + "-" + day2 + " " + hour2 + ":" + minute2 + ":" + second2
        try:
            start_time_timestamp = self.time.conversion(start_time)
            end_time_timestamp = self.time.conversion(end_time)
            if start_time_timestamp > end_time_timestamp:
                self.pop_up.error("开始时间不可大于结束时间！")
                return
        except Exception as e:
            self.pop_up.error("时间戳转换失败，请检查输入的时间是否正确！[Error:{}]".format(e))
            return
        self.c_window.show_select_schedule_window(window_b, start_time_timestamp, end_time_timestamp)

    def __delete_schedule(self, schedule_id):
        """输入日程id，删除日程"""
        if schedule_id.isdigit():
            if self.pop_up.ask("确认删除此日程吗？"):
                delete_schedule = self.database.delete_schedule(int(schedule_id))
                if delete_schedule == "Delete schedule success!":
                    self.pop_up.information("删除日程[id={}]成功！".format(schedule_id))
                    self.__close()
                else:
                    self.pop_up.error(delete_schedule)
            else:
                pass
        else:
            self.pop_up.information("日程id错误，请检查日程id是否正确！")

    def __time_enter_frame(self, window):
        """时间输入框架"""
        # 总框架
        time_enter_frame = tkinter.Frame(window)
        # 变量创建
        year = tkinter.StringVar()
        month = tkinter.StringVar()
        day = tkinter.StringVar()
        hour = tkinter.StringVar()
        minute = tkinter.StringVar()
        second = tkinter.StringVar()
        # 时间输入框架
        time_choose_year_label = tkinter.Label(time_enter_frame, text="年", font=("Arial", 13))  # 年标签
        time_choose_year_label.place(relx=0.14, rely=0.3, relwidth=0.06, relheight=0.23)
        time_choose_year_enter = tkinter.Entry(time_enter_frame, font=("Arial", 13), textvariable=year)  # 年输入框
        year.set(self.time.time_localtime(1))
        time_choose_year_enter.place(relx=0.03, rely=0.3, relwidth=0.11, relheight=0.23)
        time_choose_month_label = tkinter.Label(time_enter_frame, text="月", font=("Arial", 13))  # 月标签
        time_choose_month_label.place(relx=0.29, rely=0.3, relwidth=0.06, relheight=0.23)
        time_choose_month_enter = tkinter.Entry(time_enter_frame, font=("Arial", 13), textvariable=month)  # 月输入框
        month.set(self.time.time_localtime(2))
        time_choose_month_enter.place(relx=0.2, rely=0.3, relwidth=0.09, relheight=0.23)
        time_choose_day_label = tkinter.Label(time_enter_frame, text="日", font=("Arial", 13))  # 日标签
        time_choose_day_label.place(relx=0.44, rely=0.3, relwidth=0.06, relheight=0.23)
        time_choose_day_enter = tkinter.Entry(time_enter_frame, font=("Arial", 13), textvariable=day)  # 日输入框
        day.set(self.time.time_localtime(3))
        time_choose_day_enter.place(relx=0.35, rely=0.3, relwidth=0.09, relheight=0.23)
        time_choose_hour_label = tkinter.Label(time_enter_frame, text="时", font=("Arial", 13))  # 时标签
        time_choose_hour_label.place(relx=0.59, rely=0.3, relwidth=0.06, relheight=0.23)
        time_choose_hour_enter = tkinter.Entry(time_enter_frame, font=("Arial", 13), textvariable=hour)  # 时输入框
        hour.set(self.time.time_localtime(4))
        time_choose_hour_enter.place(relx=0.5, rely=0.3, relwidth=0.09, relheight=0.23)
        time_choose_minute_label = tkinter.Label(time_enter_frame, text="分", font=("Arial", 13))  # 分标签
        time_choose_minute_label.place(relx=0.74, rely=0.3, relwidth=0.06, relheight=0.23)
        time_choose_minute_enter = tkinter.Entry(time_enter_frame, font=("Arial", 13), textvariable=minute)  # 分输入框
        minute.set("00")
        time_choose_minute_enter.place(relx=0.65, rely=0.3, relwidth=0.09, relheight=0.23)
        time_choose_second_label = tkinter.Label(time_enter_frame, text="秒", font=("Arial", 13))  # 秒标签
        time_choose_second_label.place(relx=0.89, rely=0.3, relwidth=0.06, relheight=0.23)
        time_choose_second_enter = tkinter.Entry(time_enter_frame, font=("Arial", 13), textvariable=second)  # 秒输入框
        second.set("00")
        time_choose_second_enter.place(relx=0.8, rely=0.3, relwidth=0.09, relheight=0.23)
        return time_enter_frame, year, month, day, hour, minute, second  # TODO: BUG(在创建时间框架的时候直接获取了时间，无法获取用户输入的时间了)

    def new_schedule_window(self, window_main):
        """新建日程窗口"""
        if self.__window_check() is False:  # B级窗口占用检测
            self.__init_ui(window_main=window_main)  # 初始化B级窗口
            # 窗口设为为Ture-占用
            self.check_window_B = True
            # 日程标签
            schedule_label = tkinter.Label(self.window_b, text="日程信息", font=("Arial", 13))
            schedule_label.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.1)
            # 输入框变量创建
            schedule = tkinter.StringVar()
            # 输入框
            schedule_enter = tkinter.Entry(self.window_b, font=("Arial", 11), textvariable=schedule)
            schedule_enter.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.15)
            # 时间标签
            time_label = tkinter.Label(self.window_b, text="提醒时间", font=("Arial", 13))
            time_label.place(relx=0.1, rely=0.355, relwidth=0.2, relheight=0.1)
            # 时间输入
            time_enter = self.__time_enter_frame(self.window_b)
            time_enter[0].place(relx=0.1, rely=0.455, relwidth=0.8, relheight=0.3)
            # 保存按钮
            save_button = tkinter.Button(self.window_b, text="保存", command=lambda: self.__schedule_save(schedule.get(), time_enter[1].get(), time_enter[2].get(), time_enter[3].get(), time_enter[4].get(), time_enter[5].get(), time_enter[6].get()))
            save_button.place(relx=0.75, rely=0.8, relwidth=0.17, relheight=0.12)

        elif self.check_window_B is True:
            return

    def delete_schedule_window(self, window_main):
        """删除日程窗口"""
        if self.__window_check() is False:  # B级窗口占用检测
            self.__init_ui(window_main=window_main)  # 初始化B级窗口
            # 窗口设为为Ture-占用
            self.check_window_B = True
            # 日程id变量
            schedule_id = tkinter.StringVar()
            # "需要删除的日程id"标签
            tkinter.Label(self.window_b, text="需要删除的日程id：", font=("Arial", 13)).place(relx=0.25, rely=0.4, relwidth=0.3, relheight=0.125)
            # 日程id输入框
            tkinter.Entry(self.window_b, textvariable=schedule_id).place(relx=0.55, rely=0.4, relwidth=0.2, relheight=0.125)
            # 确认按钮
            tkinter.Button(self.window_b, text="确认", command=lambda: self.__delete_schedule(schedule_id.get())).place(relx=0.75, rely=0.8, relwidth=0.15, relheight=0.1)
        elif self.check_window_B is True:
            return

    def update_schedule_window(self, window_main):
        """更新日程窗口"""
        if self.__window_check() is False:  # B级窗口占用检测
            self.__init_ui(window_main=window_main)  # 初始化B级窗口
            # 窗口设为为Ture-占用
            self.check_window_B = True
            # 日程id变量创建
            schedule_id = tkinter.StringVar()
            # 日程id
            schedule_id_label = tkinter.Label(self.window_b, text="需要更改日程的id：", font=("Arial", 13))
            schedule_id_label.place(relx=0.5, rely=0.05, relwidth=0.3, relheight=0.07)
            schedule_id_enter = tkinter.Entry(self.window_b, font=("Arial", 13), textvariable=schedule_id)
            schedule_id_enter.place(relx=0.8, rely=0.05, relwidth=0.1, relheight=0.07)
            # 新日程标签
            new_schedule_label = tkinter.Label(self.window_b, text="新日程信息", font=("Arial", 13))
            new_schedule_label.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.1)
            # 新输入框变量创建
            new_schedule = tkinter.StringVar()
            # 新日程输入框
            new_schedule_enter = tkinter.Entry(self.window_b, font=("Arial", 11), textvariable=new_schedule)
            new_schedule_enter.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.15)
            # "新提醒时间"标签
            tkinter.Label(self.window_b, text="新提醒时间", font=("Arial", 13)).place(relx=0.1, rely=0.355, relwidth=0.2, relheight=0.1)
            # 时间输入框
            time_enter = self.__time_enter_frame(self.window_b)
            time_enter[0].place(relx=0.1, rely=0.455, relwidth=0.8, relheight=0.3)
            # 保存按钮
            save_button = tkinter.Button(self.window_b, text="保存", command=lambda: self.__schedule_save(new_schedule.get(), time_enter[1].get(), time_enter[2].get(), time_enter[3].get(), time_enter[4].get(), time_enter[5].get(), time_enter[6].get(), False, schedule_id.get()))
            save_button.place(relx=0.75, rely=0.8, relwidth=0.17, relheight=0.12)
        elif self.check_window_B is True:
            return

    def select_schedule_window(self, window_main):
        """查询窗口"""
        if self.__window_check() is False:  # B级窗口占用检测
            self.__init_ui(window_main=window_main)  # 初始化B级窗口
            # 窗口设为为Ture-占用
            self.check_window_B = True
            # 创建时间输入框架
            start_time = self.__time_enter_frame(self.window_b)
            end_time = self.__time_enter_frame(self.window_b)
            start_time[0].place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.3)
            end_time[0].place(relx=0.1, rely=0.55, relwidth=0.8, relheight=0.3)
            # 标签
            tkinter.Label(self.window_b, text="开始时间", font=("Arial", 13)).place(relx=0.1, rely=0.05, relwidth=0.2, relheight=0.1)
            tkinter.Label(self.window_b, text="结束时间", font=("Arial", 13)).place(relx=0.1, rely=0.455, relwidth=0.2, relheight=0.1)
            # 确认按钮
            tkinter.Button(self.window_b, text="确认", command=lambda: self.__select_enter(self.window_b, start_time[1].get(), start_time[2].get(), start_time[3].get(), start_time[4].get(), start_time[5].get(), start_time[6].get(), end_time[1].get(), end_time[2].get(), end_time[3].get(), end_time[4].get(), end_time[5].get(), end_time[6].get())).place(relx=0.8, rely=0.86, relwidth=0.15, relheight=0.1)
        elif self.check_window_B is True:
            return


class UIC(object):
    """C级窗口，三级窗口"""
    def __init__(self):
        # 窗口检测-只允许一个C级窗口出现
        self.check_window_C = False
        # 时间初始化
        self.time_label = None
        # 工具初始化
        self.time = logic.Time()
        self.pop_up = PopUp()
        # ui初始化默认设置
        self.window_c = None
        self.local_window_size = None
        # 数据库初始化
        self.database = logic.Database()
        # 画布与滚动条初始化
        self.canvas = None
        self.scrollbar = None

    def __init_ui(self, window_b):
        """UIC初始化"""
        self.window_c = tkinter.Toplevel(window_b)  # 创建B级窗口
        self.window_c.title('SMT Tool @2021-C级窗口')  # 设置标题
        self.window_c.iconbitmap(r"./resources/images/icon.ico")  # 程序窗口图标
        self.local_window_size = self.window_c.maxsize()  # 获取主机显示器大小
        self.window_c.geometry(
            "{}x{}+{}+{}".format(int(self.local_window_size[0] / 3), int(self.local_window_size[1] / 3),
                                 int(self.local_window_size[0] / 3), int(self.local_window_size[1] / 3)))  # 按比例缩放程序大小
        self.window_c.configure(background="#00BFFF")  # 设置背景色
        self.window_c.resizable(False, False)  # 禁止自由缩放窗口大小
        self.window_c.transient(window_b)  # 使得子窗口始终在父窗口之上
        self.window_c.grab_set()  # 模态对话框，锁定与父窗口交互
        # 自定义退出
        self.window_c.protocol("WM_DELETE_WINDOW", self.__close)

    def __window_check(self):
        """窗口检查，只允许一个C级窗口出现"""
        if self.check_window_C is True:
            self.pop_up.warning("已存在一个C级窗口，请先关闭当前C级窗口后再执行此操作！")
            return True
        else:
            return False

    def __close(self):
        """窗口关闭时执行"""
        self.check_window_C = False  # 窗口设为为False-未占用
        self.window_c.grab_release()  # 释放锁定
        self.window_c.destroy()

    def __auto_update_show_select_window(self, data, inner_frame):
        """自动更新查询日程窗口"""
        self.__update_show_select_window(data, inner_frame)
        self.window_c.after(3000, lambda: self.__auto_update_show_select_window(data, inner_frame))
        # 这里如果不使用lambda函数的话data和inner_frame两个参数就访问不到了，因为这两个参数局局部变量，等自动执行时，就需要重新传入参数了

    def __update_show_select_window(self, data, inner_frame):
        """更新查询日程窗口"""
        # 销毁旧组件
        for i in inner_frame.winfo_children():
            i.destroy()
        # 重新布局新组件
        row = 1
        if not data:
            frame = tkinter.Frame(inner_frame)
            tkinter.Label(frame, text="暂无数据", font=("Arial", 13)).pack(fill="x")
            frame.pack(fill=tkinter.BOTH, padx=175, pady=30)
        else:
            frame = tkinter.Frame(inner_frame)
            tkinter.Label(frame, text="日程:", font=("Arial", 13)).pack(side="left", fill="x")
            frame.pack(fill=tkinter.BOTH, padx=20, pady=30)
            for i in data:
                row += 1
                tkinter.Label(frame, text=i, font=("Arial", 11)).pack(side="top", padx=10, pady=5, anchor="w")
        # 更新滚动区域
        UI.update_scrollregion(self.canvas)

    def show_select_schedule_window(self, window_b, start_time_timestamp, end_time_timestamp):
        """展示查询窗口"""
        if self.__window_check() is False:  # C级窗口占用检测
            self.__init_ui(window_b=window_b)  # 初始化C级窗口
            # 窗口设为为Ture-占用
            self.check_window_C = True
            # "查找指定日程"标签
            tkinter.Label(self.window_c, text="查找指定时间段日程", font=("Arial", 13)).place(relx=0.35, rely=0.07, relwidth=0.3, relheight=0.1)
            # 日程显示框架
            show_select_frame = tkinter.Frame(self.window_c, background="#FFFFFF")
            show_select_frame.place(relx=0.145, rely=0.2, relwidth=0.745, relheight=0.7)
            # 创建画布
            self.canvas = tkinter.Canvas(show_select_frame, background="#FFFFFF")
            # 创建滚动条
            self.scrollbar = tkinter.Scrollbar(show_select_frame, width=25)
            # 画布与滚动条相互绑定
            self.canvas.configure(yscrollcommand=self.scrollbar.set)  # 当视图移动时，移动滚动条
            self.scrollbar.config(command=self.canvas.yview)  # 当滚动条移动时，移动视图
            # 内容框架
            inner_frame = tkinter.Frame(self.canvas, background="#FFFFFF", width=int(self.local_window_size[0] * 0.71))
            # 画布窗口
            self.canvas.create_window((0, 0), window=inner_frame, anchor=tkinter.NW)  # 第一个是画布窗口坐标起始点为画布的00点，第二个是窗口中放个框架，第三个是组件布局起始点，左上角开始
            # 布局画布与滚动条
            self.canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
            self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
            data = self.database.select_schedule(start_time_timestamp, end_time_timestamp)
            # 滚轮绑定
            self.canvas.bind("<MouseWheel>", lambda event: UI.on_mouse_wheel(event, self.canvas))
            # 展示查询-自动更新
            self.__auto_update_show_select_window(data, inner_frame)
            # 手动刷新按钮
            tkinter.Button(self.window_c, text="刷新", command=lambda: self.__auto_update_show_select_window(data, inner_frame)).place(relx=0.74, rely=0.1, relwidth=0.15, relheight=0.1)
        elif self.check_window_C is True:
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

