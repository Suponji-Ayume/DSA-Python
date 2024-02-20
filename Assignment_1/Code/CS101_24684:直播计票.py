votes = {}

vote_list = list(map(int, input().split()))
for index in vote_list:
    if index not in votes:
        votes[index] = 1
    else:
        votes[index] += 1

# 先按照票数降序排序，再按照编号升序排序
votes_list = sorted(votes.items(), key=lambda x: (-x[1], x[0]))

# 如果有票数并列的，按序输出 index
for index, count in votes_list:
    if index == votes_list[0][0]:
        print(index, end='')
    else:
        if count == votes_list[0][1]:
            print(f' {index}', end='')
