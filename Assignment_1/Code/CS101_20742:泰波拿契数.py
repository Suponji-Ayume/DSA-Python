def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


if __name__ == '__main__':
    n = int(input())
    print(tribonacci(n))
