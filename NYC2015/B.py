N = int(input())
a = [int(input()) for _ in range(N)]
a = sorted(a)
total = a[0]
ans = 1
for i in range(1, N):
    if a[i] > total:
        total += a[i]
        ans += 1
print(ans)
