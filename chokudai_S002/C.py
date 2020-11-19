N = int(input())
ab = [list(map(int, input().split())) for _ in range(N)]
ans = - float('inf')
for i in range(len(ab)):
    ans = max(ans, ab[i][0] + ab[i][1])
print(ans)
