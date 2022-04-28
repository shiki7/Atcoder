a, b, c, d, e, f, x = map(int, input().split())

l = x // (a + c) * a * b + min(x % (a + c), a) * b
r = x // (d + f) * d * e + min(x % (d + f), d) * e
if l == r:
    print("Draw")
elif l < r:
    print("Aoki")
else:
    print("Takahashi")
