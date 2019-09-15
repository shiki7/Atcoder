N, K, Q = map(int, input().split())
a = [int(input()) for _ in range(Q)]

count = []
for i in range(N):
    count.append(K-Q)

for i in range(Q):
    count[a[i]-1] += 1
for i in range(N):
    if count[i] <= 0:
        print('No')
    else:
        print('Yes')
