def dist(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2) ** 0.5


N, M = map(int, input().split())
xyr = [list(map(float, input().split())) for _ in range(N+M)]

ans = float('inf')
for i in range(N+M):
    for j in range(N+M):
        if i == j:
            continue
        elif i < N:
            ans = min(ans, xyr[i][2])
        elif j < N:
            ans = min(ans, dist(xyr[i], xyr[j]) - xyr[j][2])
        else:
            ans = min(ans, dist(xyr[i], xyr[j]) / 2)
print(ans)
