# -*- coding: utf-8 -*-
N = int(input())
a = list(map(int, input().split()))

x, y = 0, 0
for i, v in enumerate(sorted(a, reverse=True)):
    if i % 2 == 0:
        x += v
    else:
        y += v
print(x-y)
