# 由于协程切换是在IO操作时自动完成，所以gevent需要修改Python自带的一些标准库，这一过程在启动时通过monkey patch完成
from functools import reduce
from gevent import monkey
import datetime

monkey.patch_all()
import gevent
# requests是一个功能强大又十分流行的网络请求库，和之前的gevent一样，使用pip命令安装即可
import requests

def task(url, results):
    """任务"""
    start = datetime.datetime.now()
    resp = requests.get(url)  # 这里对响应没有做处理，我们可以自己根据需求再处理一下的
    end = datetime.datetime.now()
    results.append((end - start).microseconds / 1000)


# 本例中，需要等待多个协程全部返回，所以要使用joinall，并且依据您的网络速度，它们执行完成的顺序是不确定的。
results = []
tasks = []
for i in range(0, 10, 1):
    tasks.append(gevent.spawn(task, 'https://www.baidu.com/', results))
gevent.joinall(tasks)
print(results)


def up(x, y):
    """求平均值的函数"""
    if not x:
        return y
    elif not y:
        return x
    else:
        return x + y
# 求平均值
avg = reduce(up, results) / len(results)
print(avg)
