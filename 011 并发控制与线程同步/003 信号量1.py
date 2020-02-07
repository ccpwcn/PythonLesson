# 信号号的线程同步方式，在并发模型中具有重要意义，此处做一个并发抢购示例
import threading


class Goods(object):
    """商品类"""
    def __init__(self, total):
        self.total = total   # 商品创建时指定一个库存

    def buy(self, buyer):
        if self.total > 0:
            self.total -= 1
            print('{} had it'.format(buyer))
        else:
            print('nothing, {} buy failed'.format(buyer))


class MyThread(threading.Thread):
    def __init__(self, semaphore, s, goods):
        super().__init__()
        self.semaphore = semaphore
        self.s = s
        self.goods = goods

    def run(self):
        self.semaphore.acquire()  # 等待信号
        self.goods.buy(self.s)    # 抢购
        print('thread {} going done'.format(self.s))


# 预置信号号为0，所有线程都会阻塞
semaphore = threading.Semaphore(value=3)
# 假定商品只有2个库存了
goods = Goods(total=2)
threads = [
    MyThread(semaphore, 'one', goods),
    MyThread(semaphore, 'two', goods),
    MyThread(semaphore, 'three', goods),
]
# 启动这3个线程
for t in threads:
    t.start()
# 发信号，让所有线程开始抢
semaphore.release()
# 等待所有线程结束
for t in threads:
    t.join()
# 判断库存是否为0，为0就是对的，否则就说明抢购出现bug了，抢购的基本要求是：无论如何都不能多卖
assert goods.total == 0
print('完成')
