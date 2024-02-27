n, x, y = map(int, input().split())
average_score = {}
for _ in range(n):
    course, name, score = input().split()
    score  = int(score)
    if name not in average_score:
        average_score[name] = [score, 1]
    else:
        average_score[name] = [(average_score[name][0] * average_score[name][1] + score) / (average_score[name][1] + 1),
                               average_score[name][1] + 1]

m = int(input())
for _ in range(m):
    name = input()
    if average_score[name][0] > y and average_score[name][1] >= x:
        print("yes")
    else:
        print("no")

