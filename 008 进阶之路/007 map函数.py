names = ['a.txt', 'b.txt', 'c.txt', 'd.txt']
print(names)
for name in names:
    print(name)

# 给每个成员后面加一个换行
m = map(lambda x: x + '\n', names)
print(m)  # 会得到一个map对象
print(list(m))  # 转为list输出


numbers = [1, 2, 3, 4, 5]
# 给所有成员乘2
m = map(lambda x: x * 2, numbers)
print(list(m))


# 来个稍微复杂点的，给数列中的偶数乘2，其余保持不变
# 逻辑复杂一点的时候，写lambda表达式会导致代码可读性很差，写成函数更好
def increment(n):
    if n % 2 is 0:
        return n * 2
    else:
        return n
m = map(increment, numbers)
print(list(m))