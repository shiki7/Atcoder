n = int(input())

# 二分探索
left = 0
right = n+1
while left + 1 < right:
    mid = (left + right) // 2
    if mid*(mid+1)//2 <= n+1:
        left = mid
    else:
        right = mid
print(n-left+1)
