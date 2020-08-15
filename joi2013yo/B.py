n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

ans = [0] * n
for i in range(3):
    for j in range(n):
        flg = True
        for k in range(n):
            if j == k:
                continue
            if a[j][i] == a[k][i]:
                flg = False
                break
        if flg:
            ans[j] += a[j][i]

for i in range(n):
    print(ans[i])
