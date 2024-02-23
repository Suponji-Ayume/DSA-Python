n = int(input())
for i in range(n):
    p = int(input())
    str_p = str(p)
    if p % 19 == 0 or "19" in str_p:
        print("Yes")
    else:
        print("No")