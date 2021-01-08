a, b = input().split()
c = 0
d = 0
for x, y in zip(a, b):
    c += int(x)
    d += int(y)
print(max(c, d))
