N = int(input())
p = list(map(int, input().split()))

dp = [0] * (sum(p) + 1)
dp[0] = 1
for i in range(N):
    for j in range(sum(p), -1, -1):
        if dp[j] == 1:
            dp[j+p[i]] = 1

print(dp.count(1))
