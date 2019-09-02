N = int(input())
A = list(map(int, input().split()))
min_total = 10**9

x = []
for i in range(N):
    x.append(A[i] - (i + 1))
x.sort()
b = x[N // 2]
total = 0
for i in range(N):
    total += abs(A[i] - (b + i + 1))
print(total)
