class House:

    def __init__(self, name, area):

        print("初始化房子中...")
        self.name = name  # 房子名称
        self.area = area  # 房子面积
        self.furniture_name_list = []  # 房子中家具名称列表
        self.free_area = area  # 剩余面积

    def __str__(self):
        return ("House name : %s\nHouse area : %.02f\nHouse free area:%.02f\nHouse furniture:%s"
                % (self.name, self.area, self.free_area, self.furniture_name_list))  # 代码太长的话可以用小括号扣住，然后回车

    def __del__(self):
        print("House deleted...")

    def add_furniture(self, furniture_name, furniture_area):
        """添加家具，将家具添加到家具名称列表"""
        if furniture_area < self.free_area:
            self.furniture_name_list.append(furniture_name)  # 添加家具到家具列表
            self.free_area -= furniture_area  # 计算剩余面积
            print("Add %s succeed!" % furniture_name)
        else:
            print("Add %s fail!" % furniture_name)


class Furniture:

    def __init__(self, furniture_name, furniture_area):
        """初始化家具"""
        print("初始化家具中...")
        self.name = furniture_name
        self.area = furniture_area

    def __str__(self):
        return "家具名称：%s   家具面积：%.02f" % (self.name, self.area)

    def __del__(self):
        print("Furniture deleted...")


# 主程序
my_house = House("my house", 5)
bed = Furniture("席梦思", 4)
chest = Furniture("衣柜", 2)
table = Furniture("桌子", 1.5)

print(bed)
print(chest)
print(table)

my_house.add_furniture(bed.name, bed.area)
my_house.add_furniture(chest.name, chest.area)
my_house.add_furniture(table.name, table.area)
print(my_house)
