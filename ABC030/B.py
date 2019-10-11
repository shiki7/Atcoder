n, m = map(int, input().split())

a = (n % 12) * 30 + 30 * (m / 60)
b = 6 * m
ans = abs(a - b)
if ans <= 180:
    print(ans)
else:
    print(360 - ans)
