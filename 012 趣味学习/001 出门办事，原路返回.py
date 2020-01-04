# 任务描述：
# 1、去楼下花园找王大爷，取3元钱
# 2、去小区门口的包子店买3个现蒸的肉包子
# 3、去小区外马路对面快递公司去快递
# 4、将肉包子送给王大爷
# 解决思路：
#     栈


class Task(object):
    steps = []

    def forward(self, location, desc):
        if not self.steps:
            print('即将行动，从家里出发')
        self.steps.append((location, desc))
        print('【前进】所在位置：{}，任务：{}'.format(location, desc))

    def back(self, what):
        if not self.steps:
            print('全部完成')
        else:
            just = self.steps.pop()
            if not self.steps:
                print('【后退】刚才位置：{}，完成：{}，到达：{}，将要：{}'.format(just[0], just[1], '家', '缴旨'))
            else:
                next = self.steps[-1]
                print('【后退】刚才位置：{}，完成：{}，到达：{}，事由：{}，将要：{}'.format(just[0], just[1], next[0], next[1], what))


if __name__ == '__main__':
    t = Task()
    t.forward('楼下花园', '找王大爷取3元钱')
    t.forward('包子店', '告诉老板把肉包子现在蒸上，5分钟之后来取')
    t.forward('快递公司', '取快递')
    t.back('取包子')
    t.back('送包子')
    t.back('回家')
    t.back('？')

