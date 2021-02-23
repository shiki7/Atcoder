a, b, c = map(int, input().split())

if b > 4:
    b = b % 4 + 4
if c > 4:
    c = c % 4 + 4
d = b**c
if d > 4:
    d = d % 4 + 4

ans = int(str(a)[-1]) ** d
print(str(ans)[-1])
