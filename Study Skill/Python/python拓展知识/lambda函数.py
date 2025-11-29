# lambda函数
# 用于简化函数体，通常作为参数时使用此函数
"""
lambda 参数,参数: 执行代码
"""
# 示例代码
button = tkinter.Button(self.home_frame, text="test", command=lambda: self.show_frame(self.about_frame))
