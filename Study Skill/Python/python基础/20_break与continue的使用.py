i = 0


while i < 10:
    if i == 3:
        i += 1
        continue  # 跳过一次循环
    elif i == 5:
        break  # 中断整个循环
    print(i)
    i += 1

