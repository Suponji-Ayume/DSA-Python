str = input()

# 先转换成小写字母
str = str.lower()

# 去掉元音字母
str = str.replace('a', '')
str = str.replace('e', '')
str = str.replace('i', '')
str = str.replace('o', '')
str = str.replace('u', '')
str = str.replace('y', '')

# 在每个辅音字母前加上'.'
str = '.'.join(str)
# 记得在最前面也要加上'.'
str = '.' + str

# 输出结果
print(str)