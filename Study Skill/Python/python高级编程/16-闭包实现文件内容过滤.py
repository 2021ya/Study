"""
过滤一个txt文件内容的邮箱，取出需要类型的邮箱
"""


def inner_filter(email_name):
    """创建闭包对象时，需要传入需要过滤的邮箱，调用时需要传入文件"""
    def file_name(file):
        try:
            with open(file, 'r') as f:  # 只读方式打开文件
                lists = f.readlines()  # 一次读取一行
                f.close()  # 关闭文件
            result = [i for i in lists if email_name in i]
            # 列表推导式：分为两个部分
            """
            第一部分：for i in lists
                遍历读取到的所有数据
            第二部分：if email_name in i
                将遍历到的数据进行判断，查看邮件后缀是否在行中，如果在，那么就会存储到新列表result中
            """
            return result  # 返回结果
        except Exception as e:
            print("Error:", e)

    return file_name


if __name__ == '__main__':
    filter1 = inner_filter("@qq.com")
    print(filter1("test.txt"))
