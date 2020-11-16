from itertools import permutations
N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

a = [i for i in range(1, N)]
p = list(permutations(a, N-1))
ans = 0
for i in range(len(p)):
    d = 0
    d += T[0][p[i][0]]
    for j in range(N-2):
        d += T[p[i][j]][p[i][j+1]]
    d += T[p[i][-1]][0]
    if d == K:
        ans += 1
print(ans)
