Q = int(input())
lr = [list(map(int, input().split())) for _ in range(Q)]
N = 10**5
c = [0] * (N+1)
tf = [False] * (N+1)

# 素数の倍数は素数ではないので除外していく
for i in range(2, N+1):
    if not tf[i]:
        for j in range(i*2, N+1, i):
            tf[j] = True
for i in range(3, N, 2):
    if not tf[i] and not tf[(i+1)//2]:
        c[i] += 1

for i in range(3, N, 1):
    c[i] += c[i-1]
for l, r in lr:
    print(c[r] - c[l-1])
