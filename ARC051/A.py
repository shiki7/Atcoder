import math
x1, y1, r = map(int, input().split())
x2, y2, x3, y3 = map(int, input().split())
if x1 - r >= x2 and x1 + r <= x3 and y1 - r >= y2 and y1 + r <= y3:
    print('NO')
else:
    print('YES')
# 四角形が円に内包する条件
# 円の中心と4辺の距離が半径r以下であれば内包する
if math.sqrt((x2 - x1) ** 2 + (y2-y1) ** 2) <= r and math.sqrt((x3 - x1) ** 2 + (y2-y1) ** 2) <= r and math.sqrt((x2 - x1) ** 2 + (y3-y1) ** 2) <= r and math.sqrt((x3 - x1) ** 2 + (y3-y1) ** 2) <= r:
    print('NO')
else:
    print('YES')
