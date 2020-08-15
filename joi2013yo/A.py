from math import ceil
L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
d = L-max(ceil(A/C), ceil(B/D))
if d < 0:
    print(0)
else:
    print(d)
