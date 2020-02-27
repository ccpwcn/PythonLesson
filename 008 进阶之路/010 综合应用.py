# 综合应用
# 求一个字符串列表的总字符数长度
# 需要同时用到map和reduce，先使用map逐项求取每一项的长度，再传给reduce进行累加即可

from functools import reduce

language = ['Python', 'C++', 'JavaScript', 'Java', 'Ruby']

total_len = reduce(lambda n1, n2: n1 + n2, map(lambda item: len(item), language))
print(total_len)

len_sum = 0
for lan in language:
    len_sum += len(lan)
print(len_sum)
