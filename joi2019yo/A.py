from math import ceil
A, B, C = map(int, input().split())
x = C // (7*A + B)
d = C - x*(7*A + B)
if ceil(d/A) > 7:
    print(x*7 + 7)
else:
    print(x*7 + ceil(d/A))
