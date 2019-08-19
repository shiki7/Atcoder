# -*- coding: utf-8 -*-
A, B = map(int, input().split())
num = (A+B)//2
if (abs(A-num) == abs(B-num)):
    print(num)
else:
    print('IMPOSSIBLE')
