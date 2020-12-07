# imos

import itertools

# 入力
N, W = map(int, input().split())
stp = [list(map(int, input().split())) for _ in range(N)]

a = [0] * (2*(10**5)+1)

for i in range(N):
    le = stp[i][0]
    ri = stp[i][1]
    a[le] += stp[i][2]
    a[ri] -= stp[i][2]

# 累積和
b = list(itertools.accumulate(a))
for i in range(len(b)):
    if b[i] > W:
        print('No')
        exit()
print('Yes')
