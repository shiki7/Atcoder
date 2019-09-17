a = list(map(int, input().split()))
K = int(input())
a.sort()
ans = a[-1] * (2**K)
for i in range(len(a) - 1):
    ans += a[i]
print(ans)
