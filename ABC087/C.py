n = int(input())
a = [list(map(int, input().split())) for _ in range(2)]

if n == 1:
    print(a[0][0] + a[1][0])
    exit()

ans = 0
for i in range(0, n - 1):
    ans = max(ans, sum(a[0][:i]) + a[0][i] + a[1][i] + sum(a[1][i + 1:]))
print(ans)
