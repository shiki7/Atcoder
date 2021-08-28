S = input()
T = 'chokudai#'
MOD = 10 ** 9 + 7
dp = [[0 for j in range(len(T))] for i in range(len(S) + 1)]
dp[0][0] = 1
for i in range(len(S)):
    for j in range(len(T)):
        dp[i][j] %= MOD
        dp[i + 1][j] += dp[i][j]
        if S[i] == T[j]:
            dp[i + 1][j + 1] += dp[i][j]
print(dp[len(S)][8] % MOD)
