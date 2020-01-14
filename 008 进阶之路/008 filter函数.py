numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 筛选出偶数
new_numbers = filter(lambda x: x % 2 is 0, numbers)
print(list(new_numbers))

# 筛选出大于5的偶数
def larger(n):
    return n > 5 and n % 2 is 0
new_numbers = filter(larger, numbers)
print(list(new_numbers))

# 筛选出3的倍数
new_numbers = filter(lambda x: x % 3 is 0, numbers)
print(list(new_numbers))

