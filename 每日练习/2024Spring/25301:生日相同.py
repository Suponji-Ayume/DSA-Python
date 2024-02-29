n = int(input())
same_birthday = {}
for i in range(n):
    ID, month, date = [_ for _ in input().split()]
    month = int(month)
    date = int(date)
    if (month, date) not in same_birthday:
        same_birthday[(month, date)] = [ID]
    else:
        same_birthday[(month, date)].append(ID)

# 对字典的键按日期大小排序
sorted_same_birthday_list = sorted(same_birthday.items(), key=lambda x: (x[0][0], x[0][1]))

# 打印输出
for item in sorted_same_birthday_list:
    if len(item[1]) > 1:
        print(f"{item[0][0]} {item[0][1]}", end="")
        for i in range(len(item[1])):
            if i != len(item[1]) - 1:
                print(f" {item[1][i]}", end="")
            else:
                print(f" {item[1][i]}")
