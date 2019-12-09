n, a, b = map(int, input().split())
sd = [list(input().split()) for _ in range(n)]

pos = 0
for s, d in sd:
    d = int(d)
    if a <= d <= b:
        if s == 'East':
            pos += d
        else:
            pos -= d
    elif d < a:
        if s == 'East':
            pos += a
        else:
            pos -= a
    elif d > b:
        if s == 'East':
            pos += b
        else:
            pos -= b
if pos < 0:
    print('West', abs(pos))
elif pos > 0:
    print('East', pos)
else:
    print(0)
