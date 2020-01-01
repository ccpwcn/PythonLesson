from functools import reduce

numbers = []
for i in range(1, 101):
    numbers.append(i)
sum = reduce(lambda x, y: x + y, numbers)
print(sum)
