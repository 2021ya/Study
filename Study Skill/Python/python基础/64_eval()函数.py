import os


# eval()函数可以将括号里面的看做表达式
user_input = input("")  # 如果你直接用eval()转input代码，那么就可以入侵程序
print(eval(user_input))

