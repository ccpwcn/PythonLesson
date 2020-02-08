# 忙等待是多线程编程的一个常见错误，a线程一直在等待b线程执行完成，但是b线程因为各种原因从未释放CPU执行时间，于是a线程始终得不到机会执行
import threading
import time


class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        print('MyThread running...')
        while True:
            time.sleep(1)


t = MyThread()
t.start()
t.join()
print('all done')

