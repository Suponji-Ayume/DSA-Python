def t_prime_set(N):
    mask = [1] * (N + 1)
    for i in range(2, N + 1):
        # 如果这个是已经不是素数了，它的倍数也一定被筛过了
        if mask[i] == 0:
            continue
        # 只需要从 i * i 开始筛就好，因为 i * j (j < i) 的数已经在前面被 j 筛过了
        j = i
        while i * j <= N:
            mask[i * j] = 0
            j += 1

    return set([i ** 2 for i in range(2, N + 1) if mask[i] == 1])


if __name__ == '__main__':
    t_prime_set = t_prime_set(1000000)
    n = int(input())
    input_nums = list(map(int,input().split()))
    for num in input_nums:
        if num in t_prime_set:
            print("YES")
        else:
            print("NO")