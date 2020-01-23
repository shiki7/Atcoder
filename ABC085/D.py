import heapq
import math

n, h = map(int, input().split())
max_a = 0
b = []
sum_b = 0
for _ in range(n):
    x, y = map(int, input().split())
    if x > max_a:
        max_a = x
    b.append(y)
    sum_b += y

b = list(map(lambda x: x*(-1), b))
heapq.heapify(b)
total = 0
flag = False
max_b = 0
for i in range(1, 10**8):
    if len(b) != 0:
        max_b = heapq.heappop(b)*(-1)
    else:
        flag = True
    if max_b < max_a or flag:
        print(i-1 + math.ceil((h - total) / max_a))
        exit()
    else:
        total += max_b
        if total >= h:
            print(i)
            exit()
