import math

n = int(input())
a = [int(input()) for _ in range(n)]
total = 0
a.sort()
for i in range(1, n+1):
    if i % 2 == 1:
        total += a[-i] ** 2
    else:
        total -= a[-i] ** 2
print(total * math.pi)
