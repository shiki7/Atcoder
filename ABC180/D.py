x, y, a, b = map(int, input().split())
ans = 0
while True:
    if x * a >= y:
        break
    if x * a >= x + b:
        break
    x *= a
    ans += 1
ans += (y-1-x) // b
print(ans)
