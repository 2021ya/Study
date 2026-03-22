class Goods(object):

    def __init__(self, price):
        self.original_price = price  # 原价
        self.discount = 0.8  # 折扣价

    @property
    def price(self):
        return self.original_price * self.discount  # 计算价格

    @price.setter
    def price(self, new_price):
        self.original_price = new_price  # 修改价格

    @price.deleter
    def price(self):
        del self.original_price  # 删除价格


apple = Goods(100)
print("Original price:", apple.price)

apple.original_price = 200
print("Original price:", apple.price)

del apple.price




