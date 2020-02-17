# しゃくとり法 メモ化
n = int(input())
a = list(map(int, input().split()))
v = [False for _ in range(max(a) + 1)]
v[a[0]] = True

if n == 1:
    print(1)
    exit()

left = 0
right = 1
ans = 0

while right < n and ans <= n-left+1:
    if not v[a[right]]:
        v[a[right]] = True
        ans = max(ans, right-left+1)
        right += 1
    elif left == right:
        left += 1
        right += 1
    else:
        v[a[left]] = False
        left += 1
print(ans)
