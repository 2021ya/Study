import tkinter  # 导入tkinter(python自带基础库)


# 创建窗口对象
window = tkinter.Tk()  # 实例化根窗口类-----人话：造一个窗口


# -----窗口调整-----

# 设置窗口标题
window.title("这是窗口标题")

# 获取当前屏幕分辨率
size = window.maxsize()
print("当前电脑分辨率：", size)

# 设置窗口图标
window.iconbitmap(r"./images/256x256.ico")

# 设置窗口颜色
window.configure(background=r"#00BFFF")  # 可以传颜色英文，例如：red, blue；也可以放颜色编码，例如#000000，#111111

# 设置窗口透明度-.attributes()窗口属性调整
window.attributes("-alpha", 1)  # 第一个为固定的参数，第二个为透明度，值为0-1

# 设置窗口置顶-.attributes()窗口属性调整
window.attributes("-topmost", True)  # 第一个为固定参数，第二个Ture为置顶反之

# 设置窗口大小-（我发现这个调整大小如果不写到最后面的话窗口位置就变了）
# window.geometry("500x500+300+300")
window.geometry("%dx%d+%d+%d" % (int(size[0]/2), int(size[1]/2), int(size[0]/4), int(size[1]/4)))  # 自动调整程序窗口，因为有可能返回浮点数，但这四个参数都是整数，所以要转为整数
# 格式：.geometry("宽x高+距离左边框+距离上边框")  也可以为负数
"""
传入字符串（宽x高）像素，不可用*，这个是小写"埃克斯"="x"
电脑左上角坐标为(0.0),+300+300为从屏幕左从屏幕上300像素为起点打开此程序
若你真的闲的没事量了一下的话，如果不对的话请看一下你电脑屏幕的缩放比例
"""

# 禁止更改窗口大小-False禁止|Ture-允许（默认）
window.resizable(False, False)

# 关闭按钮的调整
window.protocol("WM_DELETE_WINDOW", window.quit())  # 第一个为固定参数，第二个为点击关闭按钮是所执行的函数,默认window.quit


# -----组件调整-----

# 创建一个标签
text_table = tkinter.Label(window, text="这是标签里面的文本", font=("黑体", 15), foreground="red", background="yellow")
# text_table2 = tkinter.Label(window, text="这是标签里面的文本", font=("黑体", 15), foreground="red", background="yellow")
"""
第一个是窗口（将这个标签显示到哪个窗口
第二个为文本text
第三个为字体font，这个是元组，里面第一个为字体，第二个为字号
foreground是调整字体颜色
background是调整背景颜色
"""

# 布局，相当于启动这个标签，与打开窗口类似
# text_table.pack()
text_table.place(x=50, y=50, width=50, height=50)
# text_table.grid(row=1, column=1, columnspan=1)
# text_table2.grid(row=1, column=3, columnspan=1)
"""
布局详解：
填充布局——pack
    相当于文本框类型，会有背景色,默认最上面居中
自定义布局——place
    输入坐标，自定义位置和大小
网格布局——grid
    row控制行，column控制列,columnspan列宽
"""

# 打开窗口
window.mainloop()  # 调用组件.mainloop()进入窗口主循环，这里要注意，开启窗口之后会进入窗口循环，组件什么的需要写到上面
"""
其他语句必须在创建窗口与开启窗口的中间才能生效
"""
