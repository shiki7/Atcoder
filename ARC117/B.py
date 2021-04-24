N = int(input())
A = [0] + list(map(int, input().split()))
A = sorted(A)
ans = 1
mod = 10**9+7
for i in range(1, N+1):
    ans *= A[i] - A[i-1] + 1
    ans %= mod
print(ans)
