N, Q = map(int, input().split())
S = list(list(map(int, input().split())) for _ in range(Q))
follow = [["N"] * N for _ in range(N)]
for i in range(Q):
    a = S[i][1]-1
    if S[i][0] == 1:
        follow[a][S[i][2]-1] = "Y"
    elif S[i][0] == 2:
        for j in range(N):
            if follow[j][a] == "Y":
                follow[a][j] = "Y"
    elif S[i][0] == 3:
        tmp = []
        for j in range(N):
            if follow[a][j] == "Y":
                for k in range(N):
                    if a == k:
                        continue
                    if follow[j][k] == "Y":
                        tmp.append(k)
        for x in tmp:
            follow[a][x] = "Y"
for i in range(N):
    print("".join(follow[i]))
