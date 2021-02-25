B, C = map(int, input().split())

if C == 1:
    print(1 if B == 0 else 2)
    exit()
if B == 0:
    l = -C // 2
    r = (C - 1) // 2
    print(r - l + 1)
elif B > 0:
    a = -B - (C - 1) // 2
    b = -B + (C - 1) // 2
    c = B - C // 2
    d = B + (C - 2) // 2
    if b < c:
        print(d - c + 1 + b - a + 1)
    else:
        l = min(a, b, c, d)
        r = max(a, b, c, d)
        print(r - l + 1)
elif B < 0:
    a = B - C // 2
    b = B + (C - 2) // 2
    c = -B - (C - 1) // 2
    d = -B + (C - 1) // 2
    if b < c:
        print(d - c + 1 + b - a + 1)
    else:
        l = min(a, b, c, d)
        r = max(a, b, c, d)
        print(r - l + 1)
