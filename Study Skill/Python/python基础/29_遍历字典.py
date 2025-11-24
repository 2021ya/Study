temp_dict = {"name": "2021",
             "age": 100,
             "phone": 110}


for key in temp_dict:  # 若只有一个变量来接受，那么只会返回key
    print(key)


for key, value in temp_dict.items():  # 若有两个变量，则全会接受
    print(key, value)


for key in temp_dict:
    print("%s - %s" % (key, temp_dict[key]))  # em，视频里面教的。。。这个的意思是第一个接受key，第二个是用函数将key值输入进去然后返回value











