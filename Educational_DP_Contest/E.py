# ナップザック問題(重さが10^9を超える場合)
# 「最大の価値を満たす重さの最小化」という風に問題を置き換え
N, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]
V = sum([v for _, v in wv])

inf = float("inf")
dp = [[inf for _ in range(V+1)] for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    weight = wv[i][0]
    value = wv[i][1]
    for v in range(V+1):
        if v-value >= 0:
            dp[i+1][v] = min(dp[i][v], dp[i][v-value] + weight)
        else:
            dp[i+1][v] = dp[i][v]
ans = 0
for i in range(V+1):
    if dp[-1][i] <= W:
        ans = i
print(ans)
