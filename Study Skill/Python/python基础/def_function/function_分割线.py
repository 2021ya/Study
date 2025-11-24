def print_line(character, times, line):
    """打印多行分隔符
    :param character: 分隔符字符
    :param times: 字符数
    :param line: 行数
    """
    i = 1

    while i <= line:
        print(("%s" % character) * times)
        i += 1


name = "2021"
