# -*- coding: utf-8 -*-
N = int(input())
arr = list(map(int, input().split()))
print(arr[0])
total = 0
for a in arr:
    total += 1/a
print(1/total)
