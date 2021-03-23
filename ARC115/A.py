N, M = map(int, input().split())
S = list(input() for _ in range(N))
odd_cnt = 0
even_cnt = 0
for i in range(N):
    cnt = 0
    for j in range(M):
        if S[i][j] == '1':
            cnt += 1
    if cnt % 2 == 0:
        even_cnt += 1
    else:
        odd_cnt += 1
print(even_cnt*odd_cnt)
