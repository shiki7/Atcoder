N, X, Y, Z = map(int, input().split())
AB = list(list(map(int, input().split())) for _ in range(N))

ans = 0
for i in range(N):
    a = AB[i][0]
    b = AB[i][1]
    if a >= X and b >= Y and a+b >= Z:
        ans += 1
print(ans)
