N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

ans = 0
for i in range(N):
    total = 0
    for j in range(M):
        total += A[i][j] * B[j]
    total += C
    if total > 0:
        ans += 1
print(ans)
