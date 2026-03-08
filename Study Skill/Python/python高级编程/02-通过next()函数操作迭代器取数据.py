num = {1, 2, 3, 4, 5, 6, 7, 8, 9}

num_iter = iter(num)

print(next(num_iter))  # 通过next函数可以每次取数据，但只能一次取一个

"""
for 循环原理

for num in test:
    print(num)
    
原理讲解：
    test是一个可迭代对象，通过取出test的迭代器来来执行取值，然后赋值给num变量，然后执行下方缩进语句，直到所有数据都获取完毕之后停止
for循环停止原理：(构想，实际是用c语言来实现)
    在取完所有数据之后，如果再次进行取值，会产生StopIteration异常，但是在for循环的代码中，如果遇到此异常，会结束循环，也就是说，停止取值

"""
