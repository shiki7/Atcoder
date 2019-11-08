n = 4
c = [input().split() for _ in range(n)]
for i in range(1, n+1):
    c[-i].reverse()
    print(' '.join(c[-i]))
