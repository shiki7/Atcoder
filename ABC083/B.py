n, a, b = map(int, input().split())
ans = 0
for i in range(1, n + 1):
    s = 0
    for j in str(i):
        s += int(j)
    if a <= s <= b:
        ans += i
print(ans)
