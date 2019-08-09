# -*- coding: utf-8 -*-
N = int(input())
a = []
for i in range(N):
    a += [int(input())]
print(len(set(a)))
