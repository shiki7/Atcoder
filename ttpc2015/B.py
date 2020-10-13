n, b, c = map(int, input().split())
a = list(map(int, input().split()))
a = a[::-1]
ans = 0
for i in range(n):
    if c == 0:
        break
    elif b <= c:
        ans += b*a[i]
        c -= b
    elif b > c:
        ans += c*a[i]
        break
print(ans)
