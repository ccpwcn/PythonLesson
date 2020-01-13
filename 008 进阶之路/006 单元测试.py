import unittest


def add(n1, n2):
    return n1 + n2


class MyAdd(unittest.TestCase):
    """
    要点：
        1、继承unittest.TestCase类
        2、测试方法要以test_开头
    """

    def setUp(self) -> None:
        self.list1 = [1, 2, 3, 4, 5]
        self.list2 = [5, 4, 3, 2, 1]
        print('ready')

    def test_add(self):
        for i in range(len(self.list1)):
            self.assertEqual(add(self.list1[i], self.list2[i]), 6)

    def tearDown(self) -> None:
        print('down')


if __name__ == '__main__':
    unittest.main()

