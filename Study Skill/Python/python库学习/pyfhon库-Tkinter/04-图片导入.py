import tkinter
from PIL import ImageTk  # 导入pillow=PIL中的ImageTk模块


# 创建主窗口
root = tkinter.Tk()
# 加载图片并转换为 Tkinter 格式
photo = ImageTk.PhotoImage(file="./images/test-ico.png")
# 在 Label 中显示图片
label = tkinter.Label(root, image=photo)
label.pack()
# # 防止垃圾回收
# label.image = photo
# 启动主循环
root.mainloop()
