import itertools
import math

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
seq = []
for i in range(n):
    seq.append(i)
b = itertools.permutations(seq)
total = 0

for a in b:
    for i in range(1, n):
        total += math.sqrt((xy[a[i]][0] - xy[a[i-1]][0]) ** 2 +
                           (xy[a[i]][1] - xy[a[i-1]][1]) ** 2)
print(total/math.factorial(n))
