# -*- coding: utf-8 -*-
N, Y = map(int, input().split())
for a in range(N+1):
    for b in range(N+1):
        if a+b > N:
            break
        c = N-a-b
        if Y == (1000*a + 5000*b + 10000*c):
            print('{} {} {}'.format(c, b, a))
            exit()
print('-1 -1 -1')
