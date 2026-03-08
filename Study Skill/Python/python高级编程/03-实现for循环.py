from collections.abc import Iterable  # 判断是否为可迭代对象


def new_for(data):
    # 判断是否为可迭代对象
    if not isinstance(data, Iterable):
        print("This is not an iterable")
    # 提取迭代器
    data_iter = iter(data)
    # 取值
    while True:
        try:
            for_data = next(data_iter)
            print(for_data)
        except StopIteration:  # 终止
            break


new_for([1, 2, 3, 4, 5])

print("=" * 30)

for i in [1, 2, 3, 4, 5]:
    print(i)



