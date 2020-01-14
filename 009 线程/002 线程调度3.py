import threading
import time


class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self) -> None:
        i = 0
        while True:
            i += 1
            print(i)
            time.sleep(1)


# 创建线程实例
t = MyThread()   # 此时线程不会执行
t.start()        # 此时线程开始执行
t.join(timeout=7)         # 主线程等待子线程t执行完毕，最多等待7秒
print('all done')

# 打印all done之后，子线程并不会结束，只是主线程不会再等待子线程。
