class Test(object):

    def __init__(self, name):
        self.name = name
        self.a = 1
        self.b = 2

    def __getattribute__(self, item):
        """
        属性拦截器，在访问属性时，会判断是否有这个方法，如果有的话，那么就会执行这个方法，将这个方法的返回值作为它的属性
        :param item: 哪个实例调用方法属性来获取数据，那么就会把这个方法名称传入item中
        :return:自定义返回值
        """
        if item == 'a':  # 判断这个方法是否访问a
            return "禁止访问"
        elif item == 'b':
            return 2  # 注意，这里不要使用self.b，如果写成这样，那么又跳到这个拦截器里面了
        # else:  # 如果其余的没有写，那么就会返回这个，如果不写的话，那么会提示没有这个属性,但一般不这样写
        #     return "不提供"
        else:
            # 两种写法：
            return super().__getattribute__(item)  # 调用父类来查找，super在创建的时候就已经记录了本身，所以不需要传self了
            # """
            #     第二种方法解释：
            #         self是将a传给它了，item是把name属性传进去了，它的意思是，调用父类（既然是调用父类，那么super理论上也可以）来查找item这个属性
            #         这个时候返回的就是取出的值了
            # """
            # return object.__getattribute__(self, item)  # 调用父类来查找


a = Test("python")
print(a.name)
