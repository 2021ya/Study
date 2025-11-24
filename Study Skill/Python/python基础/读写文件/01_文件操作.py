file = open("./README.MD")  # 打开文件，需要用一个变量接收

read = file.read()
print(read)  # 读数据，并打印出,文件指针到末尾，后面再进行读的时候读不到内容了
print(len(read))  # 查看读取的内容长度
print("_" * 50)

read2 = file.read()
print(read2)
print(len(read2))  # 查看读取的内容长度

file.close()  # 关闭文件

"""
open函数的第二个参数，以什么方式打开

访问方式                        说明                                     注意
   r                文件的指针将会放在文件的开头                这是默认模式。如果文件不存在抛出异常
   w                以只写方式打开文件                        如果文件存在会被覆盖。如果文件不存在，创建新文件
   a                以追加方式打开文件                        如果该文件已存在，文件指针将会放在文件的结尾。如果文件不存在，创建新文件进行写入
   r+               以读写方式打开文件                        文件的指针将会放在文件的开头。如果文件不存在，抛出异常
   w+               以读写方式打开文件                        如果文件存在会被覆盖。如果文件不存在，创建新文件
   a+               以读写方式打开文件                        如果该文件已存在，文件指针将会放在文件的结尾。如果文件不存在，创建新文件进行写入
"""

file = open("./README.md", "r")  # 只读，默认
file.close()
file = open("./README.md", "w")  # 只写，覆盖文件
file.close()
file = open("./README.md", "a")  # 追加
file.close()
file = open("./README.md", "a+")  # 以读写打开，并且追加模式，若文件已存在，追加；不存在，创建新文件
file.close()
file = open("./README.md", "r+")  # 以读写打开，指针放开头，若文件不存在，报错
file.close()
file = open("./README.md", "w+")  # 以读写打开，若文件存在，覆盖；不存在，创建新文件
file.close()

file = open("./README.md", "r", encoding="utf-8")  # encoding="编码格式"
print(file)
file.close()

print("_" * 50)

file = open("./README.md", "a+", encoding="utf-8")
file.write("aaaaaa\naaaaaaa\naaaaaaa")  # 当前文件指针在末尾
file.close()

file = open("./README.md", "r", encoding="utf-8")

while True:
    text = file.readline(4)  # 一次读取一行,其中的参数值指定读取几个字符
    print(text, end="")
    if not text:  # 如果当读到行数内容为空时
        break

file.close()


# 复制小文件（可以直接读取所以文件）（如果复制大文件，建议一行一行读取，不然会占用内存）

file = open("./README.md", "r", encoding="utf-8")  # 打开旧文件
file_text = file.read()  # 读旧文件
new_file = open("./NEW_README.md", "w", encoding="utf-8")  # 创建新文件
new_file.write(file_text)  # 写入到新文件
file.close()  # 关闭旧文件
new_file.close()  # 关闭新文件

print("_" * 50)

file = open("./NEW_README.md", "r", encoding="utf-8")
print(file.read())
file.close()


# with语句————任何打开文件之后运行完with块代码自动退出
with open("./NEW_README.md", "r", encoding="utf-8") as file:  # 打开文件作为file
    print(file.read())  # 处理数据
    # 自动关闭文件
