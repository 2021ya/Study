import function1
import function2 as f2  # 使用as来给模块起别名为f2，这样以后，之后代码调用就用别名来调用函数
from function1 import name1  # 使用"from 模块名 import 工具名"来导入的工具之后的代码不需要再写模块名了，但只能导入单个工具，相当于直接就是在当前文件中有了这个代码
from function1 import MkTest as Test1
from function3 import MkTest
from function3 import *  # 导入这个模块的所有工具，同样相当于当前文件有这个代码了，在当前当前文件如果又写了一个与模块重名的东西，是不会提示的


function1.Mk1()
f2.Mk2()
print(name1)
MkTest()  # 若同时导入两个模块中有相同的工具名称，那么之后运行之后导入的那个工具，这个时候需要用别名来避免重名
Test1()  # 同工具包，使用别名调用
print(function1.__file__)  # 每个模块都会内置一个属性，可以查看模块的完整路径

