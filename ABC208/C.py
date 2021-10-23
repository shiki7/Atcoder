N, K = map(int, input().split())
a = list(map(int, input().split()))
b = sorted(a)

target = b[K % N]
for i in range(N):
    print(K // N + (1 if a[i] < target else 0))
