n = 3
x = [list(map(int, input().split())) for _ in range(n)]
a = [0] * n
b = [0] * n
a[0] = 0
b[0] = x[0][0]
b[1] = x[0][1]
b[2] = x[0][2]
a[1] = x[1][0] - b[0]
a[2] = x[2][0] - b[0]

for i in range(n):
    for j in range(n):
        if x[i][j] != (a[i] + b[j]):
            print('No')
            exit()
print('Yes')
