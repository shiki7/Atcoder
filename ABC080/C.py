import itertools

N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]

ans = -float('inf')
for x in list(itertools.product([0, 1], repeat=10)):
    if x.count(0) == 10:
        continue
    total = 0
    for i in range(N):
        count = 0
        for j in range(10):
            count += x[j] & F[i][j]
        total += P[i][count]
    ans = max(ans, total)
print(ans)
