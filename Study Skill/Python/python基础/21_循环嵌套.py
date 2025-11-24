i = 0


while i <= 5:
    print("*" * (i + 1))
    i += 1


print("*", end="我是不换行")  # 正常输出之后会自动换行，但加上end=""之后会取消换行，若将引号换为其他的可以替代
print("...")


line = 1  # 行数


while line <= 5:
    i = 1  # 记录次数，第几行打印几个*
    while i <= line:
        print("*", end="")
        i += 1
    print()
    line += 1








