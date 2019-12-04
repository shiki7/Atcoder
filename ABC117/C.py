n, m = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)
b = []
for i in range(1, m):
    b.append(a[i] - a[i-1])
b = sorted(b, reverse=True)
print(sum(b[n-1:]))
