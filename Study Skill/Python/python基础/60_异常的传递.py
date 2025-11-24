def demo1():
    return int(input("Please input a number:"))


def demo2():
    demo1()


try:  # 如果传到最后都没有处理异常，就会崩溃，只需要在其中一个地方处理异常即可
    print(demo2())
except Exception as result:
    print(result)

"""
执行流程：

从2行报错，传到6行，传到9行

Please input a number:a
Traceback (most recent call last):
  File "E:\Python\pythonStudy\60_异常的传递.py", line 9, in <module>
    print(demo2())
          ^^^^^^^
  File "E:\Python\pythonStudy\60_异常的传递.py", line 6, in demo2
    demo1()
  File "E:\Python\pythonStudy\60_异常的传递.py", line 2, in demo1
    return int(input("Please input a number:"))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'a'
"""