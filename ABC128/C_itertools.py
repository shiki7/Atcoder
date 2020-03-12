import itertools

N, M = map(int, input().split())
ks = [list(map(int, input().split())) for _ in range(M)]
p = list(map(int, input().split()))

k = []
s = []
for i in range(len(ks)):
    k.append(ks[i][0])
    s.append(ks[i][1:])

ans = 0
for x in itertools.product([0, 1], repeat=N):
    total = 0
    for i in range(M):
        count = 0
        for j in range(k[i]):
            if x[s[i][j]-1]:
                count += 1
        if p[i] == count % 2:
            total += 1
    if total == M:
        ans += 1
print(ans)
