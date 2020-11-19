N = int(input())
ab = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(len(ab)):
    ans += max(ab[i][0], ab[i][1])
print(ans)
