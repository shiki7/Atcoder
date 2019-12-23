n, k = map(int, input().split())
x = list(map(int, input().split()))

ans = float("inf")
for i in range(0, n-(k-1)):
    lr = abs(x[i]) + abs(x[i+k-1]-x[i])
    rl = abs(x[i+k-1]) + abs(x[i+k-1]-x[i])
    ans = min(lr, rl, ans)
print(ans)
