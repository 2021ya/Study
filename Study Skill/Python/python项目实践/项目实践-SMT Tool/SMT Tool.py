import ui  # 导入UI界面(小写，不要用大写做模块名）
import logic  # 导入程序逻辑


# 工具初始化
pop_up = ui.PopUp()

try:
    class Main(object):
        """程序主类"""

        def __init__(self):
            """初始化程序"""
            # 程序类初始化
            self.ui = ui.UI()  # ui
            # 文件类初始化
            self.file = logic.File()  # 文件操作
            self.log = logic.Log()  # 日志

        def main(self):
            self.ui.main()


    if __name__ == '__main__':
        run = Main()
        run.main()
except Exception as e:
    pop_up.error("未知错误[Error:{}]".format(e))
