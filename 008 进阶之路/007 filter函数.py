# 简单地

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(new_numbers))
