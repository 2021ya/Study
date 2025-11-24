for num in [1, 2, 3, 4, 5]:
    print(num)
    if num == 3:
        print("中断循环")
        break
else:
    print("如果for循环完整执行会打印,反之，如果for循环中途中断，则不会打印！")

print("over!")


