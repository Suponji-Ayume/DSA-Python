n = int(input())
max_sum = 0

for a1 in range(n + 1):
    for a2 in range(n + 1):
        if (a1 + a2) % 2 == 0:
            for a3 in range( n + 1):
                if (a2 + a3) % 3 == 0:
                    if (a1 + a2 + a3) % 5 == 0:
                        max_sum = a1 + a2 + a3 if a1 + a2 + a3 > max_sum else max_sum

print(max_sum)
