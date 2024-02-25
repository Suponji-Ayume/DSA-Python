# 采用动态规划算法
# sum[i] 表示从第一个数开始，加到索引为 i 的数的和
# 子区间[i,j]的和可以表示成 sum[j] - sum[i - 1]

# t = int(input())
# for _ in range(t):
#     n, hate = map(int, input().split())
#     nums = list(map(int, input().split()))
#     max_length = -1
#
#     # 前缀和 sum 数组
#     sum = []
#     sum.append(nums[0])
#     for i in range(1, n):
#         sum.append(sum[i - 1] + nums[i])
#
#     # 循环求每一个子数组的和
#     for i in range(n):
#         for j in range(i, n):
#             if i == 0:
#                 if j == 0:
#                     sub_sum = sum[0]
#                 else:
#                     sub_sum = sum[j]
#             else:
#                 sub_sum = sum[j] - sum[i - 1]
#             if sub_sum % hate != 0:
#                 max_length = max(max_length, j - i + 1)
#     print(max_length)

# 这 TM 是个数学题
# 如果给的每个数组都是 hate 的倍数，那么任意子区间都是 hate 的倍数，返回 -1
# 如果给的数组之和不是 hate 的倍数，那么直接返回 len(nums)
# 如果数组之和是 hate 的倍数，那么分别找到从左向右数第一个不是 hate 倍数的数的索引 x，以及从右向左第一个不是 hate 倍数的数的索引 y
# 然后比较 n - (x + 1) 和 y，返回较大的那个

t = int(input())

for _ in range(t):
    n, hate = map(int, input().split())
    nums = list(map(int, input().split()))
    # 如果数组的和不是 hate 的倍数，直接返回 n
    if sum(nums) % hate != 0:
        print(n)
    else:
        # x 为第一个不是 hate 倍数的索引，y 是最后一个不是 hate 倍数的索引
        x, y = -1, -1
        # 判断是否都是 hate 的倍数，如果都是，则直接返回 -1
        for i in range(n):
            if nums[i] % hate != 0:
                x = i
                break
            else:
                continue
        # 如果数组中全都是 x 的倍数，即 x 没有改动过，x == -1
        if x == -1:
            print(-1)
        # 从后往前找到最后一个不是 hate 倍数的索引
        else:
            for i in range(n - 1,-1,-1):
                if nums[i] % hate != 0:
                    y = i
                    break
            max_length = max(n - x - 1, y)
            print(max_length)
