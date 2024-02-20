# 打印出小于等于n的所有素数表
def prime_list(n: int):
    mask = [1] * (n + 1)
    mask[0] = mask[1] = 0
    for i in range(2, n + 1):
        j = 2
        while i * j <= n:
            mask[i * j] = 0
            j += 1
    return [i for i in range(n + 1) if mask[i] == 1]


if __name__ == "__main__":
    n = int(input())
    prime_list = prime_list(n)

    # 寻找 n 的素数分解
    for i in prime_list:
        if n - i in prime_list:
            print(i, n - i)
            break
