a = int(input())
# 用来存八进制的每一位
bits = []
# 利用短除法
while a != 0:
    bits.append(str(a % 8))
    a //= 8
print(''.join(bits[::-1]))