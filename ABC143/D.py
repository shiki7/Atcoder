import bisect

n = int(input())
L = list(map(int, input().split()))

ans = 0
L.sort()

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        idx = bisect.bisect_left(L, L[i] + L[j])
        ans += max(0, idx - j - 1)
print(ans)
