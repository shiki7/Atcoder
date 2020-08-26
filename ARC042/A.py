# TLE
from collections import deque

n, m = map(int, input().split())
b = []
for i in range(n):
    b.append(i+1)
d = deque(b)
for _ in range(m):
    a = int(input())
    d.remove(a)
    d.appendleft(a)
for i in range(n):
    print(d[i])
