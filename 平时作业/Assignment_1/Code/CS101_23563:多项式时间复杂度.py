str = input()
str_list = list(str.split('+'))

# 用于存储指数
index_list = []

# 遍历每一项
for item in str_list:
    # 找到每一项中的 ^ 符号
    if '^' in item:
        # 分割出指数
        base, index = item.split('^')
        # 判断系数是否是 0
        base = base[:-1]
        if base == '0':
            continue
        # 转换成数字
        index = int(index)
        # 存储指数
        index_list.append(index)
    else:
        # 如果没有 ^ 符号，判断是否有 n
        if 'n' in item:
            # 如果有 n，指数为 1
            index_list.append(1)
        else:
            # 如果没有 n，指数为 0
            index_list.append(0)

# 指数降序排序
index_list.sort(reverse=True)

# 输出最大指数
print(f'n^{index_list[0]}')
