N = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(N):
    ans += 2**(N-i-1) * a[i]
print(ans)
