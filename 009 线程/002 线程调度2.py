import threading
import time


class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self) -> None:
        for i in range(1, 10):
            print(i)
            time.sleep(1)


# 创建线程实例
t = MyThread()   # 此时线程不会执行
t.start()        # 此时线程开始执行
t.join()         # 主线程等待子线程t执行完毕

