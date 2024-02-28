from math import *

str = input()
extract_str = [str[2 ** i - 1] for i in range(floor(log2(len(str))) + 1)]
result = ""
i, j = 0, len(extract_str) - 1
while i <= j:
    result += extract_str[i]
    if i != j:
        result += extract_str[j]
    i += 1
    j -= 1

print(result)
