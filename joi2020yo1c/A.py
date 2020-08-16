X, L, R = map(int, input().split())
ans = L
d = float('inf')
for i in range(L, R+1):
    if abs(X-i) < d:
        ans = i
        d = abs(X-i)
print(ans)
