N, M, Q = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(Q)]

solved = [[] for _ in range(N)]
score = [N for _ in range(M)]

for i in range(Q):
    c = s[i]
    if c[0] == 1:
        ans = 0
        for j in range(len(solved[c[1]-1])):
            ans += score[solved[c[1]-1][j]-1]
        print(ans)
    elif c[0] == 2:
        score[c[2]-1] -= 1
        solved[c[1]-1].append(c[2])
