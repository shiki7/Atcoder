N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
ans = float('inf')
for i in range(N):
    for j in range(N):
        if i == j:
            ans = min(ans, A[i][0] + A[j][1])
        else:
            ans = min(ans, max(A[i][0], A[j][1]))
print(ans)
