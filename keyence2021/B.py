N, K = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A)
c = [[-1] for _ in range(K)]

if A[0] == 0:
    c[0].append(A[0])
cnt = 0
for i in range(1, N):
    if A[i] == A[i-1] and cnt < K - 1:
        cnt += 1
    else:
        cnt = 0
    if c[cnt][-1] == A[i] - 1:
        c[cnt].append(A[i])

ans = 0
for i in range(K):
    ans += c[i][-1] + 1
print(ans)
