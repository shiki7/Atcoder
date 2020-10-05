N, T = map(int, input().split())
a = list(map(int, input().split()))
cur = 0
for i in range(N):
    if a[i] >= cur:
        cur = a[i]
    else:
        for k in range(1, 100):
            if a[i] + k*T > cur:
                cur = a[i] + k*T
                break
print(cur)
