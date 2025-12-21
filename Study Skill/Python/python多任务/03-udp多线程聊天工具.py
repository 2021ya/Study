import socket
import threading


def send_massage(udp_socket, address, port):
    while True:
        massage = input("massage：")
        if massage:
            udp_socket.sendto(massage.encode('utf-8'), (address, port))
        # else:
        #     break


def recv_massage(udp_socket):
    while True:
        data = udp_socket.recvfrom(1024)
        print("src:", data)
        print(">>>from {} massage:".format(data[1]), data[0].decode('utf-8'))


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定本地端口
    udp_socket.bind(("", 7890))  # udp要实现收发数据需要绑定端口
    # 获取对方address和port
    address = input("address:")
    port = int(input("port:"))
    # 创建线程
    send_massage_thread = threading.Thread(target=send_massage, args=(udp_socket, address, port))
    recv_massage_thread = threading.Thread(target=recv_massage, args=(udp_socket,))
    send_massage_thread.start()
    recv_massage_thread.start()


if __name__ == '__main__':
    main()
