# 导入threading模块（底层还有个模块为thread,这个模块需要传入很多参数，所以简化为了threading）
import threading
import time  # 为方便观察，需要使用时间


def test2():
    """子线程执行"""
    while True:
        print("子线程")
        time.sleep(1)
        break


t1 = threading.Thread(target=test2)  # 此处传入引用，不要调用函数-----创建子线程
t1.start()  # 使用start执行子线程，test2函数会有子线程执行，主线程继续往下执行-----只有调用start()函数才会开始创建线程
print("有子线程时：", threading.enumerate())
"""
每个子线程互不影响，若有多个线程被开始，执行顺序是不确定的，有可能后创建的先执行
"""

while True:
    print("主线程")
    time.sleep(1)
    break


print("无子线程时", threading.enumerate())  # enumerate()函数可查看有多少线程，是一个列表，其中包含主线程和子线程， 可以通过len()来查看列表中有几个线程

"""
若子线程未执行完毕，但主线程执行完毕，那么此时主线程会一直等待子线程，直到子线程执行完毕，回收线程，然后才会退出程序
"""
