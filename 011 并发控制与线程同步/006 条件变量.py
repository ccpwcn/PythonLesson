# coding=utf-8
import random
import threading
import time

con = threading.Condition()


# 生产者
class Producer(threading.Thread):

    def __init__(self, total_bowl):
        threading.Thread.__init__(self)
        self.total_bowl = total_bowl

    def run(self):
        # 锁定线程
        con.acquire()
        while self.total_bowl > 0:
            print("[P] 开始做饭。。。")
            time.sleep(random.randint(1, 5))
            print("[P] 饭做好了！！！")
            # 唤醒等待的线程
            con.notify()  # 唤醒小伙伴开吃啦
            # 等待通知
            con.wait()
            # 得知消费者已经吃完了
            print("[P] 做好了一碗")
            self.total_bowl -= 1
        # 唤醒其它线程
        con.notify()
        con.release()


# 消费者
class Consumers(threading.Thread):
    def __init__(self, total_bowl):
        threading.Thread.__init__(self)
        self.total_bowl = total_bowl

    def run(self):
        con.acquire()
        while self.total_bowl > 0:
            print("[C] 开始吃饭。。。")
            time.sleep(random.randint(1, 5))
            print("[C] 饭吃完了！！！")
            # 唤醒其它线程
            con.notify()
            # 等待通知
            con.wait()
            # 得知生产者已经做好饭了
            print("[C] 吃完了一碗")
            self.total_bowl -= 1
        # 唤醒其它线程
        con.notify()
        con.release()


total_bowl = 3
p = Producer(total_bowl)
c = Consumers(total_bowl)
p.start()
c.start()
p.join()
c.join()
