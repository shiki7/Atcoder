N, M = map(int, input().split())
s = []
s.append(['0']*(M+2))
for _ in range(N):
    tmp = list('0' + input() + '0')
    s.append(tmp)
s.append(['0']*(M+2))

for i in range(1, N+1):
    ans = []
    for j in range(1, M+1):
        cnt = 0
        if s[i-1][j-1] == "#":
            cnt += 1
        if s[i-1][j] == "#":
            cnt += 1
        if s[i-1][j+1] == "#":
            cnt += 1
        if s[i][j-1] == "#":
            cnt += 1
        if s[i][j] == "#":
            cnt += 1
        if s[i][j+1] == "#":
            cnt += 1
        if s[i+1][j-1] == "#":
            cnt += 1
        if s[i+1][j] == "#":
            cnt += 1
        if j < M and s[i+1][j+1] == "#":
            cnt += 1
        ans.append(cnt)
    print(''.join(map(str, ans)))
