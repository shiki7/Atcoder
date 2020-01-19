n = int(input())
p = list(map(int, input().split()))
ans = 1
cur = p[0]
for i in range(1, n):
    if p[i] <= cur:
        cur = p[i]
        ans += 1
print(ans)
