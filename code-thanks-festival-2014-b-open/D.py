N, T = map(int, input().split())
a = [int(input()) for _ in range(N)]

ans = 0
for i in range(1, T+1):
    cnt = 0
    for j in range(N):
        if i % a[j] == 0:
            cnt += 1
    ans = max(ans, cnt)
print(ans)
