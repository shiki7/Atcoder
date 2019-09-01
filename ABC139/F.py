# not clear
from math import sqrt

N = int(input())
x = []
y = []
total = 0
for i in range(N):
    tmp_x, tmp_y = map(int, input().split())
    x.append(tmp_x)
    y.append(tmp_y)

# 4パターン計測する
# x+ y+
total_x = 0
total_y = 0
for i in range(N):
    if x[i] + y[i] > 0:
        total_x += x[i]
        total_y += y[i]
    elif x[i] + y[i] == 0:
        if ((total_x+x[i])**2 + (total_y+y[i])**2) > (total_x**2 + total_y**2):
            total_x += x[i]
            total_y += y[i]
total_a = sqrt(total_x**2 + total_y**2)

# x+ y-
total_x = 0
total_y = 0
for i in range(N):
    if x[i] - y[i] >= 0:
        total_x += x[i]
        total_y += y[i]
    elif x[i] + y[i] == 0:
        if ((total_x+x[i])**2 + (total_y+y[i])**2) > (total_x**2 + total_y**2):
            total_x += x[i]
            total_y += y[i]
total_b = sqrt(total_x**2 + total_y**2)

# x- y-
total_x = 0
total_y = 0
for i in range(N):
    if -x[i] - y[i] >= 0:
        total_x += x[i]
        total_y += y[i]
    elif x[i] + y[i] == 0:
        if ((total_x+x[i])**2 + (total_y+y[i])**2) > (total_x**2 + total_y**2):
            total_x += x[i]
            total_y += y[i]
total_c = sqrt(total_x**2 + total_y**2)

# x- y+
total_x = 0
total_y = 0
for i in range(N):
    if -x[i] + y[i] >= 0:
        total_x += x[i]
        total_y += y[i]
    elif x[i] + y[i] == 0:
        if ((total_x+x[i])**2 + (total_y+y[i])**2) > (total_x**2 + total_y**2):
            total_x += x[i]
            total_y += y[i]
total_d = sqrt(total_x**2 + total_y**2)

print(max(total_a, total_b, total_c, total_d))
