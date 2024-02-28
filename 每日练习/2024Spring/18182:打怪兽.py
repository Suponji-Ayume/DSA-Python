nCases = int(input())

for _ in range(nCases):
    n, m, b = map(int, input().split())
    skills = {}
    for i in range(n):
        t, x = map(int, input().split())
        if t in skills:
            skills[t].append(x)
        else:
            skills[t] = [x]


    # 对每一时刻的招数进行排序
    for i in skills:
        skills[i].sort(reverse=True)
    # 再按照时间顺序排列
    sorted_skills = sorted(skills.items(), key=lambda x:x[0])

    # 开始打怪兽
    alive = True
    for i in range(len(sorted_skills)):
        for j in range(min(m, len(sorted_skills[i][1]))):
            b -= sorted_skills[i][1][j]
            if b <= 0:
                alive = False
                break
        if not alive:
            print(sorted_skills[i][0])
            break
    if alive:
        print("alive")