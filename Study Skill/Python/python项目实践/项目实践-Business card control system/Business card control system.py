# 导入函数文件(不能循环导入，只能所有文件导入到一个文件，千万不要这个文件和那个文件互相导入（吃过亏了）)
import function_file
import data_file


while True:
    # 系统初始界面模块
    function_file.show_menu()

    # 用户选择模块
    user_input = input("Enter your choice(0/1/2/3): ")
    print("Your choice is: ", user_input)

    if user_input == "1":
        # 调用data.file文件里面的列表的用法，将字典加入列表
        new_user = function_file.new_card(data_file.userdata_file)
        if not new_user:  # 判断是否是False
            pass  # 不进行保存
        else:
            data_file.userdata_file.append(new_user)  # 加入数据库
        print("lading...")
    elif user_input == "2":
        function_file.all_card(data_file.userdata_file)
    elif user_input == "3":
        function_file.find_card(data_file.userdata_file)
    elif user_input == "0":
        break
    else:
        input("Enter Error!")
