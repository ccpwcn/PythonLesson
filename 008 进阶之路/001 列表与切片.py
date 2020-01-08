numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 遍历
# for n in numbers:
#     print(n)

# 添加
numbers.append(11)
print(numbers)
numbers.append('a')  # 可以添加不同类型的数据
print(numbers)

# 删除
numbers.pop()  # 删除最后一个
numbers.pop(1) # 删除指定索引位，后面的数据会往前移动
print(numbers)

# 修改
numbers[2] = 100
print(numbers)

# 切片：无论下标是正数还是负数，都是从0开始，正数从左至右，使用右开区间，负数从右至左，使用左开区间
# 即：n:m，如果n和m都是正数，切片区间为右开区间：[n,m)，如果n和m都是负数，切片区间为左开区间：(n,m]
print('3:    ==>', numbers[3:])  # 取下标为3的及之后的所有数据
print(':3    ==>', numbers[:3])  # 取下标为3的之前的数据
print(':-3   ==>', numbers[:-3])  # 取下标为-3的及之前的所有数据
print('2:5   ==>', numbers[2:5])  # 取下标为2的及其到下标为5的所有数据，不含下标为5的数据，右开区间
print('-3:-1 ==>', numbers[-3:-1])  # 取下标为-3到下标为-1之间的数据，不含下标为-3的数据，左开区间
