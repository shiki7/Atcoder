n, a, b = map(int, input().split())
x = list(map(int, input().split()))

ans = 0
for i in range(1, n):
    if a * (x[i]-x[i-1]) < b:
        ans += a * (x[i]-x[i-1])
    else:
        ans += b
print(ans)
