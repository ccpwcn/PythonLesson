import _thread


def thread_proc():
    for i in range(1, 10):
        print(i)


_thread.start_new_thread(thread_proc, ())

# 上述代码不会有任何输出，原因是程序启动的时候，都会有一个主线程，主线程执行完第9行代码之后，会立即退出
# 线程函数thread_proc并没有机会执行
