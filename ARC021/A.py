a = [list(map(int, input().split())) for _ in range(4)]
for i in range(3):
    for j in range(4):
        if a[i][j] == a[i+1][j]:
            print('CONTINUE')
            exit()
for i in range(4):
    for j in range(3):
        if a[i][j] == a[i][j+1]:
            print('CONTINUE')
            exit()
print('GAMEOVER')
