# 形参与实参
# n1和n2就是形参
def add(n1, n2):
    return n1 + n2
# 数字1和2分别会传给n1和n2，数字1和数字2是实参
r = add(1, 2)
print(r)


# 命名参数
def out(name):
    print('hello ' + name)
out(name='world')  # 此时字符串world是个命名参数
def out(a=1, b=2):
    print(a + b)
out(a=2, b=3)
out(b=3, a=2)


# 默认参数，也称可选参数
def out(name='world'):
    print('hello ' + name)
out()
out(name='xiao wang')

# 关键字参数
def total(factor, **kw):
    r = 0
    if 'k' in kw:
        r = factor * 2
    elif 'j' in kw:
        r = factor * 3
    else:
        r += factor
    print(r)
total(2)
total(2, k=2)
total(2, j=3)


