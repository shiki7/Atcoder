import math

A, B, W = map(int, input().split())
W = 1000 * W
ans_max = int(math.floor(W/A))
ans_min = int(math.ceil(W/B))

if ans_min > ans_max:
    print('UNSATISFIABLE')
else:
    print(ans_min, ans_max)
