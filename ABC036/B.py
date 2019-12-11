n = int(input())
s = [list(input()) for _ in range(n)]
ans = [[0 for _ in range(n)] for _ in range(n)]
b = [[0]*n]*n
for i in range(n):
    for j in range(n):
        ans[i][j] = s[n-1-j][i]
for a in ans:
    print(''.join(a))
