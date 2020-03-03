from math import sqrt
N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        x1 = xy[i][0]
        y1 = xy[i][1]
        x2 = xy[j][0]
        y2 = xy[j][1]
        ans = max(ans, sqrt((x1-x2) ** 2 + (y1-y2)**2))
print(ans)
