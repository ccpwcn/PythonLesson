from functools import reduce

numbers = []
for i in range(1, 101):
    numbers.append(i)
# 1到100累加求和
total = reduce(lambda x, y: x + y, numbers)
print(total)


# 复杂点的：对numbers中的大于等于60的数字求平均值
# 第一次：x是None，y是第一个数，最后一次：x是最后一个数，y是None
def up(x, y):
    if not x:
        if y >= 60:
            return y
    elif not y:
        if x >= 60:
            return x
    elif x >= 60 and y >= 60:
        return x + y
avg = reduce(up, numbers) / 40
print(avg)
# 验证一下结果对不对
t = 0
for i in range(60, 101, 1):
    t += i
print(avg == t / 40)
