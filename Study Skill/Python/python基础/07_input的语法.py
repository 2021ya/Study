password = input("请输入你的银行密码，谢谢我要打劫：")  # 引号中间是提示内容
print(password)
print(type(password))
# <class 'str'>

age = input("请输入你的年龄:")
print(age)
print(type(age))
# <class 'str'>
# 输入的默认都是字符串类型em，略有思考

age2 = int(input("请输入你的年龄："))
print(age2)
print(type(age2))
# <class 'int'>
# 哦豁，给它搞成整数了，那我如果输入汉字呢，哈哈哈
"""
输入：aa
控制台：
Traceback (most recent call last):
  File "E:\Python\pythonProject\07_input的语法.py", line 12, in <module>
    age2 = int(input("请输入你的年龄："))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'aa'

# 这这这？？？嗯，bug，让我想想，可以判断用户输入的是什么类型的数据吗？好吧，现在还没想到
"""

age3 = float(input("请输入你的年龄："))
print(age3)
print(type(age3))
# <class 'float'>
# 浮点数
