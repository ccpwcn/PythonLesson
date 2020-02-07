# 全局变量进行并发控制和线程同步，是最简单的方法
import _thread
import time

flag = 0


def thread_proc(s, n):
    global flag
    while flag is 0:
        time.sleep(1)
    print('thread {}/{} going done'.format(s, n))


_thread.start_new_thread(thread_proc, ('one', 1))
_thread.start_new_thread(thread_proc, ('two', 2))
_thread.start_new_thread(thread_proc, ('three', 3))
time.sleep(2)
print('set start flag')
flag = 1
time.sleep(5)
print('all done')
