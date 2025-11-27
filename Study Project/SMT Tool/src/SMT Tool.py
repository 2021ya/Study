import time
import UI  # 导入UI界面
import logic  # 导入程序逻辑


class Main(object):
    """程序主类"""

    def __init__(self):
        """初始化程序"""
        # 类初始化
        self.ui = UI.UI()  # ui
        self.file = logic.File()  # 文件操作
        self.log = logic.Log()  # 日志

    def main(self):
        self.ui.main()


if __name__ == '__main__':
    run = Main()
    run.main()
