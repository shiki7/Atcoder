a = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
b = [int(input()) for _ in range(n)]

for i in range(n):
    for j in range(3):
        for k in range(3):
            if b[i] == a[j][k]:
                a[j][k] = '#'

if a[0][0] == "#" and a[0][1] == "#" and a[0][2] == '#':
    print('Yes')
elif a[1][0] == "#" and a[1][1] == "#" and a[1][2] == '#':
    print('Yes')
elif a[2][0] == "#" and a[2][1] == "#" and a[2][2] == '#':
    print('Yes')
elif a[0][0] == "#" and a[1][0] == "#" and a[2][0] == '#':
    print('Yes')
elif a[0][1] == "#" and a[1][1] == "#" and a[2][1] == '#':
    print('Yes')
elif a[0][2] == "#" and a[1][2] == "#" and a[2][2] == '#':
    print('Yes')
elif a[0][0] == "#" and a[1][1] == "#" and a[2][2] == '#':
    print('Yes')
elif a[0][2] == "#" and a[1][1] == "#" and a[2][0] == '#':
    print('Yes')
else:
    print('No')
