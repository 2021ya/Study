first_name = "张"
last_name = "三"  # 定义变量

full_name = first_name + last_name  # 字符串拼接直接使用“+”

print(full_name)

print(last_name * 10)  # 也可以直接使字符串多次打印

print((first_name + last_name) * 10)  # 嗯，很厉害，哈哈哈

# 注意：字符串不可以和数字相加

"""
代码：print(full_name + 10)
不信者：
Traceback (most recent call last):
  File "E:\Python\pythonProject\06_字符串拼接.py", line 15, in <module>
    print(full_name + 10)
          ~~~~~~~~~~^~~~
TypeError: can only concatenate str (not "int") to str
张三
三三三三三三三三三三
张三张三张三张三张三张三张三张三张三张三
"""

print(full_name + "10")  # 但是可以给它数字变成字符串，你只需要给它加上引号（但这也是字符串拼接而已）
