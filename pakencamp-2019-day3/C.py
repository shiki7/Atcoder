import itertools
import numpy as np

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
p = np.arange(M)

ans = 0
for x, y in list(itertools.combinations(p, 2)):
    total = 0
    for i in range(N):
        total += max(A[i][x], A[i][y])
    ans = max(ans, total)
print(ans)
