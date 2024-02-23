L, M = map(int, input().split())
trees = [1] * (L + 1)

for i in range(M):
    start, end = map(int, input().split())
    for tree in range(start, end + 1):
        trees[tree] = 0
print(sum(trees))
