A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = float('inf')
for i in range(M):
    x, y, c = map(int, input().split())
    ans = min(ans, a[x-1] + b[y-1] - c)
ans = min(ans, min(a) + min(b))
print(ans)
