import itertools

n = int(input())
a = []
xy = [0] * n
for i in range(n):
    tmp = int(input())
    a.append(tmp)
    xy[i] = [list(map(int, input().split())) for j in range(tmp)]

comb = itertools.product([0, 1], repeat=n)
ans = 0
for c in comb:
    list_c = list(c)
    flag = True
    for i in range(len(xy)):
        if list_c[i] == 1:
            for j in range(len(xy[i])):
                if xy[i][j][1] == 1:
                    if list_c[xy[i][j][0]-1] != 1:
                        flag = False
                        break
                else:
                    if list_c[xy[i][j][0]-1] != 0:
                        flag = False
                        break
    if flag:
        ans = max(ans, list_c.count(1))
print(ans)
