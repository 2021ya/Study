import socket


def main():
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定服务器端口
    tcp_server_socket.bind(("192.168.131.149", 7890))
    # 将套接字设置为监听模式-----为等待链接
    tcp_server_socket.listen(128)

    while True:
        # 等待接收客户端消息
        print("等待客户端链接...")
        server_client, client_address = tcp_server_socket.accept()  # 第一个为接待客户端的客户端，第二个为链接到此服务器的客户端地址
        print("{}链接成功".format(client_address))
        while True:
            # 接收客户端消息
            recv_data = server_client.recv(1024)
            print("来自{}的消息：".format(client_address), recv_data.decode("utf-8"))
            if recv_data:  # 只要发过来数据，那么就会回复
                # 回复客户端消息
                send_data = "服务器已收到消息！"
                server_client.send(send_data.encode("utf-8"))
            else:  # 若客户端中断连接，那么会发来空数据，那么就断开（客户端不可主动发送空数据，只有中断连接的时候才会传过空数据）
                send_data = "与服务器断开连接..."  # 因为客户端主动断开连接，理论上这句话发不过去了
                server_client.send(send_data.encode("utf-8"))
                break
        # 关闭接待客户端
        print("{}:断开连接...".format(client_address))
        server_client.close()
        # break
        # 关闭服务器
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
