N, K = map(int, input().split())
mod = 10**9+7
ans = 0
for i in range(K, N+2):
    a = (i-1)*i//2
    b = (N+(N-i+1))*i//2
    ans += b-a+1
    ans %= mod
print(ans)
