K, N = map(int, input().split())
a = list(map(int, input().split()))

max_diff = a[0] + K - a[-1]
for i in range(1, N):
    max_diff = max(max_diff, a[i] - a[i-1])
print(K-max_diff)
