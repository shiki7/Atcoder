# 最終的に.......#####の並びになると想定
# それぞれの累積和の足し算が最小になる境目を求める
N = int(input())
S = list(input())
b = [0] * N
w = [0] * N
x, y = 0, 0
ans = 0
# 累積和
for i in range(N):
    if S[i] == '#':
        x += 1
    else:
        y += 1
    b[i] = x
    w[i] = y

ans = float('inf')
for i in range(N):
    ans = min(ans, b[i] + w[N-1] - w[i])
print(min(ans, b[N-1], w[N-1]))
