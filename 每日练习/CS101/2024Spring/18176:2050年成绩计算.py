# 根据数学推理，t-prime 应该是素数的完全平方，我们只需要打印素数表然后求平方即可
def t_prime_lst(N):
    mask = [1] * (N + 1)
    for i in range(2, N + 1):
        j = 2
        while i * j <= N:
            mask[i * j] = 0
            j += 1
    lst = [i ** 2 for i in range(2, N + 1) if mask[i] == 1]
    return lst


if __name__ == '__main__':
    t_prime_lst = t_prime_lst(10000)
    m, n = map(int, input().split())
    for _ in range(m):
        valid_score = 0
        scores = list(map(int, input().split()))
        for score in scores:
            if score in t_prime_lst:
                valid_score += score
        if valid_score == 0:
            print('0')
        else:
            average_score = valid_score / len(scores)
            print("{:.2f}".format(average_score))
