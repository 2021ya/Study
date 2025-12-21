import threading


def test(num, num2, num3=4, num4=4):
    for i in range(num):
        print(i)

    for i in range(num2):
        print("aa", i)

    print(num3, num4)


t = threading.Thread(target=test, args=(6, 5), kwargs={"num4": 555, "num3": 4444})  # 直接写数字不是元组，需要加个逗号, 也可以用字典传入指定参数
# 若要传参，那么需要用args来传元组(可迭代对象即可，意思就是可以获取里面的值即可，比如传入两个，那么就需要用元组或列表这种可以获取里面的每个值即可)，里面的值会传给子线程
t.start()
