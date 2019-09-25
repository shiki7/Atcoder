n, m = map(int, input().split())
ab = [map(int, input().split()) for _ in range(m)]
ans = [0] * n
for a, b in ab:
    ans[a - 1] += 1
    ans[b - 1] += 1
for i in ans:
    print(i)
