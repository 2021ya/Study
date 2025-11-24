from db.model import Model


if __name__ == '__main__':
    model = Model("stu")
    # data_list = model.findall()
    # print(model.find(2))
    # for data in data_list:
    #     print(data)
    # # print(model.delete(4))
    # print(model.fields)  # 取出字段列表
    # print(model.pk)
    # dic = {"name": "2035", "age": "18", "sex": "w", "classid": "python02"}
    # print(model.add(dic))
    # print(model.update("name", "2036", 2))
    data = model.select(where=["classid = \"python01\""], order="name", limit=3)
    for row in data:
        print(row)
