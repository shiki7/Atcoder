n, m = map(int, input().split())
sc = [list(map(int, input().split())) for _ in range(m)]
ans = [-1] * n

if n == 1:
    if m == 0:
        print(0)
        exit()
    for i in range(m):
        s = sc[i][0]
        c = sc[i][1]
        if ans[s-1] != -1 and ans[s-1] != c:
            print(-1)
            exit()
        else:
            ans[s-1] = c
    print(ans[0])
else:
    if m == 0:
        print('1' + str('0' * (n-1)))
        exit()
    for i in range(m):
        s = sc[i][0]
        c = sc[i][1]
        if ans[s-1] != -1 and ans[s-1] != c:
            print(-1)
            exit()
        elif s == 1 and c == 0:
            print(-1)
            exit()
        else:
            ans[s-1] = c
    for i in range(n):
        if i == 0 and ans[i] == -1:
            ans[i] = 1
        elif i != 0 and ans[i] == -1:
            ans[i] = 0
    print(''.join(map(str, ans)))
