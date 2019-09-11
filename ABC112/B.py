N, T = map(int, input().split())
ct = [list(map(int, input().split())) for _ in range(N)]
ans = []
for c, t in ct:
    if t <= T:
        ans.append(c)
if len(ans) > 0:
    print(min(ans))
else:
    print('TLE')
