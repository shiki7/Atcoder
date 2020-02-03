n = int(input())
a = list(map(int, input().split()))

if n == 2:
    a = sorted(a)
    print(a[1], a[0])
    exit()

max_a = max(a)
M = max_a // 2
min_diff = float('inf')
r = 0
for i in range(n):
    if abs(a[i] - M) < min_diff:
        min_diff = abs(a[i] - M)
        r = a[i]

print(max_a, r)
