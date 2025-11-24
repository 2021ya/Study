# 用户数据库
data_user = [
    {"name": None,
     "password": None,
     "phone_number": None,
     "email": None}
]


ctrl_system_password = "999"
try_find_number = 0


# 程序主体
while True:
    print("\n\n")
    print("*" * 60)
    print("Welcome to 【Business card control system(tempV1.0)】\n")
    print("1.New card \n2.All card \n3. Find card \n4. Exit system\n")
    print("*" * 60)

    # 用户输入模块
    input_user = input("Enter your choice: ")

    # 程序判断模块
    if input_user == "1":
        user_name = input("Enter your name: ")
        user_password = input("Enter your password: ")
        if_ture_password = user_password.isalnum()  # 判断密码是否为字母或数字，返回Ture,False
        # if if_ture_password == True:
        if if_ture_password:  # 可以直接判断是否为ture或false,不必自己写
            user_phone_number = input("Enter your phone number: ")
            if len(user_phone_number) == 11 and user_phone_number.isnumeric():  # 判断手机号
                # i_number = 0
                # for i in user_phone_number:  # 循环判断手机号位数
                #     i_number += 1
                if len(user_phone_number) != 11:
                    input("Phone number format Error! Please try again.(enter)")
                else:
                    user_email = input("Enter your email: ")
                    temp_dic = {"name": user_name,
                                "password": user_password,
                                "phone_number": user_phone_number,
                                "email": user_email}
                    data_user.append(temp_dic)
                    input("Add successfully!(enter)")
            elif not user_phone_number.isnumeric():
                input("Phone number format Error! Please try again.(enter)")
        # elif if_ture_password == False:
        elif not if_ture_password:
            input("Format Error! Please try again.(enter)")

    elif input_user == "2":
        system_password = input("Please enter system password: ")
        if system_password == ctrl_system_password:
            print("SYSTEM:\n", data_user)
            input("SYSTEM:Find!(enter)")
        else:
            input("System password Error! Please try again.(enter)")
    elif input_user == "3":
        if try_find_number <= 2:
            user_find_name = input("Enter your need find name: ")
            user_find_password = input("Enter %s password: " % user_find_name)
            print("lading...")
            for i in data_user:
                if i["name"] == user_find_name and i["password"] == user_find_password:
                    index_dic = data_user.index(i)  # 查询这个字典索引
                    print(i)  # 输出这个字典
                    user_choose = input("Find!Please enter your choose(1.revise/2.delete/3.exit): ")
                    # 查询到的字典操作
                    if user_choose == "1" or user_choose == "revise":
                        user_revise = input("Revise your card(1.name/2.password/3.phone_number/4email): ")
                        if user_revise == "1" or user_revise == "name":  # 修改字典内容
                            user_revise_name = input("Enter your revise name: ")
                            i["name"] = user_revise_name
                            input("revise successfully!(enter)")
                            break
                        elif user_revise == "2" or user_revise == "password":
                            user_revise_password = input("Enter your revise password: ")
                            i["password"] = user_revise_password
                            input("revise successfully!(enter)")
                            break
                        elif user_revise == "3" or user_revise == "phone_number":
                            user_revise_phone_number = input("Enter your revise phone number: ")
                            i["phone_number"] = user_revise_phone_number
                            input("revise successfully!(enter)")
                            break
                        elif user_revise == "4" or user_revise == "email":
                            user_revise_email = input("Enter your revise email: ")
                            i["email"] = user_revise_email
                            input("revise successfully!(enter)")
                            break
                        else:
                            input("Revise Error! Please try again.(enter)")
                            break
                    elif user_choose == "2" or user_choose == "delete":
                        data_user.pop(index_dic)
                        input("delete successfully!(enter)")
                        break
                    elif user_choose == "3" or user_choose == "exit":
                        break
            else:  # for循环完全循环完毕才会执行
                input("name or password Error! Please try again.(enter)")
                try_find_number += 1
        elif try_find_number > 2:
            input("Too many attempts!(enter),try=%d" % try_find_number)
        else:
            input("Error:find-number-judge")
    elif input_user == "4":
        break
    elif input_user == "system":
        system_password = input("Please enter system password: ")
        if system_password == ctrl_system_password:
            ctrl_system = input("Please enter system choose(1.revise system password/2.find times/3.All delete):")
            if ctrl_system == "1" or ctrl_system == "revise system password":
                ctrl_system_password = input("Enter system revise password: ")
                input("revise successfully!(enter)")
            elif ctrl_system == "2" or ctrl_system == "find times":
                try_find_number = input("<try:\"%s\">,please revise try number:" % try_find_number)
                if try_find_number.isnumeric():
                    try_find_number = int(try_find_number)
                    print("lading...")
                    input("revise successfully!(enter)")
                else:
                    input("Format Error! Please try again.(enter)")
            elif ctrl_system == "3" or ctrl_system == "all delete":
                all_delete = input("yes/no?")
                if all_delete == "yes":
                    data_user.clear()
                    input("revise successfully!(enter)")
                elif all_delete == "no":
                    input("revise Error! Please try again.(enter)")
                else:
                    input("system enter Error! Please try again.(enter)")
            else:
                input("system enter Error! Please try again.(enter)")
        else:
            input("system enter Error! Please try again.(enter)")
    else:
        input("Unknown Enter Error!(enter)")
