import time

import gevent
import time
from gevent import monkey


monkey.patch_all()  # 打补丁，程序自己改代码


def task(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # gevent.sleep(1)  # time.sleep不可用，需要打补丁：monkey.patch_all()  # 需要导入模块from gevent import monkey,这样time.sleep就视为了gevent.sleep
        time.sleep(1)


g1 = gevent.spawn(task, 3)
g2 = gevent.spawn(task, 4)
g3 = gevent.spawn(task, 5)

g1.join()
g2.join()
g3.join()

"""
gevent只有有耗时操作时，才会切换任务
若遇到耗时操作时，切换到其他函数
相当于做饭等待时，可以做其他事
"""
