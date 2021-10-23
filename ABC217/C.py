N = int(input())
p = list(map(int, input().split()))
ans = [0] * N
for i in range(N):
    ans[p[i]-1] = i+1
print(*ans)
