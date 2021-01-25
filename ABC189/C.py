# pypyにしないとTLEになる
N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(N):
    m = float('inf')
    for j in range(i, N):
        m = min(A[j], m)
        ans = max(ans, m*(j-i+1))
print(ans)
