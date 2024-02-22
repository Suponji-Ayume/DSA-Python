# 修改操作
def C(nums, d):
    for i in range (len(nums)):
        nums[i] += d

# 查询位操作
def Q(nums, i):
    # 符合要求的计数
    count = 0
    for j in range(len(nums)):
        # 将整数转换成二进制字符串，并且逆序排列，让字符串第一位是二进制最低位
        binary = bin(nums[j])[2:][::-1]
        # 如果要查询的位超过了二进制的位数，认为补 0，要查询的是非 0 位，所以不计数，继续循环即可
        if i >= len(binary):
            continue
        # 查询位非 0，计数 + 1
        if binary[i] == '1':
            count += 1
    return count

if __name__ == '__main__':
    # 第一行输入
    N, M = map(int, input().split())
    # 输入 N 个整数
    nums = list(map(int, input().split()))
    # 循环输入 M 条指令行，按照指令不同分类
    for _ in range(M):
        instruction, operator_num = input().split()
        if instruction == 'Q':
            print(Q(nums, int(operator_num)))
        else:
            C(nums, int(operator_num))
