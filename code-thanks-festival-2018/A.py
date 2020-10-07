t, a, b, c, d = map(int, input().split())
ans = 0
if a <= t:
    ans = b
if c <= t:
    ans = max(ans, d)
if a+c <= t:
    ans = b+d
print(ans)
