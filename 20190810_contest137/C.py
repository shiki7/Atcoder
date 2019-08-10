# -*- coding: utf-8 -*-
N = int(input())
a = []
count = 0
for i in range(N):
    a += [''.join(sorted(input()))]
sorted_a = sorted(a)
for i in range(N-1):
    for j in range(1, N):
        if i+j >= N:
            break
        if sorted_a[i] == sorted_a[i+j]:
            count += 1
        else:
            break
print(count)
