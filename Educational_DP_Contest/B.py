# pypyにしないとTLEになる
n, k = map(int, input().split())
h = list(map(int, input().split()))

dp = [0] * n
for i in range(1, n):
    min_tmp = float('inf')
    for j in range(1, k+1):
        if j > i:
            break
        min_tmp = min(min_tmp, dp[i-j] + abs(h[i]-h[i-j]))
    dp[i] = min_tmp
print(dp[-1])
