import itertools

N, M = map(int, input().split())
AB = list(list(map(int, input().split())) for _ in range(M))
K = int(input())
CD = list(list(map(int, input().split())) for _ in range(K))

p = list(itertools.product([0, 1], repeat=K))
ans = 0
for i in range(2**K):
    cnt = 0
    s = set()
    for j in range(K):
        s.add(CD[j][p[i][j]])
    for j in range(M):
        if AB[j][0] in s and AB[j][1] in s:
            cnt += 1
    ans = max(ans, cnt)
print(ans)
