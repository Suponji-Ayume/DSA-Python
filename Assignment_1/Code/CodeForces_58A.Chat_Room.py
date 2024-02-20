s = input()

word = "hello"

# 设定一个指向word中字符的游标
i = 0

# 设定一个标志位，用于判断是否找到了hello
flag = False

# 遍历s，如果找到了hello中的字符，i += 1
for j in range(len(s)):
    if s[j] == word[i]:
        i += 1
    if i == 5:
        flag = True
        break

if flag:
    print("YES")
else:
    print("NO")
