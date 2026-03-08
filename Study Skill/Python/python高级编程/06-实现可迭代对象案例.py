

class Data(object):
    """可迭代对象类"""
    def __init__(self):
        self.data = []  # 创建存储数据库

    def add(self, every):
        """
        向数据库中添加数据
        :param every:值
        """
        self.data.append(every)

    def __iter__(self):
        """
        标记为可迭代对象
        :return: 迭代器-DataIter
        """
        return DataIter(self)


class DataIter(object):
    """迭代器"""
    def __init__(self, iterable):
        self.iterable = iterable  # 接收可迭代对象
        self.current = 0  # 用于记录当前访问到的位置

    def __iter__(self):
        """
        因为迭代器本身也是可迭代对象，所以这里需要返回自身，使自身处于可迭代状态，这样迭代器本身也可被for循环来遍历
        通过iter()函数取出迭代器的时候，数据已经有了，然后是用迭代器来手动执行遍历
        """
        return self

    def __next__(self):
        """取值"""
        if self.current < len(self.iterable.data):  # 使用len来判断数据多少,self.iterable.data来读取可迭代对象中的全部数据
            data_source = self.iterable.data[self.current]  # 使用切片拿数据
            self.current += 1
            return data_source  # 若被迭代，返回数据
        else:  # 如果拿完全部数据还要继续遍历的话直接返回StopIteration来使for循环中断
            # return StopIteration
            raise StopIteration  # raise是返回异常


if __name__ == '__main__':
    data = Data()  # 实例化可迭代对象
    data.add(1)  # 添加数据
    data.add(2)
    data.add(3)
    data.add(4)
    data.add(5)
    data.add(6)
    data.add(7)
    data.add(8)
    data.add(9)
    for i in data:  # 使用for循环来遍历自定义可迭代对象
        print("不使用迭代器取数据：", i)

    print("*" * 30)

    for i in iter(data):
        print("直接用迭代器取数据：", i)
        """
        因为迭代器本身也是可迭代对象，这时就用到了迭代器中的__iter__函数了，里面返回的是自身
        """

    print("*" * 30)

    data_iter = iter(data)  # 提取迭代器
    print("手动取数据：", next(data_iter))  # 使用迭代器来手动遍历数据
