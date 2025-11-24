students = [
    {"name": "2021",
     "age": 18,
     "height": 1.8,
     "weight": 56,
     "id": "11111111111"},

    {"name": "2022",
     "age": 18,
     "height": 1.75,
     "weight": 60,
     "id": "22222222222"}
]


user_name = input("Please enter you need look up name:")


for student in students:  # 一个字典算一个整体，循环遍历的时候一个字典一个字典拿的，拿出的每一个字典都为变量student
    if user_name == student["name"]:  # 假如拿出一个字典，判断这个字典的key(name)，是否有用户输入的name，student["name"]返回的是value
        print(student)  # 如果是，打印这个字典，然后退出，不继续遍历
        break
else:  # 循环结束之后还未找到用户的name，打印未找到
    print("Sorry, your name was not found!")
"""
    相当于是看for循环是否完整的遍历完成
    如果遍历完成打印else的语句
    如果遍历中断，跳过else语句
"""












