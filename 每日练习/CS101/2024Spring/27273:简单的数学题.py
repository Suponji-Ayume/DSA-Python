from math import *


# 找到不大于 n 的最大 2 的幂指数
def find_largest_power(n):
    return floor(log2(n))


# 给定最高幂指数，计算 2 的幂次和
def sum_2_power(n):
    return 2 ** (n + 1) - 1


# 计算从 1 到 n 的高斯和
def Gaussian_Sum(n):
    return (1 + n) * n // 2


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        result = Gaussian_Sum(n) - 2 * sum_2_power(find_largest_power(n))
        print(result)
