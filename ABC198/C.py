import math
R, X, Y = map(int, input().split())
a = (X**2+Y**2)**(1/2)
if R == a:
    print(1)
elif R > a:
    print(2)
else:
    print(math.ceil(a/R))
