a, b, x = map(int, input().split())


def check(m, x):
    return a*m + b * len(str(m)) <= x


left = 0
right = 10**9+1
# 二分探索
while right - left > 1:
    mid = (left + right) // 2
    if check(mid, x):
        left = mid
    else:
        right = mid
print(left)
