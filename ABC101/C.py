n, k = map(int, input().split())
a = list(map(int, input().split()))
min_a = min(a)
count = 0
for i in range(n):
    if min_a != a[i]:
        count += 1
a, b = divmod(count, k-1)
if b == 0:
    print(a)
else:
    print(a+1)
