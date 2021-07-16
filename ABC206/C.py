N = int(input())
a = sorted(list(map(int, input().split())))+[0]
cnt = 1
ans = N * (N-1) // 2
for i in range(1, N+1):
    if a[i] == a[i-1]:
        cnt += 1
    else:
        if cnt > 1:
            ans -= cnt * (cnt-1) // 2
        cnt = 1
print(ans)
