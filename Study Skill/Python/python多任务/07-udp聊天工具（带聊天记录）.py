import socket
import sys
import threading
import queue
import time


class SendMassage(threading.Thread):
    """发送消息"""
    def __init__(self, udp_socket, fifo_q, host_ip):
        super().__init__()
        self.udp_socket = udp_socket
        self.fifo_q = fifo_q
        self.host_ip = host_ip

    def run(self):
        while True:
            dest_ip = input("Dest IP:")
            # 退出程序
            if dest_ip == "exit sys":
                sys.exit()
            # 端口检查
            dest_port = None
            try:
                dest_port = int(input("Dest Port:"))
            except Exception as e:
                print(e)
            # 发送消息
            while True:
                massage = input("Massage:")
                if massage:
                    self.udp_socket.sendto(massage.encode("utf-8"), (dest_ip, dest_port))
                    self.fifo_q.put("From {}:{} to {}:{} :{}".format(self.host_ip, 7890, dest_ip, dest_port, massage))  # 将消息存入队列
                    print("From {}:{} to {}:{} :{}".format(self.host_ip, 7890, dest_ip, dest_port, massage))  # .gethostbyname获取本地ipv4地址
                else:
                    break


class ReceiveMassage(threading.Thread):
    """接收消息"""
    def __init__(self, udp_socket, fifo_q, host_ip):
        super().__init__()
        self.udp_socket = udp_socket
        self.fifo_q = fifo_q
        self.host_ip = host_ip

    def run(self):
        while True:
            # 接收数据
            receive_data = self.udp_socket.recvfrom(1024)
            # 解析消息
            massage = receive_data[0].decode("utf-8")
            src_ip = receive_data[1][0]
            src_port = int(receive_data[1][1])
            # 输出消息
            self.fifo_q.put("From {}:{} to {}:{} :{}".format(src_ip, src_port, self.host_ip, 7890, massage))
            print("From {}:{} to {}:{} :{}".format(src_ip, src_port, self.host_ip, 7890, massage))


class FileQueue(threading.Thread):
    """文件队列"""

    def __init__(self, fifo_q):
        super().__init__()
        self.fifo_q = fifo_q

    def run(self):
        """负责保存聊天记录"""
        while True:
            try:
                history = open(r"./history.log", "a")
                history.write(self.fifo_q.get() + "\n")
                history.close()
            except Exception as e:
                print(e)


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定本地配置
    host_port = None
    host_port = input("Bind Localhost Port:")
    try:
        host_port = int(host_port)
    except Exception as e:
        print(e)
    udp_socket.bind(('', host_port))
    # 获取主机名称
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    # 创建队列
    fifo_q = queue.Queue()
    # 创建线程（发送，接收，写入）
    send_massage = SendMassage(udp_socket, fifo_q, host_ip)
    receive_massage = ReceiveMassage(udp_socket, fifo_q, host_ip)
    file_queue = FileQueue(fifo_q)
    # 启动线程
    send_massage.start()
    receive_massage.start()
    file_queue.start()
    while True:
        # 主线程循环等待
        time.sleep(5)


if __name__ == "__main__":
    main()
