N = int(input())
ST = [input().split() for _ in range(N)]
for i in range(N):
    for j in range(i + 1, N):
        if ST[i][0] == ST[j][0] and ST[i][1] == ST[j][1]:
            print('Yes')
            exit()
print('No')
