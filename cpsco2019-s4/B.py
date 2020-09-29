N, D = map(int, input().split())
S = [input() for _ in range(D)]
ans = 0
for i in range(D-1):
    for j in range(i+1, D):
        cnt = 0
        for k in range(N):
            if S[i][k] == 'o' or S[j][k] == 'o':
                cnt += 1
        ans = max(ans, cnt)
print(ans)
