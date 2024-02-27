A  = input()

# 前缀和思想
sub_binary2int = []
# 边界条件
sub_binary2int.append(int(A[0]))
for i in range(1, len(A)):
    bit = int(A[i])
    sub_binary2int.append(sub_binary2int[i - 1] * 2 + bit)

result = ""

for sub_sum in sub_binary2int:
    if sub_sum % 5 ==0:
        result += "1"
    else:
        result += "0"

print(result)