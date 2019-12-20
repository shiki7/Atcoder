import math
a, b, x = map(int, input().split())

v = a*a*b
# 台形
if v/2 < x:
    c = (v - x) * 2 / (a ** 2)
    print(math.atan2(c, a)/math.pi*180)
# 三角形
else:
    c = x * 2 / (a*b)
    print(math.atan2(b, c)/math.pi*180)
