# 信号号的线程同步方式，在并发模型中具有重要意义，此处做一个示例：秒杀抢购
import _thread
import threading
import time


class Goods(object):
    """商品类"""

    def __init__(self, total):
        self.total = total  # 商品创建时指定一个库存

    def buy(self, buyer):
        if self.total > 0:
            self.total -= 1
            print('{} had it'.format(buyer))
        else:
            print('nothing, {} buy failed'.format(buyer))


def thread_proc(semaphore, s, goods):
    semaphore.acquire()  # 等待信号
    goods.buy(s)  # 抢购
    print('thread {} going done'.format(s))


# 预置信号号为0，所有线程都会阻塞
semaphore = threading.Semaphore(value=3)
# 假定商品只有2个库存了
goods = Goods(total=2)
_thread.start_new_thread(thread_proc, (semaphore, 'one', goods))
_thread.start_new_thread(thread_proc, (semaphore, 'two', goods))
_thread.start_new_thread(thread_proc, (semaphore, 'three', goods))
# 发信号，让所有线程开始抢
semaphore.release()
time.sleep(3)
# 查看库存是否为0，为0就是对的，否则就说明抢购出现bug了，抢购的基本要求是：无论如何都不能多卖
print(goods.total)
