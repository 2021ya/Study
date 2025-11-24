def test(name, title="", gender=True):  # 定义缺省参数直接写等于号，然后赋值，这样就是默认参数了---注意：缺省参数必须放在末尾，不要夹在中间，后面不能跟上没有默认参数的函数了
    gender_test = "man"
    if not gender:
        gender_test = "woman"
    print("[%s] %s is %s!" % (title, name, gender_test))


test("2021")  # 缺省参数，大白话来说就是默认参数，如果不传入参数就是默认，传入参数就改变
test("2022", gender=False)  # 若有多个参数时，要想传入指定参数的值，需要将参数名写出来才能指定参数








