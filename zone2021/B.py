N, D, H = map(int, input().split())
ans = 0
for _ in range(N):
    d, h = map(int, input().split())
    ans = max((D*h-d*H)/(D-d), ans)
print(ans)
