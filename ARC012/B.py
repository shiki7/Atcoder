N, v1, v2, L = map(int, input().split())
for _ in range(N):
    L = v2 * (L / v1)
print(L)
