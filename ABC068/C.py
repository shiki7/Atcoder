n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

x = []
y = []
for a, b in ab:
    if a == 1:
        x.append(b)
    if b == n:
        y.append(a)

if len(set(x) & set(y)) >= 1:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
