N, X = map(int, input().split())
vp = list(list(map(int, input().split())) for _ in range(N))
total = 0
for i in range(N):
    total += vp[i][0] * vp[i][1]
    if total > X * 100:
        print(i+1)
        exit()
print(-1)
