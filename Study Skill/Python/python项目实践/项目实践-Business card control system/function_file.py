# function文件库


def show_menu():
    """显示初始菜单"""
    print("\n\n")
    print("*" * 60)
    print("Welcome to use \"【Business card control system】 V1.0\"")
    print()
    print("1.New card \n2.All card \n3. Find card \n0. Exit system")
    print()
    print("*" * 60)


def new_card(data_file):
    """需要提前传入一个data(内含字典数据),输入名字、密码、手机号、邮件，返回一个字典"""
    user_name = input("Enter your name: ")
    for i in data_file:  # 判断是否重名
        if user_name == i["name"]:
            input("This name in data file is same, please find and revise this name!（Press Enter to continue...）")
            return False
    else:
        user_password = input("Enter your password: ")
        user_phone_number = input("Enter your phone number: ")
        if len(user_phone_number) != 11 or not user_phone_number.isdigit():  # 判断电话号位数
            input("Your phone number is error!please try enter again(enter)")
            return  # 返回到调用函数处，下方代码不执行
        new_email = input("Enter your email: ")
        if "@" not in new_email or "." not in new_email:
            input("Your email is error!please try enter again(enter)")
            return
        user_email = new_email
        new_dic = {"name": user_name,
                   "password": user_password,
                   "phone_number": user_phone_number,
                   "email": user_email}
        print("-" * 60)
        print("Add successful!")
        print("Press enter to continue")
        input("-" * 60)
        return new_dic


def all_card(data_file):
    """显示所有名片"""
    if len(data_file) == 0:  # 判断是否为空
        print("")
        print("-" * 60)
        print("Data is None! \nPress Enter to continue...")
        input("-" * 60)
    else:
        for i in data_file:  # 打印数据
                print("-" * 100)
                print("Name:%6s" % (i["name"]), end="\t\t\t")
                print("password:%6s" % (i["password"]), end="\t\t\t")
                print("phone number:%11s" % (i["phone_number"]), end="\t\t\t")
                print("email:%16s" % (i["email"]))
        print("-" * 100)
        input("Press Enter to continue...")


def find_card(datafile):
    """输入一个列表(内含字典数据)，查找名片"""
    name_find = input("Enter your need find name: ")
    password_find = input("Enter %s password: " % name_find)
    # phone_find = input("Enter %s phone number: " % name_find)
    # email_find = input("Enter %s email: " % name_find)
    for i in datafile:
        if (i["name"] == name_find) and (i["password"] == password_find):
            index = datafile.index(i)
            print("-" * 100)  # 打印数据
            print("Name:", i["name"], end="\t\t\t")
            print("password:", i["password"], end="\t\t\t")
            print("phone number:", i["phone_number"], end="\t\t\t")
            print("email:", i["email"])
            print("-" * 100)
            user_choose = input("Your choose is (1.revise/2.delete/3.return):")
            if user_choose == "1":
                new_name = input("Enter your new name: ")
                if new_name != name_find:  # 如果改名字才会判断是否重名
                    for ii in datafile:  # 判断是否重名
                        if new_name == ii["name"]:
                            input("This name in data file is same, please find and revise this name!（Press Enter to "
                                  "continue...）")
                            return  # 返回到调用函数处，下方代码不执行
                new_phone_number = input("Enter your new phone number: ")
                if len(new_phone_number) != 11 or not new_phone_number.isdigit():  # 判断电话号位数
                    input("Your phone number is error!please try enter again(enter)")
                    return  # 返回到调用函数处，下方代码不执行
                new_email = input("Enter your new email: ")
                if "@" not in new_email or "." not in new_email:
                    input("Your email is error!please try enter again(enter)")
                    return
                i["name"] = new_name
                i["password"] = input("Enter your new password: ")
                i["phone_number"] = new_phone_number
                i["email"] = new_email
                print("-" * 60)
                print("Lading...")
                print("Revise successfully!")
                input("Press Enter to continue...")
            elif user_choose == "2":
                user_enter_choose = input("yes or no?:")
                if user_enter_choose == "yes":
                    datafile.pop(index)
                    print("-" * 60)
                    print("Lading...")
                    print("Delete successfully!")
                    input("Press Enter to continue...")
                elif user_enter_choose == "no":
                    print("-" * 60)
                    print("Enter cancel!")
                    print("Press Enter to continue...")
                    input("-" * 60)
                else:
                    print("-" * 60)
                    print("Enter error!")
                    print("Press Enter to continue...")
                    input("-" * 60)
            elif user_choose == "3":
                return
            else:
                print("-" * 60)
                print("Enter error!")
                print("Press Enter to continue...")
                input("-" * 60)
            break
    else:
        print("-" * 60)
        print("Name or password error!")
        print("Press Enter to continue...")
        input("-" * 60)
