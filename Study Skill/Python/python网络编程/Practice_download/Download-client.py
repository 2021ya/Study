import socket


def main():
    """客户端-两边都是同一个协议才可通信"""
    # 建立连接
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接服务器
    tcp_socket.connect(("192.168.131.149", 7890))
    while True:
        # 给服务器发送文件名
        file_name = input("请输入要下载的文件（退出/exit）：")
        if file_name == "exit":
            break
        tcp_socket.send(file_name.encode("utf-8"))
        # 接收数据
        with open(r"./{}.txt".format(file_name), "wb") as f:  # wb以二进制打开文件
            receive_data = tcp_socket.recv(1024*1024)  # 1MB数据
            try:
                f.write(receive_data)
                print("下载完成！")
            except Exception as e:
                print("文件下载失败：{}".format(e))
    # 退出客户端
    tcp_socket.close()


if __name__ == '__main__':
    main()
