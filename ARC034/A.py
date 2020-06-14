n = int(input())
ans = 0
for _ in range(n):
    a = list(map(int, input().split()))
    ans = max(ans, sum(a[0:4]) + a[4] * 110 / 900)
print(ans)
