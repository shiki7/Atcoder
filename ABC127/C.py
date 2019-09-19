n, m = map(int, input().split())
mi, ma = 1, n
for _ in range(m):
    l, r = map(int, input().split())
    mi = max(l, mi)
    ma = min(r, ma)
print(max(0, ma - mi + 1))
