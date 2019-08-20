# -*- coding: utf-8 -*-
N = int(input())
digit_count = len(str(N))
if digit_count == 1:
    print(N)
elif (digit_count % 2 == 1):
    print(N - int(str(90) * (digit_count//2)))
else:
    total = 0
    for i in range(0, digit_count//2):
        total += 9*(100**i)
    print(total)
