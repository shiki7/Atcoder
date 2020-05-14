from itertools import product
from operator import add

n, m, x = map(int, input().split())
ca = [list(map(int, input().split())) for _ in range(n)]

p = list(product([0, 1], repeat=n))
ans = float('inf')
for i in range(len(p)):
    total = [0]*m
    money = 0
    for j in range(n):
        if p[i][j] == 1:
            total = list(map(add, total, ca[j][1:m+1]))
            money += ca[j][0]
    if len([y for y in total if y >= x]) == m:
        ans = min(ans, money)
if ans == float('inf'):
    print(-1)
else:
    print(ans)
