import socket


def main():
    # 创建udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    """
    变量接收，第一个是地址族，AF_INET为ipv4，后面加6就是ipv6了，第二个参数为协议SOCK_DGRAM为udp协议,SOCK_STREAM为TCP协议了
    AF_INET + SOCK_RAW,原始IP包,构造自定义数据包、ARP欺骗、嗅探
    """
    # 使用udp套接字
    # udp_socket.sendto(b"Information", ("192.168.26.149", 8080))
    """
    发送的信息只能是字节类型bytes;前面加上b表示用字节存储
    """
    print("发送数据中(exit)")
    # 绑定此程序ip和端口
    udp_socket.bind(('', 9999))  # 若不绑定端口，那么系统会随机分配
    while True:
        send_data = input("send：")
        if send_data == "exit":
            break
        udp_socket.sendto(send_data.encode("utf-8"), ("192.168.26.149", 8080))  # .encode()改变编码格式
        """
        第一个为发送的信息，第二个为发送地址和端口（元组）
        """
    # 关闭套接字
    udp_socket.close()

    # 接收数据演示
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定端口
    udp_socket.bind(("", 7788))  # 使用元组来记录接收的地址和端口,若ip为空，那么就是本地随便一个ip都可以
    print("接收数据")
    # 接受数据
    i = 0
    while True:
        recvfrom_data = udp_socket.recvfrom(1024)  # 最大接收数据的大小--此处会一直循环直到接收数据--此数据为元组包括信息和发送方信息
        # 打印数据
        recvdata = recvfrom_data[0]
        print("数据包：", recvfrom_data)
        print("原信息：", recvdata)
        print("解码信息：", recvdata.decode("utf-8"))  # 解码.decode()
        i += 1
        print("当前接受数据({}/5):{}".format(i, i))
        if i == 5:
            break
    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
