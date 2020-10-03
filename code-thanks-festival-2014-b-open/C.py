N = int(input())
V = list(map(int, input().split()))
F = list(map(int, input().split()))
ans = 0
for i in range(N):
    if F[i]*2 > V[i]:
        ans += 1
print(ans)
