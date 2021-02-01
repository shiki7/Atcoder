N, S, D = map(int, input().split())
XY = list(list(map(int, input().split())) for _ in range(N))
for i in range(N):
    if XY[i][0] < S and XY[i][1] > D:
        print('Yes')
        exit()
print('No')
