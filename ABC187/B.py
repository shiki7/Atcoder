N = int(input())
xy = list(list(map(int, input().split())) for _ in range(N))
ans = 0
for i in range(N):
    for j in range(i, N):
        if xy[j][0] - xy[i][0] != 0 and -1 <= (xy[j][1] - xy[i][1]) / (xy[j][0] - xy[i][0]) <= 1:
            ans += 1
print(ans)
