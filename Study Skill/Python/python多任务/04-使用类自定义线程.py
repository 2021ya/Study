import threading
import time


class MyThread(threading.Thread):  # 此处要继承线程父类
    """使用类来实现自定义线程"""

    def run(self):  # 此函数创建线程的时候会自动执行run()函数
        while True:
            print("Thread-1 run...")
            time.sleep(1)

    def xx(self):  # 其他函数除非run()函数调用，否则不会执行，可以理解为，其他函数都是为run()函数服务的
        pass


t = MyThread()  # 实例化对象
t.start()  # 此处创建线程，.start()方法会自动调用类中的run()函数
#
print("aaa")
#
# while True:
#     print("Main thread run...")
#     time.sleep(1)
