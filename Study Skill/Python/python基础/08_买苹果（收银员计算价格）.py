price_str = input("请输入产品单价：")
weight_str = input("请输入产品重量：")
"""
输入：
print(price_str * weight_str)
输出：
Traceback (most recent call last):
  File "E:\Python\pythonProject\08_买苹果（收银员计算价格）.py", line 3, in <module>  # em这里为什么会报错，但是可以正常执行（我查理一下，反斜杠是转义字符，可能会有误会，但先这样吧，留个纪念，无伤大雅）
    print(price_str * weight_str)
          ~~~~~~~~~~^~~~~~~~~~~~
TypeError: can't multiply sequence by non-int of type 'str'

# 字符串类型不可直接运算
"""
price_float = float(price_str)
weight_float = float(weight_str)  # 使输入变成浮点数，可以运算

money = price_float * weight_float

print(money)
print(price_float * weight_float)
print(float(price_str) * float(weight_str))
print(float(input("请输入你的产品单价：")) * float(input("请输入你的产品重量：")))  # 来自网友的写法，666,一行代码解决，666
# 四种输出方法

