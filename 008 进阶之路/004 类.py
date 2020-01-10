# 类定义
class People(object):
    name = None
    age = None

    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def __str__(self):
        return 'name=' + self.name + ', age=' + str(self.age)


p = People(name='wang', age=18)
print(p)


# 类继承
class Student(People):
    location = None

    def __init__(self, name=None, age=None):
        super().__init__(name, age)

    def __str__(self):
        return 'name=' + self.name + ', age=' + str(self.age) + ', location=' + self.location


# 类实例化
stu = Student(name='zhang', age=11)
stu.location = '北京市'
print(stu.location)
print(stu)


# 类实例在函数中的使用
def change(stu):
    stu.location = '上海'


change(stu)
print(stu)