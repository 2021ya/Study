age = int(input("请输入您的年龄："))

print("方法1：")
if age < 0 or age > 120:  # 或运算
    print("You don't a man")
else:
    print("You are a man")

print("方法2：")
if age >= 0 and age <= 120:  # 与运算，不规范
    print("You are a man")
else:
    print("You don't a man")

print("方法2代码优化：")
if (age >= 0) and (age <= 120):  # 与运算，加括号可以将它视为一个整体
    print("You are a man")
else:
    print("You don't a man")

print("方法3：")  # 上方的改进
if 0 <= age <= 120:
    print("You are a man")
else:
    print("You don't a man")

print("方法4：")  # 非运算
if not 0 <= age <= 120:
    print("You don't a man")
else:
    print("You are a man")
"""
if () or () or ():  # 多个函数用时用括号
    print("You are a man")
    
if (()  # 代码太长时用
    ()
    ()):
    print("You are a man")
"""

