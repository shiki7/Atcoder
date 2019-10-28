import math

tx1, ty1, tx2, ty2, t, v = map(int, input().split())
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    x = xy[i][0]
    y = xy[i][1]
    if math.sqrt((x - tx1)**2 +
                 (y - ty1)**2) + math.sqrt((x - tx2)**2 +
                                           (y - ty2)**2) <= t * v:
        print('YES')
        exit()
print('NO')
