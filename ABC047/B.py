w, h, n = map(int, input().split())
xya = [list(map(int, input().split())) for _ in range(n)]

b = [[0 for _ in range(w)] for _ in range(h)]
for x, y, a in xya:
    if a == 1:
        for i in range(h):
            for j in range(x):
                b[i][j] = 1
    elif a == 2:
        for i in range(h):
            for j in range(x, w):
                b[i][j] = 1
    elif a == 3:
        for i in range(y):
            for j in range(w):
                b[i][j] = 1
    elif a == 4:
        for i in range(y, h):
            for j in range(w):
                b[i][j] = 1
ans = 0
for i in range(h):
    for j in range(w):
        if b[i][j] == 0:
            ans += 1
print(ans)
