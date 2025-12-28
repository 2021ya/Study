import socket
import threading
import time


class Server(threading.Thread):

    def __init__(self, server_socket, ip, port):
        super().__init__()
        self.server_socket = server_socket
        self.ip = ip
        self.port = port

    def run(self):
        # self.server_socket.send(b"Hello, Client!")
        while True:
            recv_data = self.server_socket.recv(1024)
            if recv_data:
                print("From {} massages:".format(self.ip), recv_data.decode("utf-8"))
                self.server_socket.send(recv_data)  # 转发消息-----此处转回原处
            else:
                print("Client disconnected")
                self.server_socket.close()  # 若发来空消息（证明客户端关闭了连接），那么服务器断开连接
                break  # 既然断开连接，就退出循环


class TCPServer(threading.Thread):

    # 初始化服务器
    def __init__(self, port):
        super().__init__()  # 继承父类初始化
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建套接字
        self.tcp_socket.bind(('', port))  # 绑定服务器端口
        self.tcp_socket.listen(128)  # 将服务器设为监听状态

    def run(self):
        while True:
            server_client, client_info = self.tcp_socket.accept()  # 等待客户端连接
            # 若有新连接，创新新子线程来为客户端服务，服务器继续等待
            # 创建子线程为客户端服务
            server = Server(server_client, client_info[0], int(client_info[1]))
            server.start()
            print(">>>", client_info, "connected")

    def __del__(self):
        self.tcp_socket.close()  # 关闭服务器
        print("TCP Server closed!")


# 启动服务器
if __name__ == '__main__':
    tcpserver = TCPServer(7890)
    tcpserver.start()
    print("TCP Server Started!")
    while True:
        time.sleep(1)  # TODO-----bug!!!
        """
        保持主线程活跃，此处有问题，正常来说主线程应该等待子线程执行完毕再进行关闭，但是此处不会
        如果主线程执行完毕，会正常等待子线程，但是只要一有连接进来，那么程序直接崩溃，报错是无法
        在解释器关闭时创建线程，所以为了保持主线程活跃，那么只能将主线程循环
        """



