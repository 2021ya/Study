class MusicPlayer(object):

    instance = None  # 类属性，初始是空
    init_flag = False  # 判断是否初始化过，默认没有初始化

    # 此方法不需要任何装饰器比如“staticmethod、classmethod”
    # __new__方法的职责：1.创建内存空间2.返回对象的引用（内存空间）
    # __new__方法必须返回对象的引用，否则不会执行，因为没有分配空间，只会返回None
    # 下方是重写__new__方法，此方法在创建对象的时候自动执行
    def __new__(cls, *args, **kwargs):
        print("\"__new__\"loading...")
        if MusicPlayer.instance is None:  # 如果之前没有创建过实例，那就创建一个,如果有，就返回同一个实例的引用（以免重复创建类实例）
            cls.instance = super().__new__(cls)  # 调用父类方法中的__new__方法返回对象引用,类本身也是对象，所以给类创建一个实例(调用父类方法记得super()加括号！！)
            cls.instance = object.__new__(cls)  # 旧版继承父类方法---与上方代码相同效果,代码意思："object 类，请为 MusicPlayer 类创建一个实例",cls表示类自己，与self同理
        return cls.instance  # 必须返回引用

    def __init__(self):
        if MusicPlayer.init_flag is False:  # 如果初始化过，就跳过初始化，否则进行初始化
            print("\"__init__\"loading...")
            MusicPlayer.init_flag = True
            return
        return


player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)











