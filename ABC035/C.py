import itertools
N, Q = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(Q)]

a = [0] * (N+1)

# いもす法
for i in range(Q):
    le = lr[i][0]
    ri = lr[i][1]
    a[le-1] += 1
    a[ri] -= 1
ans = []
a = list(itertools.accumulate(a))

for i in range(N):
    ans.append(a[i] % 2)
print(''.join(map(str, ans)))
