import tkinter
from tkinter import messagebox  # 若你想创建弹窗组件，必须单独导入此包
from tkinter.ttk import Combobox  # 下拉菜单的包，这个包需要导入，你也可以直接导入ttk包
from tkinter import END  # 导入列表追加元素

# 创建窗口
window = tkinter.Tk()

# 获取当前屏幕分辨率
localhost_window = window.maxsize()

# 设置窗口标题
window.title("测试窗口")

# 设置窗口图标
window.iconbitmap(r"./images/256x256.ico")

# 调整窗口颜色
window.configure(background="#00BFFF")

# 调整窗口大小
window.geometry(
    "{}x{}+{}+{}".format(int(localhost_window[0] / 2), int(localhost_window[1] / 2), int(localhost_window[0] / 4),
                         int(localhost_window[1] / 4)))

# 禁止更改窗口大小-False禁止|Ture-允许（默认）
window.resizable(False, False)

# 置顶窗口
window.attributes("-topmost", True)

# 窗口标签
account = tkinter.Label(window, text="Account:", font=("黑体", 24), foreground="#000000", background="#FFFFFF")
password = tkinter.Label(window, text="Password:", font=("黑体", 24), foreground="#000000", background="#FFFFFF")

# 布局标签
account.place(x=100, y=100, width=150, height=50)
password.place(x=100, y=160, width=150, height=50)

# 创建字符串变量-用于接受输入框组件的输入
account_text = tkinter.StringVar()  # 实例化记得加括号
account_text.set("提示文本account：")  # .set方法类似于提示文本，预设
password_text = tkinter.StringVar()
password_text.set("提示文本password：")

# 输入框组件
enter_account = tkinter.Entry(window, textvariable=account_text, font=("黑体", 24))
enter_password = tkinter.Entry(window, textvariable=password_text, font=("黑体", 24))

# 布局输入框
enter_account.place(x=270, y=100, width=350, height=50)
enter_password.place(x=270, y=160, width=350, height=50)


# 按钮组件
def login():
    print("你点了登录按钮")
    print(account_text.get())  # get()函数可以获取字符串变量里面传输的值
    print(password_text.get())
    if account_text.get() != "123" or password_text.get() != "123":
        messagebox.showerror(title="Error", message="错误弹窗")  # .showerror()为错误弹窗
        messagebox.showinfo(title="info", message="信息弹窗")  # .showinfo()为信息弹窗
        messagebox.showwarning(title="warning", message="警告弹窗")  # .showwarning()为警告弹窗
        pop_up = messagebox.askyesno(title="yes/no", message="询问弹窗")  # .askyesno为询问弹窗
        messagebox.askokcancel(title="cancel?", message="确认取消弹窗")  # .askokcancel为确认取消弹窗
        messagebox.askquestion(title="question", message="问题弹窗")  # .askquestion为问题弹窗
        messagebox.askretrycancel(title="retrycancel", message="重试弹窗")  # .askretrycancel为重试弹窗
        messagebox.askyesnocancel(title="yesnocancel", message="是/否/取消弹窗")  # .askyesnocancel为"是/否/取消弹窗"
        # 以上选项弹窗均可以用Ture和False来判断，前提是用变量接收
        if pop_up:
            print("点了确定")
        elif not pop_up:
            print("点了取消")
    else:
        messagebox.showinfo(title="info", message="嗯")  # .showinfo()为信息弹窗


login_button = tkinter.Button(window, command=login, text="Login",
                              font=("黑体", 24))  # command是点击按钮之后所执行的函数；注意，传参的时候不用加括号了

# 布局按钮
login_button.place(x=150, y=320, width=130, height=50)


# 关闭函数
def close():
    pop_up = messagebox.askyesno(title="确认关闭", message="你真的真的真的要关闭吗！")
    if pop_up:
        messagebox.showinfo(title="吐槽", message="知道了，这就关，哎")
        window.quit()
        print("关了")
    if not pop_up:
        messagebox.showinfo(title="欣慰", message="我就知道，你不会关的，哈哈哈")
        pass


window.protocol("WM_DELETE_WINDOW", close)  # 使用.protocol来自定义关闭参数，第一个是固定参数，第二个是当关闭程序时所执行的函数


# 顶层窗口----窗口之中还有窗口


def register():
    window_1_1 = tkinter.Toplevel()  # 创建顶层窗口使用.Toplevel()函数
    window_1_1.title("顶层窗口")
    window_1_1.attributes("-topmost", True)
    window_1_1.iconbitmap(r"./images/256x256.ico")
    window_1_1.configure(background="#00BFFF")
    window_1_1.geometry("{}x{}+{}+{}".format(int((localhost_window[0] / 2) / 2), int((localhost_window[1] / 2) / 2),
                                             int((localhost_window[0] / 4) / 2), int((localhost_window[1] / 4 / 2))))
    window_1_1.resizable(False, False)
    # window_1_1.mainloop()  # 这是bug，会进入多层嵌套，所有窗口都是共享主窗口的事件循环的
    register_account_label = tkinter.Label(window_1_1, text="Account：", font=("黑体", 24), width=10, height=1,
                                           background="#00BFFF")
    register_password_label = tkinter.Label(window_1_1, text="Password：", font=("黑体", 24), width=10, height=1,
                                            background="#00BFFF")
    register_account_label.grid(row=1, column=1)
    register_password_label.grid(row=2, column=1)
    enter_account_text = tkinter.StringVar()
    enter_password_text = tkinter.StringVar()
    enter_account_label = tkinter.Entry(window_1_1, textvariable=enter_account_text, width=20, background="#00BFFF")
    enter_password_text = tkinter.Entry(window_1_1, textvariable=enter_password_text, width=20,
                                        background="#00BFFF")  # 输入框特殊功能：只读state=readonly,禁用state=disabled
    enter_account_label.grid(row=1, column=2)
    enter_password_text.grid(row=2, column=2)
    enter_register = tkinter.Button(window_1_1, text="注册", width=10, height=2,
                                    command=close)  # 这里用close来替代注册完关闭注册窗口，因为需要访问其他函数，但是练习的时候没有写类，所以就先这样演示看吧
    enter_register.grid(row=3, column=1)


register_button = tkinter.Button(window, command=register, text="register",
                                 font=("黑体", 24))  # command是点击按钮之后所执行的函数；注意，传参的时候不用加括号了

register_button.place(x=350, y=320, width=130, height=50)

# 创建菜单与下级菜单
menu1 = tkinter.Menu(window, tearoff=0)  # 创建菜单,tearoff为撕开菜单，默认为1，调为0就没有了
menu1_1 = tkinter.Menu(menu1, tearoff=0)  # 创建菜单1，然后窗口显示到上级菜单中
menu1_1.add_cascade(label="员工下级菜单", command='')  # 总菜单1中的下级菜单
menu1.add_cascade(label="员工",
                  menu=menu1_1)  # 添加菜单，label设置菜单名称,其中menu中也是一个菜单，这样就构成了下级菜单, command为执行函数，此为第一种下级菜单方法， 总菜单1


# menu1.add_cascade(label="员工")
# menu1.add_cascade(menu=menu1_1)  # 下级菜单第二种方法
# menu1.add_cascade(label="管理")  # 添加菜单，label设置菜单名称


# 下拉菜单
def combo():
    window_1_1_1 = tkinter.Toplevel()
    window_1_1_1.title("下拉菜单")
    window_1_1_1.attributes("-topmost", True)
    window_1_1_1.iconbitmap(r"./images/256x256.ico")
    window_1_1_1.configure(background="#00BFFF")
    window_1_1_1.geometry("{}x{}+{}+{}".format(int((localhost_window[0] / 2) / 2), int((localhost_window[1] / 2) / 2),
                                               int((localhost_window[0] / 4) / 2), int((localhost_window[1] / 4 / 2))))

    window_1_1_1.focus_set()  # 设置窗口焦点
    window_1_1_1.resizable(False, False)
    label_city = tkinter.Label(window_1_1_1, text="城市", font=("黑体", 24))  # 创建标签的时候记得要写在哪个重开创建
    label_city.place(x=50, y=30, width=100, height=45)
    choose = tkinter.StringVar()  # 创建字符串变量用于接受下拉菜单的选择
    list1 = ["山西", "北京", "上海", "武汉"]
    combo_1 = Combobox(window_1_1_1, state="readonly", textvariable=choose, values=list1,
                       font=("黑体", 24))  # 下拉菜单第一个为窗口，第二个为接受变量，第三个为值, 为了避免自己输入，这时候就设置了禁止修改了
    combo_1.current(0)  # 设置下拉列表的默认索引值
    combo_1.place(x=50, y=100, width=100, height=45)
    radiobutton_man = tkinter.StringVar(value="男")  # 设置默认值为男
    radiobutton_man_1 = tkinter.Radiobutton(window_1_1_1, text="男", font=("黑体", 24), variable=radiobutton_man, value="男")  # 第一个为窗口，第二个为文本，第三个是接受值的变量（可以直接将value传入到variable），第四个是变量
    radiobutton_man_2 = tkinter.Radiobutton(window_1_1_1, text="女", font=("黑体", 24), variable=radiobutton_man, value="女")  # 第一个为窗口，第二个为文本，第三个是接受值的变量（可以直接将value传入到variable），第四个是变量,传到同一个地方的时候，两个单选只能选一个
    radiobutton_man_1.place(x=150, y=30, width=100, height=45)
    radiobutton_man_2.place(x=250, y=30, width=100, height=45)
    print("默认值：", radiobutton_man.get(), choose.get())

    # 创建多选框
    intvar1 = tkinter.IntVar()  # 创建整数变量, 接受整数类型的数据
    intvar2 = tkinter.IntVar()  # 创建整数变量, 接受整数类型的数据
    check1 = tkinter.Checkbutton(window_1_1_1, text="多选1", font=("黑体", 24), variable=intvar1, onvalue=1, offvalue=0)  # 第一个为窗体，第二个为显示文本，第三个为字体，第四个为绑定的变量，第五个是选择之后返回什么值，第六感是不选择返回什么值
    check2 = tkinter.Checkbutton(window_1_1_1, text="多选2", font=("黑体", 24), variable=intvar2, onvalue=1, offvalue=0)  # 第一个为窗体，第二个为显示文本，第三个为字体，第四个为绑定的变量，第五个是选择之后返回什么值，第六感是不选择返回什么值
    check1.place(x=50, y=200, width=100, height=45)
    check2.place(x=250, y=200, width=100, height=45)
    print("choose:", intvar1.get(), intvar2.get())

    # 创建列表框
    listbox1 = (tkinter.Listbox(window_1_1_1, font=("黑体", 24), width=10, height=10))
    listbox1.place(x=200, y=100, width=200, height=75)  # 不可以一边布局一边追加元素，分开写列表与布局，然后才能添加元素
    listbox1.insert(END, "132")  # 这里只能传字符串,第一个为固定，第二个为元素，使用insert来追加数据，提交一次一行数据

menu1_1_1 = tkinter.Menu(menu1, tearoff=0)  # 创建菜单2，每个菜单下的菜单都需要重新写一个菜单
menu1_1_1.add_cascade(label="添加2", command=combo)  # 总菜单2中的下级菜单
menu1.add_cascade(label="管理", menu=menu1_1_1)  # 总菜单2

window.config(menu=menu1)  # 加载菜单,加载由menu1创建的所有菜单
# 打开窗口-进入窗口循环
window.mainloop()
