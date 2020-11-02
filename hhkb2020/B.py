H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]
ans = 0
for i in range(H-1):
    for j in range(W):
        if s[i][j] == '.' and s[i+1][j] == '.':
            ans += 1
for i in range(H):
    for j in range(W-1):
        if s[i][j] == '.' and s[i][j+1] == '.':
            ans += 1
print(ans)
