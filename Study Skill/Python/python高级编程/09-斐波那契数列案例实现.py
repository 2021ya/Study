# 需求：实现斐波那契数列
# 1， 1， 2， 3， 5， 8


# 方案一：函数
def test1():
    # 定义初始值
    sum_old1 = 1
    sum_old2 = 1
    sum_new1 = 0  # 存储前两项的和
    # 控制循环次数
    count = 1
    # 初始
    # print("1, 1", end=", ")
    print(1, end=", ")  # 拆包升级法-打印初始1
    while True:
        if count == 10:  # 控制生成数量
            break
        # sum_new1 = sum_old1 + sum_old2  # 运算
        # sum_old1 = sum_old2  # 移位2：旧数据2成为了旧数据1
        # sum_old2 = sum_new1  # 移位1：新数据总和成为了旧数据2
        # sum_old1, sum_old2 = sum_old2, sum_new1  # 拆包法
        sum_old1, sum_old2 = sum_old2, sum_old1 + sum_old2  # 拆包升级法--核心算法

        print(sum_old1, end=", ")
        count += 1


# 方法二：迭代器
class Iterable(object):

    def __init__(self):
        # 初始值
        self.a = 1
        self.b = 1

    def __iter__(self):
        return self  # 返回自身

    def __next__(self):
        a = self.a  # 先提前存上一个1，后面是从第二个1开始计算的
        self.a, self.b = self.b, self.a + self.b
        return a


# 方法三：生成器
def generator():
    a = 1
    b = 1
    while True:
        temp = a
        a, b = b, a + b
        yield temp  # 挂起，一旦出现这个yield，那么这个函数被叫做生成器，会让代码挂起，停在此处,如果直接打印此函数，那么会返回生成器标签,如果要取temp值，那么就需要next()函数来执行了
        """
        一个生成器中可以有多个yield，可以用next()函数来执行，如果最后有return，那么生成器终止的时候会报错“StopIterable:return的返回值”
        如果多个yield执行完毕，还要继续调用next()函数的话，会报StopIterable异常，如果只有一个yield的话，多调用一次同样如此，那么此时while的
        作用就显示出来了
        如果想要return的返回值，那么就需要捕获异常信息了
        例如：
            except StopIteration as e:
                print(e.value)  # 此时，需要调用异常的.value函数来取返回的异常值
        """


if __name__ == '__main__':
    # 方法一调用
    test1()

    # 方法二调用
    print()

    count = 0
    iterable = Iterable()
    while True:
        if count == 10:
            break
        count += 1
        print(next(iterable), end=", ")

    # 方法三调用
    print()

    print(generator())
    gen = generator()  # 提取生成器
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))

