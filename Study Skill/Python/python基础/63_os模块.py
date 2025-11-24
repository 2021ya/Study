import os


with open("test.txt", "w") as file:
    print(f"创建成功：{file}")

# 重命名，第一个是原文件名，第二个是修改之后的名称
os.rename("./test.txt", "./os_test.txt")

# 删除文件
os.remove("./os_test.txt")

# 查看目录，传入一个文件目录路径，返回当前路径目录下的所有文件与目录列表
os.listdir("./")

# 判断是否为目录
print(os.path.isdir("./os_test.txt"))

os.mkdir(r"./test")  # 创建单个目录
os.makedirs(r".\test\test1")  # 创建递归目录
os.rmdir("./test")  # 删除空目录

# 路径信息获取
print(os.path.exists("./test.txt"))      # 判断路径是否存在
print(os.path.isfile("./test.txt"))      # 判断是否为文件
print(os.path.isdir("./"))               # 判断是否为目录
print(os.path.getsize("./test.txt"))     # 获取文件大小
print(os.path.getmtime("./test.txt"))    # 获取最后修改时间

# 获取当前工作目录
print(os.getcwd())

# 执行系统命令
print(os.system("dir"))

# 路径表示方法
os.system("C:\\Users\\Public\\Desktop\\微信.lnk")  # 因为反斜杠有转义的意思，所以可以用两个反斜杠来表示单个反斜杠
os.system(r"C:\Users\Public\Desktop\微信.lnk")  # 也可以在前面加r,表示路径
os.system("C:/Users/Public/Desktop/微信.lnk")  # 也可以换成/


# 详细文件列表,共有三个返回值，第一个为路径（传入目录中的每个文件夹的路径），第二个是（传入目录中有哪些是文件夹），第三个是文件（传入目录中的文件，包括文件夹中的文件，相当于递归了这个目录？差不多）
for path_test, dir_test, file_test in os.walk(r"E:\Python"):
    print(f"当前路径：{path_test}")
    print(f"当前目录文件夹：{dir_test}")
    print(f"当前目录下的文件：{file_test}")
    print("-" * 100)

# 拼接路径，传入两个路径，将两个路径拼接,用join，若要返回值，用变量接收，这里就不写了
os.path.join(r"E:\Python\pythonStudy", r"os_test.txt")

# 将路径分隔为目录和文件，以元组返回,需要接收返回值同样用变量接收，这里不写了
os.path.split(r"E:\Python\pythonStudy\os_test.txt")
os.path.dirname(r"E:\Python\pythonStudy\os_test.txt")  # 只返回目录名称
os.path.basename(r"E:\Python\pythonStudy\os_test.txt")  # 只返回具体文件名称

# 返回当前操作系统——nt=windows
print(os.name)

# 返回当前操作系统路径分隔符
print(os.path.sep)

# 返回绝对路径
print(os.path.abspath(r".\63_os模块.py "))

# 使用os.removedirs删除多级空目录
os.removedirs("level1/level2/level3")



