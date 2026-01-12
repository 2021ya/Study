import socket
import threading
import queue
import time


def scan(ip, q):
    while True:
        # 判断队列是否为空
        if q.empty():
            break
        # 不为空扫描端口
        port = q.get()
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 每次扫描都独立一个socket
            s.settimeout(1)  # 超时最大时间
            # print("Trying TCP connection to " + ip + ":" + str(port))
            s.connect((ip, port))
            print("Port {} open!".format(port))
            s.close()
        except ConnectionRefusedError:
            # print("Port " + str(port) + " is not available")
            pass
        except PermissionError:
            print("Port {} Insufficient permissions!".format(port))
        except TimeoutError:
            pass


def progress(q, port_range):
    """进度显示"""
    start_time = time.time()
    # 进度条
    while True:
        print("\r\033[0m剩余扫描端口占比:[\033[32m%.2f%%\033[0m]" % ((q.qsize() / len(port_range)) * 100), end="")
        time.sleep(0.01)
        if q.qsize() / len(port_range) == 0:
            print("\r\033[0m剩余扫描端口占比:[\033[32m0.00%\033[0m]", end="")
            break
    end_time = time.time()
    print()
    print("Time Taken: {}".format(end_time - start_time))


def main():
    # 创建任务队列
    q = queue.Queue()
    # 扫描ip
    ip = input("Ip Address: ")
    # 端口范围
    port_range = range(int(input("Port Start Range: ")), (int(input("Port Stop Range: ")) + 1))
    # 将端口放入队列
    for port in port_range:
        q.put(port)
    # 手动输入需要线程数
    thread_num = int(input("Number of threads: "))
    # 创建线程
    progress_thread = threading.Thread(target=progress, args=(q, port_range))
    progress_thread.start()
    print()
    # 扫描线程初始化
    print("Scan Init Thread...")
    for thread in range(0, thread_num):
        t = threading.Thread(target=scan, kwargs={"ip": ip, 'q': q})
        t.start()
        # print("Scan Thread {} Init Successfully!".format(t))
        # t.join()  # 此处会堵塞主线程
    # print("All Threads Init successfully!")


if __name__ == '__main__':
    main()





















