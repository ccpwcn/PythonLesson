def add(n1, n2):
    return n1 + n2
print(add(1, 2))

def add(n1, n2):
    n1 + n2
print(add(1, 2))

# 多个返回值
def some():
    return 1, 2, 3
print(some())

# 没有明确返回值的函数
def p(n):
    print(n)
r = p(10)
print(r)

