# ナップザック問題(pypyじゃないとTLE)
N, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]

inf = float("inf")
dp = [[-inf for _ in range(W+1)] for _ in range(N+1)]
for i in range(W+1):
    dp[0][i] = 0

for i in range(N):
    weight = wv[i][0]
    value = wv[i][1]
    for w in range(W+1):
        # 重量に収まる場合のみ価値を加える
        if weight <= w:
            dp[i+1][w] = max(dp[i][w-weight] + value, dp[i][w])
        else:
            dp[i+1][w] = dp[i][w]
print(max(dp[-1]))
