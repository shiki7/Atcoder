# -*- coding: utf-8 -*-
S = int(input())
INF = 10**9

if S == 10**18:
    print(0, 0, INF, 1, 0, INF)
else:
    x = INF - S % INF
    y = S // INF + 1
    print(0, 0, INF, 1, x, y)
