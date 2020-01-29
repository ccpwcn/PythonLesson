# 协程一般用在并发量比较大的时候使用，因为并发量比较大的情况下，使用线程开销太大，协程是不错的选择。

# Python原生的协程实现太麻烦，而且是通过yield提供了对协程的基本支持，还不完全。而第三方的gevent为Python提供了比较完善的协程支持。
# 运行本代码之前，需要使用pip命令安装gevent，安装指令也很简单，直接执行pip install gevent即可。


# 导入gevent库
from gevent import monkey

monkey.patch_socket()

import gevent


# 定义运行函数
def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)


# 启动协和，第一个参数是运行函数，第二个参数开始是运行函数的参数，有多个的时候按顺序写上就可以了
g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
# 等待协和结束，和其他程序一样，如果子线程/协程没有结束，主线程却退出了，整个程序就结束了。
g1.join()
g2.join()
g3.join()
