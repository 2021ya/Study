import tkinter


window = tkinter.Tk()

window.title("滚动条学习")
size = window.maxsize()
window.configure(background=r"#00BFFF")
window.attributes("-alpha", 1)
window.geometry("%dx%d+%d+%d" % (int(size[0]/2), int(size[1]/2), int(size[0]/4), int(size[1]/4)))
window.resizable(False, False)


# 画布组件
canvas = tkinter.Canvas(window, background="#FFFFFF", highlightthickness=0, takefocus=False)  # highlightthickness组件被选中时的边框厚度，takefocus：是否可以通过Tab键获得焦点。对于纯滚动区域通常设为False
"""
参数详解：
parent(第一个参数)：父容器，Canvas会放在这个容器里
background：Canvas的背景颜色
highlightthickness：组件被选中时的边框厚度。设为0让界面更干净
takefocus：是否可以通过Tab键获得焦点。对于纯滚动区域通常设为False
"""
# 滚动条组件
scrollbar = tkinter.Scrollbar(window, orient="vertical", command=canvas.yview)
"""
参数详解：
orient(第一个参数)：父容器
"vertical"：垂直滚动条
"horizontal"：水平滚动条
command：最重要的参数！当用户拖动滚动条时，会调用这个函数
canvas.yview：Canvas内置方法，控制垂直滚动
canvas.xview：控制水平滚动
"""
# 配置滚动条的滚动
canvas.configure(yscrollcommand=scrollbar.set)
"""
作用：
当Canvas的视图位置变化时，自动更新滚动条的位置
"""
# 滚动条与画布双向绑定
scrollbar.config(command=canvas.yview)  # 拖动滚动条时，移动画布
canvas.config(yscrollcommand=scrollbar.set)  # 滚动画布时，移动滚动条
# 画布内部框架
canvas_inner_frame = tkinter.Frame(window, background="#FFFFFF")
# 画布窗口
canvas_window = canvas.create_window((0, 0), window=canvas_inner_frame, anchor=tkinter.NW)
"""
create_window方法详解：
作用：在Canvas上创建一个"窗口"，可以放入任何Tkinter组件
参数：
(x, y)：窗口在Canvas中的坐标位置，(0, 0)表示左上角
window：要放入的组件（这里是inner_frame）
anchor：锚点，决定组件的哪个角对齐到指定位置
"nw"：西北角（左上角）
"n"：北边中点
"ne"：东北角（右上角）
"w"：西边中点
"center"：中心
"e"：东边中点
"sw"：西南角（左下角）
"s"：南边中点
"se"：东南角（右下角）
width、height：窗口的宽度和高度（可选）
tags：给这个窗口添加标签，便于后续查找操作
返回值：
canvas_window：一个整数ID，代表Canvas中这个"窗口"的唯一标识符
后续可以通过这个ID操作这个窗口
"""
# 布局画布和滚动条
scrollbar.pack(side="right", fill="y", expand=False)
canvas.pack(side="left", fill="both", expand=True)


def configure_scrollregion(event):
    """更新Canvas的滚动区域"""
    # 1. 获取内部框架的边界框
    bbox = canvas.bbox("all")
    # bbox格式: (x1, y1, x2, y2) - 左上角和右下角坐标
    # 2. 设置Canvas的滚动区域
    canvas.configure(scrollregion=bbox)
    # 3. 确保内部框架与Canvas同宽
    canvas.itemconfig(canvas_window, width=canvas.winfo_width())
    """
    什么是scrollregion？
    定义：Canvas中可滚动区域的边界
    格式：(x1, y1, x2, y2)，其中：
    (x1, y1)：可滚动区域的左上角
    (x2, y2)：可滚动区域的右下角
    作用：告诉Canvas"从(x1,y1)到(x2,y2)的区域是可滚动的"
    canvas.bbox("all") 详解：
    作用：获取Canvas中所有内容的边界框
    参数：
    "all"：获取所有项目的边界框
    也可以是特定标签或ID
    返回值：(x1, y1, x2, y2) 或 None（如果没有内容）
    为什么要更新宽度？
    python
    canvas.itemconfig(canvas_window, width=canvas.winfo_width())
    问题：当Canvas宽度变化时，内部框架宽度不会自动更新
    结果：内容可能被截断或留白
    解决：每次更新时，设置内部框架宽度等于Canvas当前宽度
    """


# # 当内部框架大小改变时，更新滚动区域
# canvas_inner_frame.bind("<Configure>", configure_scrollregion)
#
#
# def on_canvas_configure(event):
#     canvas.itemconfig(canvas_window, width=event.winfo_width())
#
# # 当Canvas大小改变时，调整内部框架宽度
# canvas.bind("<Configure>", on_canvas_configure)
"""
事件详解：
<Configure>事件：当组件大小或位置改变时触发
event对象属性：
event.width：新宽度
event.height：新高度
event.x、event.y：新位置
"""


def on_mouse_wheel(event):
    """处理鼠标滚轮事件"""
    # Windows/Mac: event.delta 表示滚动的"距离"
    # Linux: 使用event.num（4=向上，5=向下）

    # 向上滚动
    if event.delta > 0:
        canvas.yview_scroll(-1, "units")  # 向上移动1个单位
        print("1")
    # 向下滚动
    elif event.delta < 0:
        canvas.yview_scroll(1, "units")  # 向下移动1个单位
        print("2")


# 绑定滚轮事件
canvas.bind_all("<MouseWheel>", on_mouse_wheel)  # Windows/Mac
# canvas.bind_all("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))  # Linux向上
# canvas.bind_all("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))  # Linux向下
"""
canvas.yview_scroll方法详解：
作用：按指定量滚动Canvas
参数：
number：滚动的数量
正数：向下/向右滚动
负数：向上/向左滚动
what：滚动单位
"units"：按行/列滚动
"pages"：按页滚动
"""
#
# # 检查：内容是否超出Canvas可见区域？
# # 添加诊断代码：
# print(f"Canvas高度: {canvas.winfo_height()}")
# print(f"内部框架高度: {canvas_inner_frame.winfo_reqheight()}")
#
# if canvas_inner_frame.winfo_reqheight() > canvas.winfo_height():
#     print("需要滚动条")
#     scrollbar.pack(side="right", fill="y")
# else:
#     print("不需要滚动条")
#     scrollbar.pack_forget()  # 隐藏滚动条

# inner_frame.update_idletasks()  # 强制立即处理闲时任务





window.mainloop()
