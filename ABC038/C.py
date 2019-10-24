n = int(input())
a = list(map(int, input().split()))

# しゃくとり法
ans = 0
right = 0
for left in range(n):
    if left > right:
        right = left
    while right + 1 < n and a[right + 1] > a[right]:
        right += 1
    ans += right - left + 1
print(ans)
