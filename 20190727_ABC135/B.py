# -*- coding: utf-8 -*-
N = int(input())
p = list(map(int, input().split()))
count = 0
for i, num in enumerate(sorted(p)):
    if num != p[i]:
        count += 1
if count > 2:
    print('NO')
else:
    print('YES')
