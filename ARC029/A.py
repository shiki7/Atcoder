n = int(input())
a = [int(input()) for _ in range(n)]
a = sorted(a, reverse=True)
b = 0
c = 0
for i in range(n):
    if b < c:
        b += a[i]
    else:
        c += a[i]
print(max(b, c))
