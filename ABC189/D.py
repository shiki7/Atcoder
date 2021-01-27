N = int(input())
S = list(input() for _ in range(N))

dp = [0] * (N+1)
dp[0] = 1
for i in range(N):
    if S[i] == "AND":
        dp[i+1] = dp[i]
    else:
        dp[i+1] = dp[i] + 2**(i+1)
print(dp[-1])
