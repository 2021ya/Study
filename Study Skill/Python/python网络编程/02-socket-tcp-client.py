import socket


def main():
    # 创建tcp client套接字
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 链接server
    server_address = (input("Enter IP Address:"), int(input("Enter Server Port:")))
    tcp_client.connect(server_address)
    print("链接服务器成功！")
    # 发送数据
    send_data = input("Enter Data:")
    tcp_client.send(send_data.encode("utf-8"))
    # 关闭套接字
    tcp_client.close()
    print("服务器已断开！")


if __name__ == '__main__':
    main()
