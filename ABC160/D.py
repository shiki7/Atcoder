from collections import defaultdict

dd = defaultdict(int)

N, X, Y = map(int, input().split())
for i in range(N-1):
    for j in range(i+1, N):
        dd[min(j-i, abs(X-1-i) + abs(Y-1-j) + 1, abs(Y-1-i)+abs(X-1-j) + 1)] += 1
for i in range(1, N):
    print(dd[i])
