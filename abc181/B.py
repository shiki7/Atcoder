N = int(input())
ab = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    ans += (ab[i][0] + ab[i][1])*(ab[i][1] - ab[i][0]+1)//2
print(ans)
