# python创建包，有两种方式1.自己手动创建init.py文件2.直接创建包，python会帮忙创建init.py文件
# 导入包的时候自动导入包中的所有文件(前提是在init.py文件中导入了模块列表)
from . send_massage import send_massage  # 如果要向外界提供模块，那么需要再init.py文件中写模块列表，格式为“from . 模块名 import 函数名”
from . receive_massage import receive_massage  # "."为当前目录
