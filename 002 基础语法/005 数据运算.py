# 加
print(1 + 1)
# 减
print(1 - 1)
# 乘
print(2 * 2)
# 除
print(10 / 3)
# 小数/浮点数
print(1 / 5)
# 整除
print(10 / 5)
# 取余/取模
print(10 % 6)
# 手动控制运算优先级
print(10 * (2 - 2))

# is not
print(not True)
print(not False)
print(1 is 1)
print('表达式与常量：', 2 is 4 / 2)  # 2是个对象，4/2也是个对象，一个是数值对象，一个是表达式，它们是不一样的
print('表达式与表达式1：', 2 / 1 is 4 / 2)  # 2/1是个表达式，4/2也是个表达式
print('表达式与表达式2：', 2 / 1 is 6 / 2)  # 虽然2/1是个表达式，6/2也是个表达式，但是它们结果不相同，所以是False

# 复数
a = 3 + 2j
b = 2 + 5j
# 复数求和
print(a + b)
# 共轭复数
print('共轭复数：', a.conjugate())