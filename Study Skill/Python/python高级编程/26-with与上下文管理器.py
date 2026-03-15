from contextlib import contextmanager


class File(object):

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):  # 使用with是自动调用
        print("will open", self.filename)
        self.f = open(self.filename, self.mode)
        return self.f  # 此时返回给21行代码中的as f中的f，那么with打开的就是self.f

    def __exit__(self, exc_type, exc_val, exc_tb):  # 当with的语句执行完毕之后，会自动执行，释放资源;
        # 注意，无论是否使用到了exc_type, exc_val, exc_tb这三个参数，都需要写上，因为在关闭时，python无论是否异常都会传入3个值
        # 第一个是错误类型，第二个是错误值，第三个是异常发生位置的堆栈信息，如果没有异常，那么都返回None
        print("will close")
        self.f.close()


"""
上下文管理器就是可以使用with的对象
类中带有__enter__和__exit__就是上下文管理器
"""

with File('test.txt', 'a') as f:
    f.write('hello@qq.com\n')


print("*" * 30)


@contextmanager  # 可以直接将类写成装饰器
def my_open(path, mode):
    f2 = open(path, mode)
    yield f2  # 返回给原调用地方，然后暂停
    f2.close()


with my_open('out.txt', 'w') as f:  # 此时f接收的是上方f2的返回
    f.write("hello, the simplest context manager")  # 执行
    # 结束之后会自动调用函数yield后面的剩余代码
