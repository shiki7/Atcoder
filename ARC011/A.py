a, b, c = map(int, input().split())
ans = c
d = 0
while True:
    if c//a == 0:
        break
    d = c % a
    c = (c // a)*b
    ans += c
    c += d
print(ans)
