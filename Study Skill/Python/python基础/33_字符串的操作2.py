str1 = "   \n \t \r"  # \n换行\t制表\r回车，这个算空格
str2 = "aa"
str3 = "五千零一"
str4 = "aaa1313"
str5 = "AV啊V"
str6 = "aa啊aa"
str7 = "aaaa"
str8 = "10101010101010101010101010101010101"
str9 = "Aa"
str10 = "101210"
str11 = "101210\r"  # 这种打印不出的类似的
str12 = "def"  # 内置函数名之类的
str13 = "def1aa1a1"
str14 = "def1aa1a1"
str15 = "def1aa1a1"
str16 = "def1aa1a1"
list_17 = ["登鹳雀楼",
           "王之涣",
           "白日依山尽",
           "黄河入海流",
           "欲穷千里目",
           "更上一层楼"]
str18 = "   aaa  \t\n  "
str19 = "登鹳雀楼\n王之涣\t白日依山尽\r黄河入海流\t欲穷千里目\n更上一层楼"
str20 = "0123456789"

# 判断字符串是否只包含空格
print(str1.isspace())

# 判断字符串是否都是字母
print(str2.isalpha())

# 判断字符串是否都为数字
print(str3.isnumeric())  # 不能判断是小数，但可以判断汉字数字！

# 判断字符串由字母或数字组成
print(str4.isalnum())  # 不能判断是小数

# 如果有字母判断是否为大写字符串
print(str5.isupper())

# 如果有字母判断是否为小写字符串
print(str6.islower())

# 如果字符串中的所有字符都为ASCll(英文)，否则为 False。?
print(str7.isascii())

# 返回 True 如果字符串是十进制字符串。否则返回 False，也就是日常数字0123456789，常用
print(str8.isdecimal())

# 判断字符串是否为标题（首字母大写）
print(str9.istitle())

# 判断字符串是否为数字字符串
print(str10.isdigit())  # 不能判断是小数

# 判断字符串是否都可打印
print(str11.isprintable())

# 判断字符串是否为有效的python标识符
print(str12.isidentifier())

# 判断字符串是否以指定字符串开头
print(str13.startswith("aa"))

# 判断字符串是否以指定字符串结尾
print(str14.endswith("aa"))

# 替换字符串,将旧字符串换为新字符串
print(str15.replace("aa", "ccc"))

# 查找指定字符串,返回索引，若查找值不存在返回-1
print(str16.find("aa"))

# 字符串的居中调整
for i in list_17:
    print("|%s|" % i.center(11, "-"))  # .center函数第一个为宽度，第二个为填充字符（默认英文空格）

print("*" * 50)

# 字符串的居左调整
for i in list_17:
    print("|%s|" % i.ljust(11, "-"))  # .ljust()函数

print("*" * 50)

# 字符串的居右调整
for i in list_17:
    print("|%s|" % i.rjust(11, "-"))  # .rjust()函数

# 去除空白字符，就是看不见的字符，包括换行，空格，回车之类的
print(str18)
print("*" * 50)
print(str18.lstrip())  # string.lstrip()截掉 string左边(开始)的空白字符
print("*" * 50)
print(str18.rstrip())  # stringstrip()截掉 string 右边(末尾)的空白字符
print("*" * 50)
print(str18.strip())  # string.strip()截掉 string 左右两边的空白字符
print("*" * 50)
print(str18.lstrip().strip().rstrip())  # 推展·多重调用 （举个例子，不要在意函数是啥）哈哈哈

# 拆分字符串，将字符串转换为列表，并去掉空白字符
str19_list = str19.split()  # 用.split()来拆分字符串，sep为分割符号，默认为所以空白字符，第二个是分割限制，默认为-1无限制，可以用变量接收
print(str19_list)
# 合并字符串
str19_str = "+".join(str19_list)  # 用“+”来合并字符串，用.join()函数，.join函数只有在两个及以上时才会插入拼接
print(str19_str)

# 字符串的切片
q_str20 = str20[0: 3: 1]  # 定义一个变量来存储值，用中括号来切片，第一个为起始，第二个是结束，左闭右开区间，第三个为步长，每取个值走几步
print(q_str20)
q_str20 = str20[0:: 1]  # 若不指定右边区间，默认切完
print(q_str20)
q_str20 = str20[:5: 2]  # 若不指定左边区间，默认从头开始
print(q_str20)
qp_str20 = str20[-5: -1: 1]  # 倒序，倒着数，但还是正着切，负一为最右，步数为2
print(qp_str20)
qp_str20 = str20[-1: -5: -1]  # 倒序，正着数，但还是倒着切，负一为最右，步数为-1，从左边开始数
print(qp_str20)
qp_str20 = str20[:: 1]  # 正序，不指定默认全切
print(qp_str20)
qp_str20 = str20[:: -1]  # 倒序，不指定默认全切
print(qp_str20)



























