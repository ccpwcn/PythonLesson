import _thread
import time


def thread_proc():
    for i in range(1, 10):
        print(i)
        time.sleep(1)


_thread.start_new_thread(thread_proc, ())
print('sleep')
time.sleep(5)

# 这段代码只会输出1到5，原因是主线程在休眠5秒之后退出了，主线程退出，整个程序都会退出
