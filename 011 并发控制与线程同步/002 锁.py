# 相比全局变量，锁的方式控制线程同步，代码更优雅、性能更高、系统开销更少、线程控制更精准
import threading


class MyThread(threading.Thread):
    def __init__(self, lock, s, n):
        super().__init__()
        self.lock = lock
        self.s = s
        self.n = n

    def run(self):
        self.lock.acquire()
        try:
            print('thread {}/{} going done'.format(self.s, self.n))
        finally:
            self.lock.release()


lock = threading.Lock()
threads = [
    MyThread(lock, 'one', 1),
    MyThread(lock, 'two', 2),
    MyThread(lock, 'three', 3),
]
for t in threads:
    t.start()
for t in threads:
    t.join()
print('all done')

