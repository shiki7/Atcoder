n = int(input())
x = [list(input()) for _ in range(n)]
ans = 0
for i in range(9):
    xflag = False
    for j in range(n):
        if x[j][i] == 'o':
            if not xflag:
                ans += 1
            xflag = True
        elif x[j][i] == 'x':
            ans += 1
            xflag = False
        else:
            xflag = False
print(ans)
