import socket


def main():
    """服务器"""
    # 建立服务器客户端
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定服务器地址
    tcp_socket.bind(("192.168.131.149", 7890))
    # 设为监听状态
    tcp_socket.listen(5)  # 只允许5个连接等待
    # 等待客户端连接
    print("Waiting for connection...")
    server_client, client_address = tcp_socket.accept()
    print(client_address, "Connection successful!")
    # 接收消息
    receive_file_name = server_client.recv(1024)
    # 发送数据
    with open(r"./test.txt", "rb") as f:
        file_data = f.read()
        server_client.send(file_data)
    print("数据传输成功！")
    # 退出服务客户端
    server_client.close()
    # 退出服务器
    tcp_socket.close()


if __name__ == "__main__":
    main()
