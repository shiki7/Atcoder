def func(x):
    a = min(x-1, 2*N+1-x)
    return max(a, 0)


N, K = map(int, input().split())
ans = 0
for i in range(2, 2*N+1):
    ans += func(i) * func(i-K)
print(ans)
