import itertools
n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]

d = [i for i in range(0, k)]
li = list(itertools.product(d, repeat=n))
for i in range(len(li)):
    check = 0
    for j in range(n):
        check ^= t[j][li[i][j]]
    if check == 0:
        print('Found')
        exit()
print('Nothing')
