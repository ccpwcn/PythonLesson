import random


def total1(n1, n2):
    return n1 + n2


total2 = lambda n1, n2: n1 + n2


for i in range(1, 5):
    n1 = random.randint(1, 10)
    n2 = random.randint(1, 10)
    choice = random.randint(0, 3)
    if choice is 0:
        print('FUNCTION {} + {} = {}'.format(n1, n2, total1(n1, n2)))
    elif choice is 1:
        print('LAMBDA {} + {} = {}'.format(n1, n2, total2(n1, n2)))
    else:
        print('what???')
