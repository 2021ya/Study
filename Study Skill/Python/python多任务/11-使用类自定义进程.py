import time
import multiprocessing


class MyProcess(multiprocessing.Process):

    def __init__(self, args):  # 传参同理
        super().__init__()
        pass

    def run(self):
        while True:
            print("我是子进程")
            time.sleep(1)


if __name__ == '__main__':
    process = MyProcess(args=args)  # 传参同理
    process.start()
    while True:
        print("我是主进程")
        time.sleep(1)

