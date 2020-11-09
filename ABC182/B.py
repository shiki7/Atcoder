N = int(input())
a = list(map(int, input().split()))

max_gcd = 0
for i in range(2, max(a)+1):
    cnt = 0
    for j in range(N):
        if a[j] % i == 0:
            cnt += 1
    if cnt >= max_gcd:
        max_gcd = cnt
        ans = i
print(ans)
