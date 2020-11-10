n = int(input())
a = list(map(int, input().split()))
ans = 0
total_a = 0
max_d = 0
cur = 0
for i in range(n):
    total_a += a[i]
    max_d = max(max_d, total_a)
    ans = max(ans, cur + max_d)
    cur += total_a
print(ans)
