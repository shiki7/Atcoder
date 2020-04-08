n, h, w = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    a = ab[i][0]
    b = ab[i][1]
    if a >= h and b >= w:
        ans += 1
print(ans)
