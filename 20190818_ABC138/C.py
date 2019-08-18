# -*- coding: utf-8 -*-
N = int(input())
v = sorted(list(map(int, input().split())))

total = (v[0] + v[1]) / 2
for i in range(2, len(v)):
    total = (total + v[i]) / 2
print(total)
