N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if (a[i][0] - a[j][0]) == 0 or (a[i][0] - a[k][0]) == 0:
                if (a[i][0] - a[j][0]) == (a[i][0] - a[k][0]):
                    print('Yes')
                    exit()
            elif (a[i][1] - a[j][1]) / (a[i][0] - a[j][0]) == (a[i][1] - a[k][1]) / (a[i][0] - a[k][0]):
                print('Yes')
                exit()
print('No')
