import math
X, D = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(X)]
ans = 0
for i in range(X - 1):
    for j in range(1, X - i):
        total = 0
        for k in range(D):
            total += abs(x[i + j][k] - x[i][k])**2
        if math.sqrt(total).is_integer():
            ans += 1
print(ans)
