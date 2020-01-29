# 由于协程切换是在IO操作时自动完成，所以gevent需要修改Python自带的一些标准库，这一过程在启动时通过monkey patch完成
from gevent import monkey

monkey.patch_all()
import gevent
# requests是一个功能强大又十分流行的网络请求库，和之前的gevent一样，使用pip命令安装即可。
import requests


def f(url):
    print('GET: %s' % url)
    resp = requests.get(url)
    data = resp.text
    print('%d bytes received from %s.' % (len(data), url))


# 本例中，需要等待多个协程全部返回，所以要使用joinall，并且依据您的网络速度，它们执行完成的顺序是不确定的。
gevent.joinall([
    gevent.spawn(f, 'https://www.baidu.com/'),
    gevent.spawn(f, 'https://www.163.com/'),
    gevent.spawn(f, 'https://www.qq.com/'),
])