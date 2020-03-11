N = int(input())
xyh = [list(map(int, input().split())) for _ in range(N)]


for i in range(N):
    if xyh[i][2] > 0:
        xx, yy, hh = xyh[i][0], xyh[i][1], xyh[i][2]
        break

for cx in range(101):
    for cy in range(101):
        H = hh + abs(cx-xx) + abs(cy-yy)
        count = 0
        for i in range(N):
            x = xyh[i][0]
            y = xyh[i][1]
            h = xyh[i][2]
            if max(H - abs(x - cx) - abs(y - cy), 0) == h:
                count += 1
        if count == N:
            print(cx, cy, H)
            exit()
