# 捕获异常
import random

try:
    a = 1
    b = 0
    n = a / b
except Exception as e:
    print(e)

# 手动抛出异常
score = random.randint(1, 100)
if score < 60:
    msg = '分数{}被判断为不及格'.format(score)
    raise Exception(msg)


# 还可以手动抛出其他异常
def calc(a, op, b):
    if not (isinstance(a, int) or not isinstance(a, float)):
        raise ValueError('参数a只能是数值，不能是其他类型')
    if not (isinstance(b, int) or not isinstance(b, float)):
        raise ValueError('参数b只能是数值，不能是其他类型')
    if op is '+':
        return a + b
    elif op is '-':
        return a - b
    elif op is '*':
        return a * b
    elif op is '/':
        return a / b
    else:
        raise ArithmeticError('不支持的运算符')


print(calc(1, '+', 2))
print(calc(1, '<', 2))
