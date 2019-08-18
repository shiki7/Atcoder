# -*- coding: utf-8 -*-
N, A, B = map(int, input().split())

total = 0
for i in range(1, N+1):
    digit_sum = 0
    for j in str(i):
        digit_sum += int(j)
    if digit_sum <= B and digit_sum >= A:
        total += i
print(total)
