n = int(input())
a, b, c = 0, 0, 1
for _ in range(n):
    b = a
    a = c
    c = b+a
print(c)
