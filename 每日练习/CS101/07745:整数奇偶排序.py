# 存放奇偶数列
odd_lst = []
even_lst = []

nums = list(map(int,input().split()))
for num in nums:
    if num % 2 == 0:
        even_lst.append(num)
    else:
        odd_lst.append(num)

odd_lst.sort(reverse=True)
even_lst.sort()

# 最终结果
result_lst = odd_lst + even_lst

# 逐个打印输出
for i in range(10):
    if i != 9:
        print(result_lst[i],end=' ')
    else:
        print(result_lst[i])