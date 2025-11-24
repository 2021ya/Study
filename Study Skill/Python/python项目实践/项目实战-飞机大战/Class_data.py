import os
# import pygame


class Init(object):

    def __init__(self):
        print("Init loading...")


class Account(object):

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.__save()

    def __save(self):
        if not os.path.exists(r".\data.txt"):
            with open(r".\data.txt", "w") as f:
                pass
        with open(r".\data.txt", "r") as f:
            for account in f:
                print(account)
                name = f.readline()
                if name == "name=" + self.name:
                    print("存在")
                    return
            if not f:
                with open(r".\data.txt", 'a+', encoding="utf-8") as f:
                    f.write("name={}\npassword={}\n".format(self.name, self.password))
                    print("successfully!")


if __name__ == '__main__':
    test = Account("2021", "123456")
    # print(test.name)

















