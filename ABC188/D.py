N, C = map(int, input().split())
lrc = [list(map(int, input().split())) for _ in range(N)]

evt = []
for i in range(N):
    li = lrc[i][0] - 1
    ri = lrc[i][1]
    ci = lrc[i][2]
    evt.append([li, ci])
    evt.append([ri, -ci])
evt = sorted(evt)

t = 0
ans = 0
c = 0
for x, y in evt:
    ans += min(C, c) * (x-t)
    t = x
    c += y
print(ans)
