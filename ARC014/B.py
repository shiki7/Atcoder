N = int(input())
S = list(input() for _ in range(N))
cur = S[0]
dic = []
dic.append(S[0])
for i in range(1, N):
    if cur[-1] != S[i][0] or S[i] in dic:
        if i % 2 == 0:
            print("LOSE")
            exit()
        else:
            print("WIN")
            exit()
    cur = S[i]
    dic.append(S[i])
print('DRAW')
