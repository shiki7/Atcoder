N = int(input())
XL = [list(map(int, input().split())) for _ in range(N)]

# アームが伸びる範囲に置き換える
a = []
for i in range(N):
    a.append([XL[i][0] - XL[i][1], XL[i][0] + XL[i][1]])
# アームが届く最大座標でソートする
a = sorted(a, key=lambda x: x[1])

ans = 0
cur = - float('inf')
for i in range(N):
    if a[i][0] >= cur:
        ans += 1
        cur = a[i][1]
print(ans)
