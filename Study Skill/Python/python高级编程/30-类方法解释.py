class Test(object):

    def __init__(self):
        pass

    def test1(self):
        pass

    @classmethod
    def test2(cls):
        pass
    """
    @classmethod解释
        这个类方法原理也是装饰器
        def classmethod(src_func):  这个参数存的是原函数的引用
            def function(*args):  # 调用内部方法,接收函数参数
                a = src_func.__class__  # 这一步就等于a = Test()  # 由于是对类的访问与操作，所以，我们需要获取类，然而，我们可以通过原函数引用来调用.__class__来访问类，这样就可以操作类了                
                return src_func()  # 执行原函数，并返回
            return function
            
    # 静态方法同理，只不过不需要对类操作，只是独立的一个方法，那么就不需要对内层函数传参数
    """