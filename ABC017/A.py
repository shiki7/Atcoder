se = [list(map(int, input().split())) for _ in range(3)]
ans = 0
for i in range(3):
    ans += se[i][0] * se[i][1] // 10
print(ans)
