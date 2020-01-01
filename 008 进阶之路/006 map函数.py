names = ['a.txt', 'b.txt', 'c.txt', 'd.txt']
print(names)
for name in names:
    print(name)

m = map(lambda x: x + '\n', names)
print(m)  # 会得到一个map对象

l = list(m)
print(l)

