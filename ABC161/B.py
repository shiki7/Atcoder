n, m = map(int, input().split())
a = list(map(int, input().split()))
total = sum(a)
ans = 0
for i in range(n):
    if a[i] >= total / (4*m):
        ans += 1
if ans >= m:
    print('Yes')
else:
    print('No')
